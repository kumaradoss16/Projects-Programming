#include <iostream>
using namespace std;

template <typename T1, typename T2, typename T3>
class Container {
private:
    T1 data1;
    T2 data2;
    T3 data3;
public:
    Container(T1 x, T2 y, T3 z) : data1(x), data2(y), data3(z) {}

    void display() {
        cout << "a: " << data1 << " b: " << data2 << " c: " << data3 << "\n";
    }
};

int main() {
    Container<int, char, double> obj1(2, 'K', 2.1);
    obj1.display();

    Container<string, bool, int> obj2("Hello", true, 5);
    obj2.display();

    return 0;
}


/* Output:
a: 2 b: K c: 2.1
a: Hello b: 1 c: 5
*/
