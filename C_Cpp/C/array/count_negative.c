#include <stdio.h>
#include <limits.h>  // Include for integer limits, though not used in this specific code

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

    int count_neg = 0;  // Variable to count negative numbers

    // Loop to count negative elements
    for(int i = 0; i < n; i++){
        if(arr[i] < 0){
            count_neg += 1;  // Increment the count if the element is negative
        }
    }

    // Print the count of negative elements
    printf("Total negative elements = %d", count_neg);

    return 0;  // Return 0 to indicate successful completion
}



/* Output:
Enter the number of elements to store in the array : 10
Enter the number: 2
Enter the number: -6
Enter the number: -9
Enter the number: 7
Enter the number: 11
Enter the number: 0
Enter the number: -5
Enter the number: 3
Enter the number: 4
Enter the number: 5
Elements in array: 2 -6 -9 7 11 0 -5 3 4 5 

Total negative elements = 3
*/
