#include <iostream>
using namespace std;

// Base case function for variadic template
void print() {
    cout << "No more arguments are left" << endl;
}

// Variadic template function
template <typename T, typename... Args>
void print(T first, Args... second) {
    cout << first << endl;      // Print the first argument
    print(second...);           // Recursively call the function with the rest of the arguments
}

int main() {
    // Call the variadic template function with multiple types of arguments
    print(1, 1.25, "Hello", 'K');
    return 0;
}


/* Output:
1
1.25
Hello
K
No more arguments are left
*/
