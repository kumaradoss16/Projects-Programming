#include <stdio.h>
#include <limits.h>  // Include the header for INT_MIN and other integer limits

int main()
{
    int n;  // Variable to store the number of elements in the array
    printf("Enter the number of elements to store in the array : ");
    scanf("%d", &n);  // Read the number of elements from the user

    int arr[n];  // Declare an array of size 'n' (Variable Length Array)
    
    // Loop to read 'n' elements into the array
    for(int i = 0; i < n; i++){
        printf("Enter the number: ");
        scanf("%d", &arr[i]);  // Read each element and store it in the array
    }
    
    // Print the elements in the array
    printf("Elements in array: ");
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);  // Print each element followed by a space
    }
    printf("\n\n");  // Print a newline for better readability

    int max1, max2;  // Variables to store the largest and second largest elements
    max1 = max2 = INT_MIN;  // Initialize max1 and max2 to INT_MIN (the smallest integer value)

    // Loop to find the largest and second largest elements
    for(int i = 0; i < n; i++){
        if(arr[i] > max1){
            max2 = max1;  // Update second largest to previous largest
            max1 = arr[i];  // Update largest to the current element
        }
        else if(arr[i] > max2 && arr[i] < max1){
            max2 = arr[i];  // Update second largest if current element is between max1 and max2
        }
    }

    // Print the largest and second largest elements
    printf("First largest element = %d\n", max1);
    printf("Second largest element = %d", max2);

    return 0;  // Return 0 to indicate successful completion
}


/* Output:
Enter the number of elements to store in the array : 5
Enter the number: 4
Enter the number: 1
Enter the number: 3
Enter the number: 2
Enter the number: 6
Elements in array: 4 1 3 2 6 

First largest element = 6
Second largest element = 4
*/
