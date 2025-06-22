#include <stdio.h>
int main(){
   int n, avg, sum = 0;
   printf("Enter the number of elements do you want to add : ");
   scanf("%d", &n);
   int age[n];
   for(int i=0; i<n; i++){
       printf("Enter number : ");
       scanf("%d", &age[i]);
   }
   for(int i=0; i<n; i++){
       sum += age[i];
   }
   avg = sum / length;
   printf("%d", avg);
}
