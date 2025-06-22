#include <stdio.h>
#include <stdlib.h>

struct list {
    int *data;     // Pointer to the memory where the list items are stored
    int numitems;  // Number of items currently in the list
    int size;      // Capacity of the allocated memory
};

// Function to add an item to the list
void addtolist(struct list *mylist, int item){
    // Check if the list needs resizing
    if(mylist->numitems == mylist->size){
        // Increase capacity by 10;
        mylist->size += 10;
        // Resize the memory to fit the new capacity
        mylist->data = realloc(mylist->data, mylist->size * sizeof(int));
        if (mylist->data == NULL){
            // Handle memory allocation failure
            printf("Memory allocation failed");
            return 1; // Exit the program with an error code
        }
    }

    // Add the item to the end of the list
    mylist->data[mylist->numitems] = item;
    mylist->numitems++;  // Update the number of items
}

int main(){
    struct list mylist;
    int amount;

    // Initialize the list
    mylist.numitems = 0;
    mylist.size = 10;
    mylist.data = malloc(mylist.size * sizeof(int));

    // Check for successful memory allocation
    if (mylist.data == NULL){
        printf("Memory allocation failed");
        return 1;
    }

    // Add items to the list
    amount = 15;
    for (int i = 0; i < amount; i++){
        addtolist(&mylist, i+1);
    }

    // Display the contents of the list
    printf("Data = ");
    for(int j = 0; j < mylist.numitems; j++){
        printf("%d ", mylist.data[j]);
    }
    printf("\n");

    // Free the memory
    free(mylist.data);
    mylist.data = NULL;
    return 0;
}


/* Output:
Data = 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
*/
