#include <iostream>   // Include the iostream library for input/output operations
using namespace std;   // Use the standard namespace to avoid prefixing 'std::'

// Define a template class Storage for general types
template <typename T>
class Storage {
private:
    T value;    // A member variable to store a value of type T
public:
    // Constructor that initializes the value
    Storage(T v) : value(v) {}

    // Function to print the stored value
    void print() const {
        cout << value << "\n";  // Output the stored value followed by a new line
    }
};

// Template specialization for pointer types (T*)
template <typename T>
class Storage<T*> {
private:
    T* value;   // A pointer to store an address of type T
public:
    // Constructor that initializes the pointer value
    Storage(T* v) : value(v) {}

    // Function to print the value pointed to by the pointer
    void print() {
        cout << *value;  // Dereference the pointer and print the value it points to
    }
};

// Main function to test the template and its specialization
int main() {
    int x = 100;   // An integer variable
    Storage<int> obj1(123);  // Create a Storage object for an int value
    obj1.print();   // Call the print function, prints: 123

    Storage<int*> obj2(&x);  // Create a Storage object for an int pointer
    obj2.print();   // Call the print function, prints: 100

    return 0;  // Return 0 to indicate successful execution
}


/* Output:
Stored value = 123
Stored Pointer value = 100
*/
