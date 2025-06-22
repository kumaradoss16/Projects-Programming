#include <iostream>
using namespace std;

template <typename T>
T sum(T a, T b) {
    return a + b;
}

int main() {
    cout << "Sum of 5 and 10: " << sum(5, 10) << endl;           // work with int
    cout << "Sum of 1.5 and 2.5: " << sum(1.5, 2.5) << endl;     // work with double

    return 0;
}


/* Output:
Sum of 5 and 10: 15
Sum of 1.5 and 2.5: 4
*/
