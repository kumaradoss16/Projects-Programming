#include <iostream> // Include the input-output stream library for cin and cout
using namespace std; // Use the standard namespace to avoid prefixing std::

int main() {
    int n; // Declare an integer variable to store the number of elements
    
    // Prompt the user to enter the number of elements
    cout << "Enter the number of elements stored in the array = ";
    cin >> n; // Read the number of elements from the user
    
    // Declare an array of size 'n' to store the elements
    int num[n]; 
    
    // Loop to read 'n' elements from the user
    for (int i = 0; i < n; i++) {
        // Prompt the user to enter an element
        cout << "Enter element " << i + 1 << " = ";
        cin >> num[i]; // Read the element from the user and store it in the array
    }
    
    // Initialize max_num with the first element of the array
    int max_num = num[0];
    
    // Loop to find the maximum element in the array
    for (int i = 0; i < n; i++) {
        // Check if the current element is greater than the current maximum
        if (num[i] > max_num) {
            max_num = num[i]; // Update max_num if the current element is greater
        }
    }
    
    // Print the maximum element in the array
    cout << "Maximum element in the array : " << max_num << endl;
    
    return 0; // Return 0 to indicate successful execution
}


/* Output:
Enter the number of element stored in the array = 5
Enter the element = 7
Enter the element = 4
Enter the element = 8
Enter the element = 3
Enter the element = 1
Maximum element in the array : 8
  */
