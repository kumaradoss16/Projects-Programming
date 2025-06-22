#include <stdio.h>
#include <limits.h>  // Include for constants like INT_MIN, although it's not used in this code

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

    int even = 0;  // Variable to count even numbers
    int odd = 0;   // Variable to count odd numbers

    // Loop to count even and odd elements
    for(int i = 0; i < n; i++){
        if(arr[i] % 2 == 0){
            even += 1;  // Increment the even count if the element is even
        }
        else{
            odd += 1;  // Increment the odd count if the element is odd
        }
    }

    // Print the counts of even and odd elements
    printf("Total even elements = %d\n", even);
    printf("Total odd elements = %d", odd);

    return 0;  // Return 0 to indicate successful completion
}



/* Output:
Enter the number of elements to store in the array : 6
Enter the number: 2
Enter the number: 3
Enter the number: 4
Enter the number: 5
Enter the number: 1
Enter the number: 8
Elements in array: 2 3 4 5 1 8 

Total even elements = 3
Total odd elements = 3
*/
