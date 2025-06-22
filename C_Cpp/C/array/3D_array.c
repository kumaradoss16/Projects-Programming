#include <stdio.h>  // Includes the standard input/output library for printf and scanf functions.

int main() {  // Entry point of the program. The execution starts here.
    int layers, rows, columns;  // Declares three integer variables to store the dimensions of the 3D array.
    
    printf("Enter the number of layers = ");  // Prompts the user to enter the number of layers.
    scanf("%d", &layers);  // Reads the user input for the number of layers and stores it in the 'layers' variable.
    
    printf("Enter the number of rows = ");  // Prompts the user to enter the number of rows.
    scanf("%d", &rows);  // Reads the user input for the number of rows and stores it in the 'rows' variable.
    
    printf("Enter the number of columns = ");  // Prompts the user to enter the number of columns.
    scanf("%d", &columns);  // Reads the user input for the number of columns and stores it in the 'columns' variable.
    printf("-------------------------------------------------\n");
    
    int array[layers][rows][columns];  // Declares a 3D array with dimensions specified by the user.

    // Nested loop to input values into the 3D array.
    for(int i = 0; i < layers; i++) {  // Loops over each layer.
        printf("Enter the numbers for Layer '%d' (default Layer %d)\n", i+1);  // Prompts the user for the current layer number (1-based index).
        for(int j = 0; j < rows; j++) {  // Loops over each row in the current layer.
            for(int k = 0; k < columns; k++) {  // Loops over each column in the current row.
                printf("Enter the number [%d][%d][%d] = ", i, j, k);  // Prompts the user to enter a value for the current position.
                scanf("%d", &array[i][j][k]);  // Reads the user input and stores it in the 3D array at the specified position.
            }
        }
      printf("\n");
    }
    printf("-------------------------------------------------\n");

    // Nested loop to print the values from the 3D array.
    for(int i = 0; i < layers; i++) {  // Loops over each layer.
        printf("Layer %d:\n", i);  // Prints the current layer number (0-based index).
        for(int j = 0; j < rows; j++) {  // Loops over each row in the current layer.
            for(int k = 0; k < columns; k++) {  // Loops over each column in the current row.
                printf("%4d\t", array[i][j][k]);  // Prints the value at the current position with a width of 4 characters, followed by a tab.
            }
            printf("\n\n");  // Adds extra new lines to separate rows visually.
        }
        printf("\n");  // Adds an extra new line to separate layers visually.
    }

    return 0;  // Exits the program with a status code of 0, indicating successful completion.
}



/* Output:

Enter the number of layers = 3
Enter the number of rows = 3
Enter the number of columns = 3
-------------------------------------------------
Enter the numbers for Layer '1'(default Layer 0)
Enter the number [0][0][0] = 1
Enter the number [0][0][1] = 2
Enter the number [0][0][2] = 3
Enter the number [0][1][0] = 4
Enter the number [0][1][1] = 5
Enter the number [0][1][2] = 6
Enter the number [0][2][0] = 7
Enter the number [0][2][1] = 8
Enter the number [0][2][2] = 9

Enter the numbers for Layer '2'(default Layer 1)
Enter the number [1][0][0] = 10
Enter the number [1][0][1] = 11
Enter the number [1][0][2] = 12
Enter the number [1][1][0] = 13
Enter the number [1][1][1] = 14
Enter the number [1][1][2] = 15
Enter the number [1][2][0] = 16
Enter the number [1][2][1] = 17
Enter the number [1][2][2] = 18

Enter the numbers for Layer '3'(default Layer 2)
Enter the number [2][0][0] = 19
Enter the number [2][0][1] = 20
Enter the number [2][0][2] = 21
Enter the number [2][1][0] = 22
Enter the number [2][1][1] = 23
Enter the number [2][1][2] = 24
Enter the number [2][2][0] = 25
Enter the number [2][2][1] = 26
Enter the number [2][2][2] = 27

-------------------------------------------------
Layer 1:
   1       2       3

   4       5       6

   7       8       9


Layer 2:
  10      11      12

  13      14      15

  16      17      18


Layer 3:
  19      20      21

  22      23      24

  25      26      27

*/
