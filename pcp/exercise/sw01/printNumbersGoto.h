#include <stdio.h>

void printNumbersGoto (int n)
{
    int a = 0;

    start:

    printf(" %d", a);
    if (a <= n) a++;
    
    if (a <= n) goto start;

}