/* 
 * The main function, testing our PCP stack implementation.
 * 
 * Author: ruedi.arnold@hslu.ch
 */

#include <stdio.h>
#include <stdlib.h>
#include "stack.c"
#include "stack.h"

/*
 * 
 */
int main(int argc, char** argv) {

    // Teilaufgabe 1
    printf("\n\nTeilaufgabe 1 -----\n\n");
    stack myStack1 = init();
    print(myStack1);
    top(myStack1);
    myStack1 = push(42, myStack1);
    myStack1 = push(77, myStack1);
    myStack1 = push(1, myStack1);
    print(myStack1);
    myStack1 = push(33, myStack1);
    myStack1 = pop(myStack1);
    myStack1 = push(33, myStack1);
    print(myStack1);
    element e = top(myStack1);
    printf("top element is %i\n", e);
    print(myStack1);

   
    // Teilaufgabe 2
    printf("\n\nTeilaufgabe 2 -----\n\n");
    stack myStack2 = init(); 
    printf("size(myStack2) = %i\n", size(myStack2));  // wieso erhalte ich hier print - Stack is empty UND size = -1?
    printf("isEmpty(myStack2) = %i\n", isEmpty(myStack2)); 
    print(myStack2);
    top(myStack2);
    myStack2 = push(42, myStack2);
    myStack2 = push(77, myStack2);
    myStack2 = push(1, myStack2);
    printf("size(myStack2) = %i\n", size(myStack2)); 
    printf("isEmpty(myStack2) = %i\n", isEmpty(myStack2)); 
    print(myStack2);

    return (EXIT_SUCCESS);
}