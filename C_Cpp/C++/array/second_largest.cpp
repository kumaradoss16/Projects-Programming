#include <iostream>  // Include the I/O stream library for input and output operations
#include <climits>   // Include the header for limits of integral data types, e.g., INT_MIN

using namespace std;  // Use the standard namespace to avoid prefixing std::

void second_largest(int arr[], int arr_size) {
    int i, first, second;  // Declare integer variables for iteration and storing the largest numbers

    // Check if the array has fewer than 2 elements
    if (arr_size < 2) {
        cout << "Invalid input";  // Print an error message if there are not enough elements
        return;  // Exit the function early
    }

    // Initialize first and second to the smallest integer value
    first = second = INT_MIN;

    // Loop through the array to find the largest and second largest numbers
    for (i = 0; i < arr_size; i++) {
        // Update largest and second largest numbers if the current number is larger
        if (arr[i] > first) {
            second = first;  // Move the current largest to second largest
            first = arr[i];  // Update largest to the current number
        } else if (arr[i] > second && arr[i] != first) {
            second = arr[i];  // Update second largest to the current number if it is not equal to the largest number
        }
    }

    // Print the second largest number
    cout << "Second largest number = " << second << endl;
}

int main() {
    int arr_size;  // Declare an integer variable for the number of elements

    // Prompt the user to enter the number of elements in the array
    cout << "Enter the number of elements = ";
    cin >> arr_size;  // Read the number of elements from the user

    // Declare an array to hold the elements. Note: Variable length arrays are allowed in some compilers but are not standard C++
    int arr[arr_size];  

    // Loop to read 'arr_size' elements from the user
    for (int i = 0; i < arr_size; i++) {
        cout << "Enter the element = ";  // Prompt the user to enter an element
        cin >> arr[i];  // Read the element and store it in the array
    }

    // Call the function to find and print the second largest number
    second_largest(arr, arr_size);

    return 0;  // Return 0 to indicate successful execution
}


/* Output:
Enter the number of elements = 5
Enter the element = 3
Enter the element = 5
Enter the element = 1
Enter the element = 7
Enter the element = 9
Second largest number = 7
*/
