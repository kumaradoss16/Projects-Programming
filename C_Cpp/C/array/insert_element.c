#include <stdio.h>

int main()
{
    int size;  // Variable to store the number of elements in the array
    printf("Enter the number of elements to store in the array : ");
    scanf("%d", &size);  // Read the number of elements from the user
    
    int arr[size];  // Declare an array of size 'size'

    // Loop to read 'size' elements into the array
    for(int i = 0; i < size; i++){
        printf("Enter the number: ");
        scanf("%d", &arr[i]);  // Read each element and store it in the array
    }
    
    printf("\n");
    // Print the elements of the array
    printf("Elements in the array: ");
    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);  // Print each element followed by a space
    }
    printf("\n");

    int new, pos;  // Variables for new element and its position
    printf("Enter element to insert = ");
    scanf("%d", &new);  // Read the new element to be inserted
    printf("Enter the element's position = ");
    scanf("%d", &pos);  // Read the position where the new element should be inserted

    // Validate the position
    if(pos > size + 1 || pos <= 0){
        printf("Invalid position! Please enter the position between 1 to %d", size);
    }
    else {
        // Shift elements to the right to make room for the new element
        for(int i = size; i >= pos; i--){
            arr[i] = arr[i - 1];
        }
        
        // Insert the new element at the specified position
        arr[pos - 1] = new;  
        size++;  // Increment the size of the array
    }

    // Print the elements of the array after insertion
    printf("Elements in the array after insertion: ");
    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);  // Print each element followed by a space
    }

    return 0;  // Return 0 to indicate successful completion
}



/* Output:
Enter the number of elements to store in the array : 5
Enter the number: 2
Enter the number: 4
Enter the number: 6
Enter the number: 8
Enter the number: 10

Elements in the array: 2 4 6 8 10 
Enter element to insert = 5
Enter the element's position = 3
Elemtns in the array after insertion: 2 4 5 6 8 10 
  */
