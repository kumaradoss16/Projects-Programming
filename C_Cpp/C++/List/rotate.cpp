#include <iostream>
#include <list>

using namespace std;

void rotateList(list<int> &lst, int n) {
    for (int i = 0; i < n; ++i) {
        lst.push_back(lst.front()); // Move the front element to the back
        lst.pop_front();            // Remove the front element
    }
}

int main() {
    // Create a list of integers
    list<int> myList = {1, 2, 3, 4, 5};

    // Rotate the list by 2 positions
    int n = 2;
    rotateList(myList, n);

    cout << "List after rotating by " << n << " positions: ";
    for (int elem : myList) {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}


/* Output:
List after rotating 2positions: 3 4 5 1 2
*/
