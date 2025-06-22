#include <iostream> // Include the I/O stream library for input and output operations
#include <climits>  // Include the header for limits of integral data types, e.g., INT_MIN

using namespace std; // Use the standard namespace to avoid prefixing std::

void largest_three_num(int num[], int arr_size) {
    int i, first, second, third; // Declare integer variables for iteration and storing the largest numbers
    
    // Check if the array has fewer than 3 elements
    if (arr_size < 3) {
        printf("Invalid output"); // Print error message if there are not enough elements
        return; // Exit the function early
    }
    
    // Initialize first, second, and third to the smallest integer value
    first = second = third = INT_MIN;
    
    // Loop through the array to find the largest, second largest, and third largest numbers
    for (i = 0; i < arr_size; i++) {
        // Update largest numbers if the current number is larger than the current largest
        if (num[i] > first) {
            third = second; // Move second largest to third largest
            second = first; // Move largest to second largest
            first = num[i]; // Update largest to current number
        } else if (num[i] > second && num[i] != first) {
            third = second; // Move second largest to third largest
            second = num[i]; // Update second largest to current number
        } else if (num[i] > third && num[i] != second && num[i] != first) {
            third = num[i]; // Update third largest to current number
        }
    }
    
    // Print the largest three numbers
    cout << "First largest number = " << first << "\n";
    cout << "Second largest number = " << second << "\n";
    cout << "Third largest number = " << third << "\n"; // Fixed typo: "Thrid" to "Third"
}

int main() {
    int n; // Declare an integer variable for the number of elements
    
    // Prompt the user to enter the number of elements in the array
    cout << "Enter the number of elements stored in the array = ";
    cin >> n; // Read the number of elements from the user
    
    // Declare an array to hold the elements. Note: Variable length arrays are allowed in some compilers but are not standard C++
    int num[n]; 
    
    // Loop to read 'n' elements from the user
    for (int i = 0; i < n; i++) {
        cout << "Enter the element = "; // Prompt the user to enter an element
        cin >> num[i]; // Read the element and store it in the array
    }
    
    // Call the function to find and print the largest three numbers
    largest_three_num(num, n);
    
    return 0; // Return 0 to indicate successful execution
}


/* Output:
Enter the number of elements stored in the array = 5
Enter the element = 4
Enter the element = 6
Enter the element = 1
Enter the element = 2
Enter the element = 8
First largest number = 8
Second largest number = 6
Thrid largest number = 4
*/
