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
    printf("\n\n"); // Print a newline for better readability

    // Initialize 'max' and 'min' with the first element of the array
    int max = arr[0];
    int min = arr[0];

    // Find the maximum and minimum values in the array
    for(int i = 0; i < n; i++) {
        if(arr[i] > max) {
            max = arr[i]; // Update 'max' if the current element is greater
        }
        if(arr[i] < min) {
            min = arr[i]; // Update 'min' if the current element is smaller
        }
    }

    // Print the maximum and minimum values
    printf("Maximum element = %d\n", max);
    printf("Minimum element = %d", min);

    return 0; // Indicate that the program executed successfully
}


/* Output:
Enter the number of elements to store in the array : 5 
Enter the number: 2
Enter the number: 4
Enter the number: 1
Enter the number: 5
Enter the number: 7
Elements in array: 2 4 1 5 7 

Maximum element = 7
Minimum element = 1
  */
