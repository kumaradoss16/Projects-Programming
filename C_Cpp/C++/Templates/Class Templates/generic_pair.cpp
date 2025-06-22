#include <iostream>
using namespace std;

template <typename T1, typename T2>
class Pair {
private:
    T1 first;
    T2 second;
public:
    Pair(T1 f, T2 s) : first(f), second(s) {}

    T1 getfirst() const {
        return first;
    }

    void setfirst(T1 f) {
        first = f;
    }

    T2 getsecond() const {
        return second;
    }

    void setsecond(T2 s) {
        second = s;
    }

    void display() const {
        cout << "First: " << first << " Second: " << second << "\n";
    }
};

int main() {
    Pair<int, char> intcharPair(2, 'K');
    intcharPair.display();

    Pair<double, string> doublestringPair(3.4, "Kumar");
    doublestringPair.display();

    intcharPair.setfirst(200);
    intcharPair.setsecond('M');
    intcharPair.display();

    return 0;
}


/* Output:
First: 2 Second: K
First: 3.4 Second: Kumar
First: 200 Second: M
*/
