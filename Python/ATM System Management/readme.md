# ATM Management System

A comprehensive, production-ready multi-user ATM banking system implemented in Python with SQLite database backend, featuring advanced security measures, transaction management, and administrative controls.

## Overview

This single-file ATM system provides a complete banking simulation with user authentication, transaction processing, receipt generation, and administrative management capabilities. The application implements industry-standard security practices including PIN hashing, account lockout mechanisms, and transaction rollback protection.

## Features

### User Operations

- **Account Management**: Create new accounts with validated names, secure PINs, and minimum initial deposit requirements
- **Secure Authentication**: Login system with masked PIN input (using getpass), SHA-256 hashed credentials, and automatic account lockout after 3 failed attempts
- **Banking Transactions**:
    - Balance inquiry with transaction logging
    - Cash deposits with real-time balance updates
    - Withdrawals with multiple validation checks (minimum balance, daily limits, ATM cash availability)
    - Mini statement showing last 5 transactions
    - PIN change functionality with strength validation
- **Receipt Generation**: Automated receipt files saved to local folder for all transactions with masked account numbers and timestamps


### Administrative Features

- **Account Management**: View all accounts, unlock locked accounts (individual or bulk)
- **ATM Cash Management**: Monitor ATM cash pool, refill cash reserves
- **Transaction Monitoring**: View recent transactions across all accounts with customizable limits
- **Security**: Change admin password with minimum strength requirements
- **Protected Access**: All admin functions require password authentication


### Security Implementation

**PIN Security Policies**:

- 4-digit numeric PIN requirement
- SHA-256 hashing for secure storage (no plaintext PINs)
- Validation rules to prevent weak PINs:
    - Disallows repeating digits (e.g., 1111, 2222)
    - Disallows sequential digits (e.g., 1234, 4321)
- PIN confirmation during account creation and changes

**Account Protection**:

- Maximum 3 failed login attempts before automatic account lock
- Failed attempt counter with remaining attempts notification
- Admin-only unlock capability
- Last withdrawal date tracking for daily limit enforcement

**Input Validation**:

- Name sanitization (2-50 characters, letters and spaces only)
- Account number masking in receipts (shows last 4 digits only)
- Transaction amount validation (positive numbers, sufficient balance checks)
- Regular expression-based pattern matching for secure input handling


## Technical Architecture

### Database Schema

**Users Table**:

```sql
account_number TEXT PRIMARY KEY
name TEXT NOT NULL
pin_hash TEXT NOT NULL
balance REAL NOT NULL
locked INTEGER NOT NULL DEFAULT 0
failed_attempts INTEGER NOT NULL DEFAULT 0
created_at TEXT NOT NULL
last_withdraw_date TEXT DEFAULT NULL
```

**Transactions Table**:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
account_number TEXT NOT NULL (Foreign Key)
type TEXT NOT NULL
amount REAL NOT NULL
datetime TEXT NOT NULL
balance_after REAL NOT NULL
```

**Settings Table**:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
atm_cash_pool REAL NOT NULL
daily_withdraw_limit REAL NOT NULL
admin_password_hash TEXT NOT NULL
```


### Configuration Constants

- `DB_FILE`: SQLite database filename ("users.db")
- `MIN_BALANCE`: Minimum account balance required (₹500)
- `DEFAULT_DAILY_WITHDRAW_LIMIT`: Daily withdrawal cap (₹20,000)
- `DEFAULT_ATM_CASH_POOL`: Initial ATM cash reserves (₹1,000,000)
- `RECEIPTS_FOLDER`: Directory for transaction receipts ("receipts")
- `PIN_LENGTH`: Required PIN digit count (4)
- `MAX_NAME_LENGTH`: Maximum characters in name (50)
- `MIN_NAME_LENGTH`: Minimum characters in name (2)


### Core Functions

**Database Management**:

- `init_db()`: Creates tables and initializes default settings
- `get_db_connection()`: Returns SQLite connection with Row factory
- `get_db_transaction()`: Context manager for transaction-safe operations with automatic commit/rollback

**User Operations**:

- `generate_account_number()`: Creates unique 10-digit account numbers starting from 1000000000
- `get_user()`: Retrieves user record as dictionary
- `create_user_record()`: Inserts new user with hashed PIN and initial deposit
- `update_user()`: Updates user record in database
- `verify_pin()`: Compares hashed PIN for authentication

**Security Functions**:

- `hash_pin()`: SHA-256 hashing for PIN storage
- `hash_password()`: SHA-256 with salt for admin password
- `validate_pin_strength()`: Enforces PIN complexity policies
- `sanitize_name()`: Validates and normalizes user names
- `mask_account_number()`: Masks account numbers for privacy (e.g., ****0000)

**Transaction Processing**:

- `record_transaction()`: Logs all transactions with timestamp and balance
- `get_today_withdrawn_amount()`: Calculates total withdrawals for current day
- `generate_receipt()`: Creates formatted text receipt files with transaction details

**ATM Operations**:

- `balance_inquiry()`: Displays current balance and records inquiry transaction
- `deposit()`: Processes deposits with transaction safety and receipt generation
- `withdraw()`: Executes withdrawals with comprehensive validation:
    - Minimum balance enforcement
    - Daily limit checking
    - ATM cash availability verification
    - Transaction rollback on failure
- `mini_statement()`: Displays last 5 transactions with datetime, type, amount, and balance
- `change_pin()`: Updates PIN after verifying current PIN and validating new PIN strength

**Administrative Functions**:

- `admin_unlock_account()`: Unlocks specific or all locked accounts
- `admin_view_all_accounts()`: Lists all accounts with balance and status
- `admin_view_atm_cash()`: Shows current ATM cash pool and daily limits
- `admin_refill_atm()`: Adds cash to ATM reserves
- `admin_view_transaction()`: Displays recent transactions across all accounts
- `admin_change_password()`: Updates admin password with minimum 8-character requirement
- `verify_admin_password()`: Authenticates admin access for sensitive operations


## Installation & Setup

### Requirements

```python
sqlite3  # Built-in with Python 3.x
os
re
hashlib
datetime
getpass
typing
contextlib
```


### Running the Application

1. Save the `atm_system.py` file to your desired directory
2. Run the script:

```bash
python atm_system.py
```

3. The system automatically creates:
    - `users.db` SQLite database file
    - `receipts/` folder for transaction receipts
    - Default admin credentials (password: `SecureAdmin@2025`)

### Initial Configuration

**Default Settings**:

- ATM Cash Pool: ₹1,000,000
- Daily Withdrawal Limit: ₹20,000
- Minimum Account Balance: ₹500
- Admin Password: `SecureAdmin@2025` (change immediately via Admin Panel)


## Usage Guide

### Creating an Account

1. Select "Create Account" from main menu
2. Enter your full name (2-50 characters, letters only)
3. Set a 4-digit PIN:
    - Must be numeric
    - Cannot be all same digits (1111)
    - Cannot be sequential (1234, 4321)
4. Confirm PIN
5. Make initial deposit (minimum ₹500)
6. Receive account number and receipt

### User Login \& Operations

1. Select "Login" from main menu
2. Enter 10-digit account number
3. Enter 4-digit PIN (masked input)
4. Access ATM operations:
    - Check balance
    - Deposit funds
    - Withdraw cash (subject to limits and ATM availability)
    - View mini statement
    - Change PIN
    - Logout

### Withdrawal Process

The system validates multiple conditions before processing withdrawals:

- Account must have sufficient balance beyond minimum (₹500)
- Total daily withdrawals cannot exceed limit (₹20,000)
- ATM must have sufficient cash reserves
- All checks pass before deducting balance or ATM cash
- Transaction rolls back automatically on any failure


### Administrative Access

1. Select "Admin Panel" from main menu
2. Enter admin password
3. Available operations:
    - Unlock locked accounts (individual or bulk unlock all)
    - View all user accounts with balances and status
    - Monitor ATM cash pool levels
    - Refill ATM cash reserves
    - View recent transactions across all accounts
    - Change admin password

## Transaction Types

The system logs the following transaction types:

- `DEPOSIT`: Cash deposits to account
- `WITHDRAW`: Cash withdrawals from account
- `BALANCE`: Balance inquiry operations
- `PIN CHANGE`: PIN modification events
- `ACCOUNT CREATION - INITIAL DEPOSIT`: New account setup
- `ADMIN_UNLOCK`: Administrative account unlock actions


## Receipt Format

Each transaction generates a formatted receipt file containing:

- Transaction date/time (DD-MM-YYYY HH:MM:SS format)
- Unique transaction ID (8-digit)
- Masked account number (last 4 digits visible)
- Account holder name
- Transaction type
- Transaction amount
- Balance after transaction
- Additional information (for withdrawals: ATM cash remaining, daily withdrawal total)

Receipt filename format: `receipt_{account_number}_{DDMMYYYY_HHMMSS}_{transaction_id}.txt`

## Security Considerations

### Password Hashing

- **PIN Hashing**: SHA-256 without salt for simplicity (consider adding unique salt per user for production)
- **Admin Password**: SHA-256 with static salt (`atm_system_secure_salt_2025`)
- **No Plaintext Storage**: All credentials stored as irreversible hashes


### Account Lockout Mechanism

- Automatic lock after 3 consecutive failed PIN attempts
- Failed attempt counter visible to user
- Admin-only unlock capability prevents unauthorized access recovery
- Lock status persists across sessions via database


### Transaction Safety

- **Context Manager Pattern**: Uses `get_db_transaction()` for automatic commit/rollback
- **ACID Compliance**: SQLite ensures atomic operations
- **Validation Before Execution**: All constraints checked before modifying data
- **Rollback Protection**: Failed transactions automatically roll back without partial updates


### Input Sanitization

- Regular expression validation for names
- Type checking for numeric inputs
- Whitespace normalization
- Length constraints enforcement
- SQL injection prevention via parameterized queries


## Error Handling

The system implements comprehensive error handling:

- Database connection failures with automatic rollback
- Invalid input validation with user-friendly error messages
- Transaction failures with detailed error reporting
- Account status checks (locked, insufficient balance, etc.)
- File I/O error handling for receipt generation


## Future Enhancements

Potential improvements for production deployment:

- Add unique salt per user for PIN hashing
- Implement transaction reversal/refund functionality
- Add multi-factor authentication
- Create user-specific withdrawal limits
- Implement transaction search and filtering
- Add email/SMS notifications for transactions
- Create web-based interface
- Add account closure functionality
- Implement interest calculation on savings
- Add support for multiple currencies
- Create detailed audit logs for compliance


## License

This project is designed for educational purposes and demonstrates core banking system concepts including database management, security implementation, and transaction processing.

## Default Admin Credentials

**Username**: Admin
**Password**: `SecureAdmin@2025`

⚠️ **Security Warning**: Change the default admin password immediately after first login via the Admin Panel → Change Admin Password option.[^1]

***

