#include <iostream>
using namespace std;

template <typename T>
int search_array(T arr[], int size, T value) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == value){
            return i;
        }
    } return -1;
}

int main() {
    int intarr[] = {10, 25, 34, 33, 20};
    double doublearr[] = {2.3, 4.5, 6.7, 8.3, 2.1};

    int intvalue = 33;
    double doublevalue = 6.7;

    int intindex = search_array(intarr, 5, intvalue);
    double doubleindex = search_array(doublearr, 5, doublevalue);

    cout << "Index of " << intvalue << " in int array: " << intindex << "\n";
    cout << "Index of " << doublevalue << " in double array: " << doubleindex;
    return 0;
}

/* Output:
Index of 33 in int array: 3
Index of 6.7 in double array: 2
*/
