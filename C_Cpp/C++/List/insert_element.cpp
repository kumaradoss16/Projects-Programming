#include <iostream>
#include <list>

using namespace std;

int main() {
    // Create a list of integers
    list<int> myList = {10, 20, 30, 40, 50};

    // Create an iterator pointing to the 3rd position
    auto it = myList.begin();
    advance(it, 2); // Move the iterator to the 3rd position (0-based index)

    // Insert 25 at the 3rd position
    myList.insert(it, 25);

    cout << "List after inserting 25 at the 3rd position: ";
    for (int elem : myList) {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}


/* Output:
List after inserting 25 at a 3rd position: 10 20 25 30 40 50 
*/
