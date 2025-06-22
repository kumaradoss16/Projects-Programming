#include <stdio.h>
int main(){
   int n;
   printf("Enter the number of elements do you want to add : ");
   scanf("%d", &n);
   int age[n];
   for(int i=0; i<n; i++){
       printf("Enter number : ");
       scanf("%d", &age[i]);
   }
   int lowest = age[0];
   for(int i=0; i<n; i++){
      if (lowest > age[i]){
          lowest = age[i];
      }
   }
    printf("The lowest age in the array is: %d", lowest);
}
