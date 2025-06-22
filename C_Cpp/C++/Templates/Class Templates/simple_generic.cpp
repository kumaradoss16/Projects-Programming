#include <iostream>
using namespace std;

template <typename T>
class Box {
private:
    T value;
public:
    Box(T value) : value(value) {}
    void setvalue(T value) {
        // this->value = value; is used within a class method
        // to distinguish between a member variable (value) and 
        // a method parameter with the same name (value)
        this->value = value;
    }

    T getvalue() const {
        return value;
    }

    void display() const {
        cout << value << "\n";
    }
};

int main() {
    Box<int> intBox(43);
    intBox.display();

    Box<double> doubleBox(3.4);
    doubleBox.display();

    Box<string> stringBox("Hello, World");
    stringBox.display();

    return 0;
}


/* Output:
43
3.4
Hello, World
*/
