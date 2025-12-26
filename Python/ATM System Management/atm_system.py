"""
Single-file Multi-User ATM Management System (Beginner Friendly)

Features:
- Main menu: Login / Create Account / Exit
- Multi-user with JSON file storage (users.json)
- Account number + PIN login (PIN masked via getpass)
- SHA-256 hashed PINs (no plaintext PIN storage)
- Max 3 failed login attempts -> account lock
- Operations after login:
    1. Balance Inquiry
    2. Deposit
    3. Withdraw
    4. Mini Statement (last 5)
    5. Change PIN
    6. Logout
- Transaction history with timestamp

Files created automatically:
- atm_users.json (in same folder as this script)
"""

import sqlite3  # For database operations
import os      # For checking file existence
import re    # For regular expressions
import hashlib  # Fpr SHA-256 PIN hashing (security)
from datetime import datetime, date   # For transaction timestamps
from getpass import getpass   # For masked PIN input (no echo)
from typing import Dict, Any, Optional, Tuple   # Type hints
from contextlib import contextmanager


# -------------------- CONFIG / CONSTANTS --------------------

DB_FILE = "users.db"   # SQLite database file
MIN_BALANCE = 500   # Minimum balance required in account
DEFAULT_DAILY_WITHDRAW_LIMIT = 20000.0   # Default daily withdrawal limit per account
DEFAULT_ATM_CASH_POOL = 1000000.0   # Default total cash available in ATM
RECEIPTS_FOLDER = "receipts"

# Name validation rules
MAX_NAME_LENGTH = 50
MIN_NAME_LENGTH = 2

# PIN policies
PIN_LENGTH = 4
DISALLOW_SEQUENTIAL = True
DISALLOW_REPEATING = True

# -------------------- SECURITY UTILITIES --------------------

def hash_password(password: str) -> str:
    """Hash a password using SHA-256"""
    salt = "atm_system_secure_salt_2025"
    return hashlib.sha256((password + salt).encode()).hexdigest()

ADMIN_PASSWORD = hash_password("SecureAdmin@2025")

def hash_pin(pin: str) -> str:
    """Hashes the PIN using SHA_256 for secure storage."""
    return hashlib.sha256(pin.encode()).hexdigest()


def validate_pin_strength(pin: str) -> Tuple[bool, str]:
    """
    Validate PIN against security policies.
    Returns: (is_valid, error_message)
    """

    if len(pin) != PIN_LENGTH:
        return False, f"PIN must be {PIN_LENGTH} digits."
    
    if not pin.isdigit():
        return False, "PIN must be numeric."
    
    # Check for repeating digits (e.g., 1111, 2222)
    if DISALLOW_REPEATING and len(set(pin)) == 1:
        return False, "PIN cannot have all repeating digits (e.g., 1111)"
    
    # Check for sequential digits (e.g., 1234, 4321)
    if DISALLOW_SEQUENTIAL:
        is_ascending = all(int(pin[i]) == int(pin[i-1]) + 1 for i in range(1, len(pin)))
        is_descending = all(int(pin[i]) == int(pin[i-1]) - 1 for i in range(1, len(pin)))

        if is_ascending or is_descending:
            return False, "PIN cannot be sequential (e.g., 1234, 4321)"
    return True, ""
    

def sanitize_name(name: str) -> Tuple[bool, str, str]:
    """
    Sanitize and validate user name.
    Returns: (is_valid, sanitized_name, error_message)
    """
    # Remove extra whitespace
    name = " ".join(name.strip().split())

    # Check length
    if len(name) < MIN_NAME_LENGTH:
        return False, "", f"Name must be at least {MIN_NAME_LENGTH} characters."

    if len(name) > MAX_NAME_LENGTH:
        return False, "", f"Name must be at least {MAX_NAME_LENGTH} characters."
    
    # Check for valid character (letters, spaces, hyphens, apostrophes)
    if not re.match(r"^[A-Za-z\s]+$", name):
        return False, "", "Name can only contain letters and spaces."
    
    return True, name, ""


def mask_account_number(account_number: str) -> str:
    """Mask account number for receipts (e.g., 1000000000 -> ****000000)"""
    if len(account_number) <= 4:
        return "****"
    return "*" * (len(account_number) - 4) + account_number[-4:]
    

# -------------------- DB HELPERS --------------------

@contextmanager
# Encapsulate database connection
def get_db_transaction():
    conn = sqlite3.connect(DB_FILE)   # Open a connection to the SQLite database file
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        yield conn, cur
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


# Encapsulate database connection
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)   # Open a connection to the SQLite database file
    conn.row_factory = sqlite3.Row
    return conn   # Return the connection object


def init_db():
    conn = get_db_connection()   # Opening a connection to the database
    cur = conn.cursor()   # Creating a cursor object to execute SQL commands

    # Users table
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    account_number TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    pin_hash TEXT NOT NULL,
                    balance REAL NOT NULL,
                    locked INTEGER NOT NULL DEFAULT 0,
                    failed_attempts INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    last_withdraw_date TEXT DEFAULT NULL
                )
            """)
    
    # Transactions table
    cur.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number TEXT NOT NULL,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                datetime TEXT NOT NULL,
                balance_after REAL NOT NULL,
                FOREIGN KEY (account_number) REFERENCES users (account_number)
                )
            """)
    
    # ATM Settings (for each pool, limits)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atm_cash_pool REAL NOT NULL,
                daily_withdraw_limit REAL NOT NULL,
                admin_password_hash TEXT NOT NULL
                )
            """)
    
    # Insert default ATM settings if not exists
    cur.execute("SELECT COUNT(*) AS count FROM settings")
    if cur.fetchone()["count"] == 0:
        cur.execute("INSERT INTO settings (id, atm_cash_pool, daily_withdraw_limit, admin_password_hash) VALUES(1, ?, ?, ?)",
                    (DEFAULT_ATM_CASH_POOL, DEFAULT_DAILY_WITHDRAW_LIMIT, ADMIN_PASSWORD))
        
    conn.commit()   # Commit changes to the database
    conn.close()   # Close the database connection

    # Create Receipts folder
    if not os.path.exists(RECEIPTS_FOLDER):
        os.makedirs(RECEIPTS_FOLDER)


# -------------------- STORAGE / UTIL FUNCTIONS --------------------

def generate_account_number() -> str:
    """Generate a new 10-digit account number not already in use."""
    conn = get_db_connection()
    cur = conn.cursor()

    base = 1000000000
    while True:
        acc = str(base)
        cur.execute("SELECT 1 FROM users WHERE account_number = ?", (acc,))
        if cur.fetchone() is None:
            conn.close()
            return acc
        base += 1


def get_user(account_number: str) -> Optional[Dict[str, Any]]:
    """Retrieve user row as dict or None if not found."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE account_number = ?", (account_number,))
    row = cur.fetchone()   # Retrieves exactly ONE row from the result set of the most recent SQL query executed by the cursor
    conn.close()
    return dict(row) if row else None


def update_user(user: Dict[str, Any]) -> None:
    """Update user record in DB."""
    with get_db_transaction() as (conn, cur):
        cur.execute("""
            UPDATE users
            SET name = ?, pin_hash = ?, balance = ?, locked = ?, failed_attempts = ?, last_withdraw_date = ?
            WHERE account_number = ?
            """, (
                user["name"],
                user["pin_hash"],
                user["balance"],
                int(user.get("locked", False)),
                user.get("failed_attempts", 0),
                user.get("last_withdraw_date"),
                user["account_number"]
            ))


def create_user_record(account_number: str, name: str, pin_hash: str, initial_deposit: float) -> None:
    """Insert a new user into DB."""
    with get_db_transaction() as (conn, cur):
        cur.execute("""INSERT INTO users (account_number, name, pin_hash, balance, locked, failed_attempts, created_at, last_withdraw_date)
                    VALUES (?, ?, ?, ?, 0, 0, ?, NULL)""", (account_number, name, pin_hash, initial_deposit, datetime.now().isoformat()))


def verify_pin(user: Dict[str, Any], pin: str) -> bool:
    return user["pin_hash"] == hash_pin(pin)


def is_account_locked(user: Dict[str, Any]) -> bool:
    """Check if the account is locked."""
    return bool(user.get("locked", 0))


def lock_account(user: Dict[str, Any]) -> None:
    """Lock user account."""
    user["locked"] = True
    user["failed_attempts"] = 3
    update_user(user)


def reset_failed_attempts(user: Dict[str, Any]) -> None:
    """Reset failed login attempts counter."""
    user["failed_attempts"] = 0
    update_user(user)


def increment_failed_attempts(user: Dict[str, Any]) -> None:
    """Increase failed login attempts and lock after 3."""
    user["failed_attempts"] = user.get("failed_attempts", 0) + 1
    if user["failed_attempts"] >= 3:
        user["locked"] = True
    update_user(user)


def record_transaction(account_number: str, tx_type: str, amount: float, balance_after: float) -> None:
    """Record a transaction in the transactions table."""
    with get_db_transaction() as (conn, cur):
        cur.execute("""
                    INSERT INTO transactions (account_number, type, amount, datetime, balance_after)
                    VALUES(?, ?, ?, ?, ?)
                    """, (account_number, tx_type, amount, datetime.now().isoformat(), balance_after))
    return cur.lastrowid


def get_today_withdrawn_amount(account_number: str) -> float:
    """Return total withdraw today for this account."""
    user = get_user(account_number)
    if not user:
        return 0.0
    
    last_withdraw_date = user.get("last_withdraw_date")
    today = date.today().isoformat()

    # If no withdrawals today, return 0
    if last_withdraw_date != today:
        return 0.0
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
                SELECT COALESCE(SUM(amount), 0) AS total
                FROM transactions
                WHERE account_number = ?
                AND type = 'WITHDRAW'
                AND date(datetime) = date('now', 'localtime')
                """, (account_number,))
    row = cur.fetchone()
    conn.close()
    return float(row['total'] if row else 0.0)


def get_settings() -> Dict[str, Any]:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM settings WHERE id = 1")
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {"atm_cash_pool": 0.0, "daily_withdraw_limit": DEFAULT_DAILY_WITHDRAW_LIMIT, "admin_password_hash": ADMIN_PASSWORD}


def update_atm_cash_pool(new_amount: float) -> None:
    with get_db_transaction() as (conn, cur):
        cur.execute("UPDATE settings SET atm_cash_pool = ? WHERE id = 1", (new_amount,))


# -------------------- RECEIPT GENERATION --------------------------

def generate_receipt(account_number: str, tx_id: int, tx_type: str, amount: float, balance_after: float, additional_info: str = "") -> str:
    """
    Generate a receipt file for a transaction
    Returns th receipt filename.
    """
    user = get_user(account_number)
    timestamp = datetime.now()
    masked_account = mask_account_number(account_number)

    # Create filename
    filename = f"receipt_{account_number}_{timestamp.strftime('%d%m%Y_%H%M%S')}_{tx_id}.txt"
    filepath = os.path.join(RECEIPTS_FOLDER,filename)

    # Generate receipt content
    receipt = f"""
    {"=" * 50}
                  ATM TRANSACTION RECEIPT
    {"=" * 50}
    Date/Time      : {timestamp.strftime('%d-%m-%Y %H:%M:%S')}
    Transcation ID : {tx_id:08d}

    Account        : {masked_account}
    Name           : {user['name'] if user else "Unknown"}

    Transaction    : {tx_type}
    Amount         : {amount:.2f}
    Balance After  : {balance_after:.2f}

    {additional_info}

    {"=" * 50}
            Thank you for using our ATM service!
    {"=" * 50}
    """

    # Save receipt to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(receipt)
    
    return filename
    

# -------------------- AUTHENTICATION FUNCTIONS --------------------

def verify_admin_password() -> bool:
    """Verify admin password against stored hash."""
    settings = get_settings()
    password = getpass("Enter admin password: ")

    # Hash input and compare
    input_hash = hash_password(password)

    if input_hash != settings['admin_password_hash']:
        print('Incorrect admin password.')
        return False
    return True


def login() -> Tuple[Optional[str], Optional[Dict[str, Any]]]:
    print("\n=== Login ===")
    acc = input("Enter account number: ").strip()
    user = get_user(acc)

    if not user:
        print("Account not found.")
        return None, None
    
    if is_account_locked(user):
        print("Account is locked due to multiple failed login attempts.")
        return None, None
    
    for _ in range(3):
        pin = getpass("Enter 4-digit PIN: ").strip()

        if not pin.isdigit() or len(pin) != 4:
            print("PIN must be a 4-digit numnber.")
            increment_failed_attempts(user)
        elif verify_pin(user, pin):
            print("Login successful.")
            reset_failed_attempts(user)
            return acc, get_user(acc)   # refresh fresh user data
        else:
            print("Incorrect PIN.")
            increment_failed_attempts(user)
            user = get_user(acc)   # reload to get update failed attempts/locked status

            remaining = 3 - user["failed_attempts"]
            if remaining > 0 and not user["locked"]:
                print("Atttempts remaining:", remaining)
            else:
                print('Account locked due to mutiple failed attempts.')
                return None, None
        
    return None, None


def create_account() -> None:
    """Register a new user account."""
    print("\n=== Create Account ===")
    while True:
        name = input("Enter your name: ").strip().capitalize()
        is_valid, sanitize_named, error = sanitize_name(name)
        if not is_valid:
            print(f"{error}.")
            continue
        break 
    
    # PIN input and confirmation
    while True:
        pin = getpass("Set a 4-digit numeric PIN: ")
        confirm = getpass("Confirm PIN: ") 

        if pin != confirm:
            print("PINs do not match. Try again.")
            continue
        
        is_valid, error = validate_pin_strength(pin)
        if not is_valid:
            print(f"{error}")
            print("PIN Policy:")
            print(f"  - Must be {PIN_LENGTH} digits.")
            print("  - Cannot have repeating digits (e.g., 1111).")
            print("  - Cannot have sequential digits (e.g., 1234).")
            continue
        break

    # Initial deposit
    while True:
        try:
            amount = float(input(f"Enter initial deposit (min {MIN_BALANCE}):"))
            if amount < MIN_BALANCE:
                print(f"Minimum initial deposit is {MIN_BALANCE}.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Create user record
    pin_hash = hash_pin(pin)
    account_number = generate_account_number()
    create_user_record(account_number, sanitize_named, pin_hash, amount)
    tx_id = record_transaction(account_number, "DEPOSIT", amount, amount)

    # Generate receipt
    receipt_file = generate_receipt(
        account_number, tx_id, "ACCOUNT CREATION - INITIAL DEPOSIT",
        amount, amount, "Welcome to out ATM service!"
    )

    print("\n" + "=" * 50)
    print("\nACCOUNT CREATED SUCCESSFULLY!")
    print("=" * 50)
    print(f"Your account number is: {account_number}")
    print(f"Name: {sanitize_named}")
    print(f"Initial Balance: {amount:.2f}")
    print(f"Receipt saved: {receipt_file}")
    print("IMPORTANT: Remember your account number and PIN!")
    print("=" * 50)

    
# -------------------- ATM OPERATIONS --------------------

def balance_inquiry(account_number: str) -> None:
    """Show current balance and record a BALANCE transaction"""
    user = get_user(account_number)
    if not user:
        print("User not found.")
        return
    
    print("\n" + "=" * 50)
    print("BALANCE INQUIRY")
    print("=" * 50)
    print(f"\nCurrent balance: {user['balance']:.2f}")
    print("=" * 50)

    tx_id = record_transaction(account_number, "BALANCE", 0.0, user["balance"])


def deposit(account_number: str) -> None:
    """Deposit money into the account."""
    user = get_user(account_number)
    if not user:
        print("User not found.")
        return
    
    print("\n" + "=" * 50)
    print("           DEPOSIT")
    print("=" * 50)
    print(f"\nCurrent balance: {user['balance']:.2f}")

    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        print("Invalid amount.")
        return 
    
    if amount <= 0:
        print("Amount must be positive.")
        return
    
    try:
        with get_db_transaction() as (conn, cur):
            # Update balance
            new_balance = user['balance'] + amount
            cur.execute("""
                    UPDATE users SET balance = ? WHERE account_number = ?
                    """, (new_balance, account_number))
            
            # Record transaction
            cur.execute("""
                        INSERT INTO transactions (account_number, type, amount, datetime, balance_after)
                        VALUES (?, ?, ?, ?, ?)
                        """, (account_number, "DEPOSIT", amount, datetime.now().isoformat(), new_balance))
            tx_id = cur.lastrowid

        # Generate receipt
        receipt_file = generate_receipt(account_number, tx_id, "DEPOSIT", amount, new_balance)

        print("\nDeposit successful!")
        print(f"New Balance: {new_balance:.2f}")
        print(f"Receipt save {receipt_file}")
        print("=" * 50)

    except Exception as e:
        print(f"Transaction failed: {str(e)}")
        print("Your balance has not been changed.")


def withdraw(account_number: str) -> None:
    """Withdraw with full transaction rollback protection."""
    user = get_user(account_number)
    if not user:
        print("User not found.")
        return
    
    settings = get_settings()
    atm_cash = settings["atm_cash_pool"]
    daily_limit = settings["daily_withdraw_limit"]

    print("\n" + "=" * 70)
    print("WITHDRAW")
    print("=" * 70)
    print(f"\nCurrent balance: {user['balance']:.2f}")
    print(f"Minimum balance: {MIN_BALANCE:.2f}")
    print(f"Available : {max(0, user['balance'] - MIN_BALANCE):.2f}")
    print(f"Daily withdraw limit: {daily_limit:.2f}")
    print(f"ATM cash: {atm_cash:.2f}")

    try:
        amount = float(input("\nEnter withdrawal amount: "))
    except ValueError:
        print("Invalid amount.")
        return 
    
    if amount <= 0:
        print("Amount must be positive.")
        return 
    
    # Check min balance rule
    if user['balance'] - amount < MIN_BALANCE:
        max_withdrawable = max(0.0, user['balance'] - MIN_BALANCE)
        print(f"Cannot withdraw. Minimum balance of {MIN_BALANCE:.2f} must remain")
        print(f"You can withdraw up to: {max_withdrawable:.2f}")
        return 
    
    # Check daily limit
    today_withdraw = get_today_withdrawn_amount(account_number)
    if today_withdraw + amount > daily_limit:
        remaining = max(0.0, daily_limit - today_withdraw)
        print("\nCannot withdraw this amount due to daily limit.")
        print(f"Daily limit: {daily_limit:.2f}")
        print(f"Already withdraw today: {today_withdraw:.2f}")
        print(f"Reamining today: {remaining:.2f}")
        return 
    
    if amount > atm_cash:
        print("\nATM does not have enough cash.")
        print(f"ATM available cash: {atm_cash:.2f}")
        return 
    
    # Execute withdrawal with transaction protection
    try:
        with get_db_transaction() as (conn, cur):
            new_balance = user['balance'] - amount
            today = date.today().isoformat()
            cur.execute("""
                        UPDATE users
                        SET balance = ?, last_withdraw_date = ?
                         WHERE account_number = ?
                        """, (new_balance, today, account_number))
            
            # Update ATM cash pool
            new_atm_cash = atm_cash - amount
            cur.execute("""
                        UPDATE settings SET atm_cash_pool = ? WHERE id = 1
                        """, (new_atm_cash,))
            
            # Record transcation
            cur.execute("""
                        INSERT INTO transactions (account_number, type, amount, datetime, balance_after)
                        VALUES(?, ?, ?, ?, ?)
                        """, (account_number, "WITHDRAW", amount, datetime.now().isoformat(), new_balance))
            

            tx_id = cur.lastrowid

            # Generate receipt
            additional_info = f"ATM Cash After: {new_atm_cash:.2f}\nDaily Withdraw: {today_withdraw + amount:.2f}"
            receipt_file = generate_receipt(account_number, tx_id, "WITHDRAW", amount, new_balance, additional_info)

            print(f"{amount:.2f} Withdrawn successfully.")
            print(f"New balance: {user['balance']:.2f}")
            print(f"ATM Cash Remaining: {new_atm_cash:.2f}")
            print(f"Receipt saved: {receipt_file}")
            print("=" * 70)

    except Exception as e:
        print(f"Transaction failed and rooled back: {str(e)}")
        print("Your balance and ATM cash have not been changed.")


def mini_statement(account_number: str) -> None:
    """Show last 5 transactions."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
                SELECT datetime, type, amount, balance_after
                FROM transactions
                WHERE account_number = ?
                ORDER BY id DESC
                LIMIT 5
                """, (account_number,))
    rows = cur.fetchall()
    conn.close()
    
    print("\n" + "=" * 70)
    print("\nMINI STATEMENT (Last 5 Transactions)")
    print("\n" + "=" * 70)

    if not rows:
        print("No Transactions found.")
        return 
    
    for tx in rows:
        print(f"[{tx['datetime']}] {tx['type']} "
              f"Amount: {tx['amount']:.2f} | Balance: {tx['balance_after']:.2f}")
    print("\n" + "=" * 70)


def change_pin(account_number: str) -> None:
    """Change the user's PIN."""
    user = get_user(account_number)
    if not user:
        print("User not found.")
        return
    
    print("\n" + "=" * 70)
    print("CHANGE PIN")
    print("\n" + "=" * 70)
    
    old_pin = getpass("Enter current PIN: ")
    if not verify_pin(user, old_pin):
        print("Incorrect current PIN.")
        return
    
    print("\nSet new PIN")
    print("PIN policy")
    print(f"  - Must be {PIN_LENGTH} digits.")
    print(f"  - Caanot be all same digits (e.g., 1111).")
    print(f"  - Cannot be sequential (e.g., 1234)")
    print()
    
    while True:
        new_pin = getpass("Enter new 4-digit PIN: ")
        confirm = getpass("Confirm new PIN: ")

        if new_pin != confirm:
            print("PINs do not match. Try again.")
            continue

        if new_pin == old_pin:
            print("New PIN cannot be the same as the old PIN.")
            continue

        is_valid, error = validate_pin_strength(new_pin)
        if not is_valid:
            print(f"{error}")
            continue

        break

    user["pin_hash"] = hash_pin(new_pin)
    update_user(user)
    tx_id = record_transaction(account_number, "PIN CHANGE", 0.0, user["balance"])  

    print("PIN Changed successfully.")
    print("=" * 70)


# -------------------- ADMIN FUNCTIONS --------------------

def admin_unlock_account():
    """Admin function to unlock a locked account."""
    print("\n" + "=" * 70)
    print("         ADMIN UNLOCK ACCOUNT")
    print("=" * 70)

    if not verify_admin_password():
        return 
    
    # Show all locked account
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
                SELECT account_number, name, failed_attempts
                FROM users
                WHERE locked = 1
                ORDER BY account_number
                """)
    locked_accounts = cur.fetchall()
    conn.close()

    if not locked_accounts:
        print("\nNo locked accounts found.")
        return 
    
    print("Locked Accounts")
    print("-" * 70)
    for acc in locked_accounts:
        print(f"    Account: {acc['account_number']}")
        print(f"    Name: {acc['name']}")
        print(f"    Failed Attempts: {acc['failed_attempts']}")
        print()

    account_number = input("Enter account number to unlock (or 'all' for all): ").strip()
    if account_number.lower() == "all":
        with get_db_transaction() as (conn, cur):
            cur.execute("""
                        UPDATE users
                        SET locked = 0, failed_attempts = 0
                        WHERE locked = 1
                    """)
        rows_affected = cur.rowcount
        print(f"Unlock {rows_affected} accounts(s)")
    else:
        # Unlock specific account
        user = get_user(account_number)

        if not user:
            print("Account not found.")
            return

        if not user["locked"]:
            print("Account is not locked.")
            return 
        
        user["locked"] = False
        user["failed_attempts"] = 0
        update_user(user)

        # Log admin action
        record_transaction(account_number, "ADMIN_UNLOCK", 0.0, user['balance'])

        print(f"\nAccount {account_number} ({user['name']}) has been unlocked.")
        print("    User can now login again.")
    
    print("=" * 70)


def admin_view_all_accounts():
    """Admin function to view all accounts."""
    print("\n" + "=" * 70)
    print("    ADMIN: VIEW ALL ACCOUNTS")
    print("=" * 70)

    if not verify_admin_password():
        return
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(""" 
                SELECT account_number, name, balance, locked, failed_attempts
                FROM users
                ORDER BY account_number
                """)
    accounts = cur.fetchall()
    conn.close()

    if not accounts:
        print("\nNo accounts found.")
        return 
    
    print(f"\n{'Acount':<15} {'Name':<20} {'Balance':<12} {'Status':<10} {'Failed':<8}")
    print("-" * 70)

    for acc in accounts:
        locked_status = "LOCKED" if acc['locked'] else "ACTIVE"
        print(f"{acc['account_number']:<15} {acc['name']:<20} ₹{acc['balance']:<10.2f} {locked_status:<10} {acc['failed_attempts']:<10}")
    print("-" * 70)
    print(f"Total Accounts: {len(accounts)}")
    print("=" * 70)


def admin_view_atm_cash():
    """View current ATM cash pool."""
    print("\n" + "=" * 70)
    print("    ADMIN: ATM CASH POOL")
    print("=" * 70)

    if not verify_admin_password():
        return 
    
    settings = get_settings()

    print(f"\nCurrent ATM Cash Pool: {settings['atm_cash_pool']:.2f}")
    print(f"Daily Withdraw Limit: {settings['daily_withdraw_limit']:.2f}")
    print("=" * 70)


def admin_refill_atm():
    """Admin function to refill ATM cash pool."""
    print("\n" + "=" * 70)
    print("    ADMIN: REFILL ATM CASH")
    print("=" * 70)

    if not verify_admin_password():
        return 
    
    settings = get_settings()
    print(f"\nCurrent ATM Cash Pool: {settings['atm_cash_pool']:.2f}")

    try:
        amount = float(input("Enter amount to add: "))
    except ValueError:
        print("Invalid amount.")
        return 
    
    if amount <= 0:
        print("Amount must be positive.")
        return 
    
    new_pool = settings['atm_cash_pool'] + amount
    update_atm_cash_pool(new_pool)

    print(f"    ATM cash pool updated!")
    print(f"    Previous: {settings['atm_cash_pool']:.2f}")
    print(f"    Added: {amount:.2f}")
    print(f"    New Total: {new_pool:.2f}")
    print("=" * 70)


def admin_change_password():
    """Change admin password."""
    print("\n" + "=" * 70)
    print("     ADMIN: CHANGE PASSWORD")
    print("=" * 70)

    if not verify_admin_password():
        return 
    
    print("\nSet new admin password")
    print("Requirments:")
    print("  - Minimum 8 characters.")
    print("  - Mix of letters, numbers, and symbols recommended.")
    print()

    while True:
        new_password = getpass("Enter new admin password: ")
        if len(new_password) < 8:
            print("Password must be least 8 characters.")
            continue

        confirm = getpass("Confirm new password: ")
        if new_password != confirm:
            print("Passwords do not match. Try again.")
            continue

        break

    new_hash = hash_password(new_password)

    with get_db_transaction() as (conn, cur):
        cur.execute("UPDATE settings SET admin_password_hash = ? WHERE id = 1", (new_hash,))

    print("\nAdmin password changed successfully!")
    print("Please remember your new password!")
    print("=" * 70)


def admin_view_transaction():
    """View recent transactions across all accounts."""
    print("\n" + "=" * 70)
    print("    ADMIN: RECENT TRANSACTIONS")
    print("=" * 70)

    if not verify_admin_password():
        return 
    
    try: 
        limit = int(input("\n How many recent transactions to show? (default 10): "))
    except ValueError:
        limit = 10

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
                SELECT t.datetime, t.account_number, u.name, t.type, t.amount, t.balance_after
                FROM transactions t
                JOIN users u ON t.account_number = u.account_number
                ORDER by t.id DESC
                LIMIT ?
                """, (limit, ))
    transactions = cur.fetchall()
    conn.close()

    if not transactions:
        print("\nNo transactions found.")
        return
    
    print(f"\n{'Date/Time':<20} {'Account':<12} {'Name':<15} {'Type':<12} {'Amount':<10} {'Balance':<10}")
    print("-" * 90)
    for tx in transactions:
        dt = tx['datetime'][:19]
        print(f"{dt:<20} {tx['account_number']:<12} {tx['name']:<15} {tx['type']:<12} ₹{tx['amount']:<8.2f} ₹{tx['balance_after']:<8.2f}")
    print("-" * 90)
    print("=" * 70)
    

# -------------------- MENUS --------------------

def atm_menu(account_number: str) -> None:
    """Display ATM operatins menu for logged-in user."""
    user = get_user(account_number)
    if not user:
        print("user not found")
        return 
    
    while True:
        print("\n" + "=" * 70)
        print(f"                    ATM MENU ({user['name']})")
        print(f"    Welcome {user['name']},")
        print(f"    Account Number: {account_number}")
        print("    1. Balance Inquiry")
        print("    2. Deposit")
        print("    3. Withdraw")
        print("    4. Mini Statement")
        print("    5. Change PIN")
        print("    6. Logout")
        print("=" * 70)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            balance_inquiry(account_number)
        elif choice == "2":
            deposit(account_number)
        elif choice == "3":
            withdraw(account_number)
        elif choice == "4":
            mini_statement(account_number)
        elif choice == "5":
            change_pin(account_number)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")


def admin_menu():
    """Admin submenu for management tasks."""
    while True:
        print("\n" + "=" * 70)
        print("                        ADMIN PANEL")
        print("=" * 70)
        print("    1. Unlock Account")
        print("    2. View All Accounts")
        print("    3. View ATM Cash Pool")
        print("    4. Refill ATM cash")
        print("    5. View Recent Transactions")
        print("    6. Change Admin Password")
        print("    7. Back to Main menu")
        print("=" * 70)

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            admin_unlock_account()
        elif choice == "2":
            admin_view_all_accounts()
        elif choice == "3":
            admin_view_atm_cash()
        elif choice == "4":
            admin_refill_atm()
        elif choice == "5":
            admin_view_transaction()
        elif choice == "6":
            admin_change_password()
        elif choice == "7":
            print("\nReturning to main menu...")
            break
        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")


def main_menu() -> None:
    """Main menu: login, create account, exit"""
    while True:
        print("\n" + "=" * 70)
        print("                             MAIN MENU")
        print("=" * 70)
        print("    1. Login")
        print("    2. Create Account")
        print("    3. Admin Panel")
        print("    4. Exit")
        print("=" * 70)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            acc, user = login()
            if acc and user:
                atm_menu(acc)
        elif choice == "2":
            create_account()
        elif choice == "3":
            admin_menu()
        elif choice == "4":
            print("\n" + "=" * 70)
            print("   Thank you for using Python system. Goodbye!")
            print("=" * 70)
            break
        else:
            print("Invalid choice. Please try again.")

# -------------------- ENTRY POINT --------------------

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("    Initializing ATM System...")
    print("=" * 70)
    init_db()   # Initialize database and tables
    print("    Database initialized successfully.")
    print("Receipts folder created!")
    print("Default Admin Password; SecureAdmin@2025")
    print("Change it immediately via Admin Panel!")
    print("=" * 70)
    main_menu()

