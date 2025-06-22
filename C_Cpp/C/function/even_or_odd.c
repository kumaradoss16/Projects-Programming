#include <stdio.h>

// Function prototype
int even_or_odd(int n);

int even_or_odd(int n) {
    // Returns 0 if n is even, 1 if n is odd
    return n % 2;
}

int main() {
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    int result = even_or_odd(num);
    if(result == 0) {
        printf("The entered number is even");
    } else {
        printf("The entered number is odd");
    }
    return 0;
}


/* Output;
Enter the number: 5
The entered number is odd
*/
