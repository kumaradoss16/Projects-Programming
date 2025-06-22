#include <stdio.h>

void odd_or_even(int n);

void odd_or_even(int n){
    if (n % 2 == 0){
        printf("The entered number is even");
    }else{
        printf("The entered number is odd");
    }
}

int main(){
    int num;
    printf("Enter the number= ");
    scanf("%d", &num);
    odd_or_even(num);
    return 0;
}


/* Output:
Enter the number= 4
The entered number is even
*/
