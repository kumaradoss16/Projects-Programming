// Include the standard input-output header file
#include <stdio.h>

int main() {
    // Declare variables to store the number of rows and columns
    int row, col;

    // Prompt the user to enter the number of rows
    printf("Number of row : ");
    // Read the number of rows from the user input
    scanf("%d", &row);

    // Prompt the user to enter the number of columns
    printf("Number of column : ");
    // Read the number of columns from the user input
    scanf("%d", &col);

    // Declare a 2D array (matrix) with the specified number of rows and columns
    int matrix[row][col];

    // Loop through each row of the matrix
    for(int i = 0; i < row; i++) {
        // Loop through each column of the current row
        for(int j = 0; j < col; j++) {
            // Prompt the user to enter a number for the current element
            printf("Enter the number [%d][%d] :", i, j);
            // Read the number from user input and store it in the matrix
            scanf("%d", &matrix[i][j]);
        }
    }

    // Print a header for the matrix
    printf("The matrix: \n");

    // Loop through each row of the matrix to print it
    for(int i = 0; i < row; i++) {
        // Loop through each column of the current row
        for(int j = 0; j < col; j++) {
            // Print the current element of the matrix followed by a tab character for spacing
            printf("%d\t", matrix[i][j]);
        }
        // Print a newline after each row to separate rows in the output
        printf("\n\n");
    }

    // End of the main function
    return 0;
}


/*
output:
Number of row : 2
Number of column : 3
Enter the number [0][0] :1
Enter the number [0][1] :2
Enter the number [0][2] :3
Enter the number [1][0] :4
Enter the number [1][1] :5
Enter the number [1][2] :6
The matrix: 
1       2       3

4       5       6
*/
