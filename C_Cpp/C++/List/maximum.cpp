#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

int main() {
    // Create a list of integers
    list<int> mylist = {2, 5, 1, 6, 8, 4};

    // Find the maximum element
    auto maxelem = max_element(mylist.begin(), mylist.end());

    if (maxelem != mylist.end()) {
        cout << "Maximum element in the list: " << *maxelem;
    } else {
        cout << "List is empty";
    }
    return 0;
}


/* Output:
Maximum element in the list: 8
*/
