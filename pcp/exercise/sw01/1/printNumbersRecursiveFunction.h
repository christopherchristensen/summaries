#include <stdio.h>

void printNumbersRecursiveFunction (int n)
{
    if (n > 0) 
    {
        printNumbersRecursiveFunction (n - 1);
    }
    printf(" %d", n);
}
