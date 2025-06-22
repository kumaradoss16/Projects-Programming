#include <stdio.h> // Include the standard input/output library

int main() {
    int n; // Declare an integer variable to hold the number of elements

    // Prompt the user to enter the number of elements
    printf("Enter the number of elements to store in the array : ");
    scanf("%d", &n); // Read the number of elements from the user

    // Declare an array of size 'n'
    int arr[n]; 

    // Loop to get 'n' integers from the user and store them in the array
    for(int i = 0; i < n; i++) {
        printf("Enter the number: ");
        scanf("%d", &arr[i]); // Read each integer from the user and store it in the array
    }
    
    // Print a header for the negative numbers output
    printf("Print negative elements in array: \n");

    // Loop to check each element in the array
    for(int i = 0; i < n; i++) {
        // If the current element is negative
        if(arr[i] < 0) {
            // Print the negative number
            printf("%d\n", arr[i]);
        }
    }

    return 0; // Indicate that the program executed successfully
}

/* Output:
Enter the number of elements to store in the array : 5
Enter the number: 1
Enter the number: -2
Enter the number: 3
Enter the number: -4
Enter the number: 5
Print negative elements in array: 
-2
-4
*/
