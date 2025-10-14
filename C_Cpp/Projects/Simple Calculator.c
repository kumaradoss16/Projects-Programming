/*
===============================================================================
                        SIMPLE CALCULATOR - CLI VERSION
===============================================================================
Description: A beginner-friendly calculator program in C with menu interface
Author: C Programming Tutorial
Features: Addition, Subtraction, Multiplication, Division, Modulus
Compilation: gcc -Wall -Wextra -std=c99 -o calculator calculator.c
===============================================================================
*/

#include <stdio.h>
#include <stdlib.h>

/* ===============================================================================
                                FUNCTION PROTOTYPES
=============================================================================== */

// Mathematical operation functions
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
int modulus(int a, int b);

// Utility functions
void displayMenu(void);
void clearInputBuffer(void);
int getValidChoice(void);
double getValidNumber(const char *prompt);
void displayResult(double result, const char *operation);
void pressEnterToContinue(void);

/* ===============================================================================
                                    MAIN FUNCTION
=============================================================================== */

int main(void)
{
    int choice;
    double num1, num2, result;

    printf("\n");
    printf("===============================================================================\n");
    printf("                    WELCOME TO SIMPLE CALCULATOR v1.0\n");
    printf("===============================================================================\n");
    printf("This calculator performs basic mathematical operations.\n");
    printf("Follow the menu prompts to perform calculations.\n");

    // Main program loop - continues until user chooses to exit
    do
    {
        displayMenu();
        choice = getValidChoice();

        // Handle exit option
        if (choice == 6)
        {
            printf("\n");
            printf("===============================================================================\n");
            printf("                    THANK YOU FOR USING THE CALCULATOR!\n");
            printf("===============================================================================\n");
            break;
        }

        // Get input numbers for calculation
        printf("\n");
        num1 = getValidNumber("Enter first number: ");
        num2 = getValidNumber("Enter second number: ");

        printf("\n");
        printf("===============================================================================\n");

        // Perform calculation based on user choice
        switch (choice)
        {
        case 1: // Addition
            result = add(num1, num2);
            displayResult(result, "Addition");
            printf("%.2f + %.2f = %.2f\n", num1, num2, result);
            break;

        case 2: // Subtraction
            result = subtract(num1, num2);
            displayResult(result, "Subtraction");
            printf("%.2f - %.2f = %.2f\n", num1, num2, result);
            break;

        case 3: // Multiplication
            result = multiply(num1, num2);
            displayResult(result, "Multiplication");
            printf("%.2f × %.2f = %.2f\n", num1, num2, result);
            break;

        case 4: // Division
            if (num2 == 0)
            {
                printf("                              ERROR: DIVISION BY ZERO\n");
                printf("===============================================================================\n");
                printf("❌ Cannot divide by zero! Please try again with a non-zero divisor.\n");
            }
            else
            {
                result = divide(num1, num2);
                displayResult(result, "Division");
                printf("%.2f ÷ %.2f = %.2f\n", num1, num2, result);
            }
            break;

        case 5: // Modulus
            // Modulus only works with integers
            if (num2 == 0)
            {
                printf("                              ERROR: MODULUS BY ZERO\n");
                printf("===============================================================================\n");
                printf("❌ Cannot perform modulus by zero! Please try again.\n");
            }
            else
            {
                int intNum1 = (int)num1;
                int intNum2 = (int)num2;
                int modResult = modulus(intNum1, intNum2);
                printf("                               MODULUS RESULT\n");
                printf("===============================================================================\n");
                printf("✓ %d %% %d = %d\n", intNum1, intNum2, modResult);
            }
            break;

        default:
            printf("                                 INVALID CHOICE\n");
            printf("===============================================================================\n");
            printf("❌ Please select a valid option (1-6).\n");
        }

        pressEnterToContinue();

    } while (choice != 6);

    return 0;
}

/* ===============================================================================
                            MATHEMATICAL OPERATION FUNCTIONS
=============================================================================== */

/**
 * Addition function
 * @param a: First number
 * @param b: Second number
 * @return: Sum of a and b
 */
double add(double a, double b)
{
    return a + b;
}

/**
 * Subtraction function
 * @param a: First number (minuend)
 * @param b: Second number (subtrahend)
 * @return: Difference of a and b
 */
double subtract(double a, double b)
{
    return a - b;
}

/**
 * Multiplication function
 * @param a: First number
 * @param b: Second number
 * @return: Product of a and b
 */
double multiply(double a, double b)
{
    return a * b;
}

/**
 * Division function
 * @param a: Dividend
 * @param b: Divisor (should not be zero)
 * @return: Quotient of a divided by b
 */
double divide(double a, double b)
{
    return a / b;
}

/**
 * Modulus function (remainder after division)
 * @param a: Dividend (integer)
 * @param b: Divisor (integer, should not be zero)
 * @return: Remainder of a divided by b
 */
int modulus(int a, int b)
{
    return a % b;
}

/* ===============================================================================
                                UTILITY FUNCTIONS
=============================================================================== */

/**
 * Display the main menu options
 */
void displayMenu(void)
{
    printf("\n");
    printf("===============================================================================\n");
    printf("                               CALCULATOR MENU\n");
    printf("===============================================================================\n");
    printf("Choose an operation:\n");
    printf("  1. ➕  Addition       (a + b)\n");
    printf("  2. ➖  Subtraction    (a - b)\n");
    printf("  3. ✖️   Multiplication (a × b)\n");
    printf("  4. ➗  Division       (a ÷ b)\n");
    printf("  5. 📊  Modulus        (a %% b)\n");
    printf("  6. 🚪  Exit Program\n");
    printf("===============================================================================\n");
}

/**
 * Clear input buffer to handle invalid input
 */
void clearInputBuffer(void)
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
    {
        // Clear the input buffer
    }
}

/**
 * Get valid menu choice from user
 * @return: Valid choice (1-6)
 */
int getValidChoice(void)
{
    int choice;

    while (1)
    {
        printf("Enter your choice (1-6): ");

        if (scanf("%d", &choice) == 1)
        {
            clearInputBuffer();
            if (choice >= 1 && choice <= 6)
            {
                return choice;
            }
            else
            {
                printf("❌ Invalid choice! Please enter a number between 1 and 6.\n\n");
            }
        }
        else
        {
            clearInputBuffer();
            printf("❌ Invalid input! Please enter a numeric choice (1-6).\n\n");
        }
    }
}

/**
 * Get valid number from user with custom prompt
 * @param prompt: Message to display to user
 * @return: Valid floating-point number
 */
double getValidNumber(const char *prompt)
{
    double number;

    while (1)
    {
        printf("%s", prompt);

        if (scanf("%lf", &number) == 1)
        {
            clearInputBuffer();
            return number;
        }
        else
        {
            clearInputBuffer();
            printf("❌ Invalid input! Please enter a valid number.\n");
        }
    }
}

/**
 * Display formatted result header
 * @param result: The calculated result
 * @param operation: Name of the operation performed
 */
void displayResult(double result, const char *operation)
{
    printf("                               %s RESULT\n", operation);
    printf("===============================================================================\n");
    printf("✓ ");
}

/**
 * Pause program and wait for user to press Enter
 */
void pressEnterToContinue(void)
{
    printf("\n📝 Press Enter to continue...");
    getchar();
}

/* ===============================================================================
                                END OF PROGRAM
=============================================================================== */
