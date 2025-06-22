#include <stdio.h>
#include <limits.h>  // Include for integer limits, though not used in this specific code

int main()
{
    int n;  // Variable to store the number of elements in the arrays
    printf("Enter the number of elements to store in the array : ");
    scanf("%d", &n);  // Read the number of elements from the user

    int arr1[n], arr2[n];  // Declare two arrays of size 'n'

    // Loop to read 'n' elements into the first array (arr1)
    for(int i = 0; i < n; i++){
        printf("Enter the number: ");
        scanf("%d", &arr1[i]);  // Read each element and store it in arr1
    }

    // Copy elements from arr1 to arr2
    for(int i = 0; i < n; i++){
        arr2[i] = arr1[i];  // Copy each element from arr1 to arr2
    }

    // Print the elements of the first array
    printf("Elements in the array 1: ");
    for(int i = 0; i < n; i++){
        printf("%d ", arr1[i]);  // Print each element of arr1 followed by a space
    }
    printf("\n");  // Print a newline for better readability

    // Print the elements of the second array
    printf("Elements in the array 2: ");
    for(int i = 0; i < n; i++){
        printf("%d ", arr2[i]);  // Print each element of arr2 followed by a space
    }

    return 0;  // Return 0 to indicate successful completion
}



/* Output:
Enter the number of elements to store in the array : 5
Enter the number: 10
Enter the number: 20
Enter the number: 30
Enter the number: 40
Enter the number: 50


Elements in the array 1: 10 20 30 40 50 
Elements in the array 2: 10 20 30 40 50 
  */
