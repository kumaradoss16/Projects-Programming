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
    
    // Print all elements of the array
    printf("Elements in array: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]); // Print each element followed by a space
    }
    printf("\n"); // Print a newline for better readability

    // Initialize a variable to hold the sum of elements
    int sum = 0;

    // Calculate the sum of all elements in the array
    printf("Sum of all elements in the array = ");
    for(int i = 0; i < n; i++) {
        sum += arr[i]; // Add each element to 'sum'
    }

    // Print the sum
    printf("%d", sum);
    
    return 0; // Indicate that the program executed successfully
}


/* Output:
Enter the number of elements to store in the array : 4
Enter the number: 1
Enter the number: 2
Enter the number: 3
Enter the number: 4
Elements in array: 1 2 3 4 
Sum of all elements in the array = 10
*/
