#include <iostream> // Includes the iostream library for input and output operations
using namespace std; // Allows the use of standard library features without prefixing with 'std::'

// Function to separate 0's and 1's in the array
void seperate_ones_zeros(int num[], int size_arr){
    int ctr = 0; // Counter to keep track of the number of 0's
    // Loop through the array to count the number of 0's
    for (int i = 0; i < size_arr; i++){
        if (num[i] == 0){
            ctr++; // Increment counter if the element is 0
        }
    }
    // Fill the beginning of the array with 0's
    for (int i = 0; i < ctr; i++){
        num[i] = 0;
    }

    // Fill the remaining part of the array with 1's
    for (int i = ctr; i < size_arr; i++) {
        num[i] = 1;
    }
}

// Main function where the execution starts
int main(){
    int size_arr; // Variable to store the number of elements in the array
    cout << "Enter the number of elements stored in the array = "; // Prompt for the number of elements
    cin >> size_arr; // Read the number of elements from user input

    int num[size_arr]; // Declare an array of the given size
    // Loop to read array elements from user input
    for (int i = 0; i < size_arr; i++) {
        cout << "Enter the element(0's and 1's) = "; // Prompt for each element
        cin >> num[i]; // Read the element from user input
    }
    
    // Display the original array
    cout << "Original array = ";
    for (int i = 0; i < size_arr; i++) {
        cout << num[i] << " "; // Print each element of the array
    }
    cout << endl; // Print a newline for better formatting

    // Call the function to separate 0's and 1's
    seperate_ones_zeros(num, size_arr);
    
    // Display the array after separation
    cout << "After separation array = ";
    for (int i = 0; i < size_arr; i++){
        cout << num[i] << " "; // Print each element of the array after separation
    }
    cout << "\n"; // Print a newline for better formatting
    return 0; // Return 0 to indicate successful execution
}


/* Output:
Enter the number of elements stored in the array = 8
Enter the element(0's and 1's) = 1
Enter the element(0's and 1's) = 0
Enter the element(0's and 1's) = 0
Enter the element(0's and 1's) = 1
Enter the element(0's and 1's) = 1
Enter the element(0's and 1's) = 1
Enter the element(0's and 1's) = 0
Enter the element(0's and 1's) = 0
Original array = 1 0 0 1 1 1 0 0 After Original array = 0 0 0 0 1 1 1 1
  */
