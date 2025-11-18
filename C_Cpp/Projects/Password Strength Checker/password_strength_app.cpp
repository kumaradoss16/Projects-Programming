#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <cctype> //standard library header that provides functions for character classification and manipulation.
using namespace std;

// ANSI color codes
namespace Color
{
    const string RESET = "\033[0m";
    const string RED = "\033[31m";
    const string GREEN = "\033[32m";
    const string YELLOW = "\033[33m";
    const string CYAN = "\033[36m";
    const string BLUE = "\033[34m";
}

// Blacklisted Passwords
vector<string> blacklist = {"password", "123456", "qwerty", "admin", "letmein", "welcome", "iloveyou", "abc123", "pass123", "000000"};

// Function: Check if password is blacklisted
bool isBlacklisted(const string &pwd)
{
    for (auto &b : blacklist)
    {
        if (pwd == b)
            return true;
    }
    return false;
}

// Calculate entropy (Shannon)
double calculateEntropy(const string &pwd)
{
    int charset = 0;
    bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false;

    for (char c : pwd)
    {
        if (islower(c))
            hasLower = true;
        else if (isupper(c))
            hasUpper = true;
        else if (isupper(c))
            hasDigit = true;
        else
            hasSpecial = true;
    }

    if (hasLower)
        charset += 26;
    if (hasUpper)
        charset += 26;
    if (hasDigit)
        charset += 10;
    if (hasSpecial)
        charset += 32;

    return pwd.length() * log2(charset);
}

// Score Bar Graph

string barGraph(int score)
{
    string bar = "[";
    for (int i = 0; i < 5; i++)
    {
        if (i < score)
            bar += "#";
        else
            bar += "=";
    }
    bar += "]";
    return bar;
}

// Improvement Suggestions
vector<string> getSuggestions(bool rules[], bool blacklisted)
{
    vector<string> s;
    if (!rules[0])
        s.push_back("Increase length to at least 8 characters");
    if (!rules[1])
        s.push_back("Add uppercase letters");
    if (!rules[2])
        s.push_back("Add lowercase lettes");
    if (!rules[3])
        s.push_back("Add digits");
    if (!rules[4])
        s.push_back("Add special characters");
    if (blacklisted)
        s.push_back("Avoid common passwords (backlisted)");
    return s;
}

// Function to Calculate Password Strength
int checkStrength(const string &password, bool rules[])
{
    int score = 0;

    // Rule 1: Minumum Length
    if (password.length() >= 8)
    {
        rules[0] = true;
        score++;
    }

    // Rule 2 : Uppercase Letter
    for (char c : password)
    {
        if (isupper(c))
        {
            rules[1] = true;
            score++;
            break;
        }
    }

    // Rule 3 : Lowercase Letter
    for (char c : password)
    {
        if (islower(c))
        {
            rules[2] = true;
            score++;
            break;
        }
    }

    // Rule 4 : Digit
    for (char c : password)
    {
        if (isdigit(c))
        {
            rules[3] = true;
            score++;
            break;
        }
    }

    // Rule 5: Special Character
    string special = "!@#$%^&*()-_=+{}[]|;:'\",.<>/?`~";
    for (char c : password)
    {
        if (special.find(c) != string::npos)
        {
            rules[4] = true;
            score++;
            break;
        }
    }

    return score;
}

// Convert score -> Strength Message
string getStrengthMessage(int score)
{
    switch (score)
    {
    case 0:
    case 1:
        return Color::RED + "Very Weak" + Color::RESET;
    case 2:
        return Color::YELLOW + "Medium" + Color::RESET;
    case 3:
        return Color::CYAN + "Strong" + Color::RESET;
    case 4:
    case 5:
        return Color::GREEN + "Very Strong" + Color::RESET;
    }

    return "Unknown";
}

int main()
{
    int n;
    cout << "Enter number of passwords to check: ";
    cin >> n;
    cin.ignore(); // To ignore the newline character after integer input

    vector<string> passwords(n);
    cout << "Enter passwords (each on a new line):" << endl;

    for (int i = 0; i < n; i++)
    {
        getline(cin, passwords[i]);
    }

    cout << Color::BLUE + "\n=== Enhanced Password Strength Report ===" + Color::RESET << endl;

    int strengthCount[5] = {0};

    ofstream csv("password_report.csv");
    csv << "Password  |  Score  | Entropy  |  Blacklisted  |  Strength\n";
    csv << "---------------------------------------------------------\n";

    for (int i = 0; i < n; i++)
    {
        bool rules[5] = {false};
        bool blacklisted = isBlacklisted(passwords[i]);

        int score = checkStrength(passwords[i], rules);
        double entropy = calculateEntropy(passwords[i]);

        // Count Strength Type
        if (score == 0)
            strengthCount[0]++;
        else if (score == 1)
            strengthCount[1]++;
        else if (score == 2)
            strengthCount[2]++;
        else if (score == 3)
            strengthCount[3]++;
        else
            strengthCount[4]++;

        // CSV log
        csv << passwords[i] << " | " << score << " | " << entropy << " | " << (blacklisted ? "YES" : "NO") << " | " << getStrengthMessage(score) << endl;

        cout << "\nPassword #" << i + 1 << ": " << Color::YELLOW + passwords[i] + Color::RESET << endl;
        cout << "----------------------------------------" << endl;
        cout << "Score Bar   : " << barGraph(score) << endl;
        cout << "Entropy     : " << fixed << setprecision(2) << entropy << " bits\n";
        cout << "Blacklisted : " << (blacklisted ? "YES" : "NO") << endl;
        cout << "Strength    : " << getStrengthMessage(score) << endl;
        cout << "\nSuggestions\n";
        auto sugg = getSuggestions(rules, blacklisted);
        if (sugg.empty())
        {
            cout << Color::GREEN << "Looks good! No improvements needed.\n"
                 << Color::RESET;
        }
        else
        {
            for (auto &s : sugg)
            {
                cout << "- " << s << endl;
            }
        }
        cout << "----------------------------------------" << endl;
    }

    csv.close();

    // Summary Report
    cout << Color::BLUE + "\n=== Summary Report ===" + Color::RESET << endl;
    cout << "Very weak  : " << strengthCount[0] << endl;
    cout << "Weak       : " << strengthCount[1] << endl;
    cout << "Medium     : " << strengthCount[2] << endl;
    cout << "Strong     : " << strengthCount[3] << endl;
    cout << "Very Strong: " << strengthCount[4] << endl;

    cout << "\nCSV exported to: Password_report.csv\n";

    return 0;
}
