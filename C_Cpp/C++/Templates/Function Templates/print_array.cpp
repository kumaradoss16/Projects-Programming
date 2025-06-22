#include <iostream>
using namespace std;

template <typename T>
void printarray(T arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

int main() {
    int intarr[] = {1, 2, 3, 4, 5};
    double doublearr[] = {2.3, 4.2, 5.6, 1.2};

    cout << "Integer array: ";
    printarray(intarr, 5);

    cout << "Double array: ";
    printarray(doublearr, 4);
}

/* Output:
Integer array: 1 2 3 4 5
Double array: 2.3 4.2 5.6 1.2
*/
