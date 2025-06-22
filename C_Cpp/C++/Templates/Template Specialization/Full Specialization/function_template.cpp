#include <iostream>
using namespace std;

template <typename T>
T getmax(T a, T b) {
    return (a > b) ? a : b;
}

// Full specialization for char
template <>
char getmax(char a, char b) {
    cout << "Specified template for char\n";
    return (a > b) ? a : b;
}

int main() {
    cout << "Max of 3 and 7: " << getmax(3, 7) << "\n";          // Uses generic template
    cout << "Max of 3.4 and 2.3: " << getmax(3.4, 2.3) << "\n";  // Uses generic template
    cout << "Max of f and h: " << getmax('f', 'h');              // Uses specialized template

    return 0;
}


/* Output:
Max of 3 and 7: 7
Max of 3.4 and 2.3: 3.4
Specified template for char
Max of f and h: h
*/
