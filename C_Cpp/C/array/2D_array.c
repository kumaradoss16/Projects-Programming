#include <stdio.h>  // Include the standard input-output header file for printf function

int main() {  // Entry point of the C program
    // Initialize a 2D array (matrix) with fixed values
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Print a header indicating the start of the matrix output
    printf("The Matrix: \n");

    // Loop through each row of the matrix
    for(int i = 0; i < 2; i++) {
        // Loop through each column of the current row
        for(int j = 0; j < 3; j++) {
            // Print the current element of the matrix followed by a tab character
            printf("%d\t", matrix[i][j]);
        }
        // Print two newline characters to separate rows in the output for better readability
        printf("\n\n");
    }

    // End of the main function, return 0 to indicate successful execution
    return 0;
}




/*
Output:
The Matrix: 
1       2       3

4       5       6
   */
