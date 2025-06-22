#include <iostream>
#include <stack>
#include <string>  // Include string for std::string
using namespace std;

int main() {
    stack<string> cars;  // Use stack<string> for string values

    cars.push("Volvo");
    cars.push("BMW");
    cars.push("Ford");
    cars.push("Mazda");

    // Printing the elements in the stack (LIFO order)
    // cars.empty() returns true if the stack has no elements, and false otherwise. 
    // The ! operator negates this result.
    cout << "Stack: " << endl;
    while (!cars.empty()) {
        cout << cars.top() << endl;  // Display the top element
        // After calling pop(), the stack's top element becomes the next one below the removed element.
        cars.pop();  // Remove the top element
    }

    return 0;
}


/* Output
Stack: 
Mazda
Ford
BMW
Volvo
*/
//
