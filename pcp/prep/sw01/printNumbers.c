#include <stdio.h>

void printNumbersGoTo(int n);
void printNumbersFor(int n);
void printNumbersRecursiveFunction(int n);

int main() {
    int a = 0;
    
    printNumbersGoTo(7);
    printNumbersFor(7);
    printNumbersRecursiveFunction(7);
    
    printf("%s", "= printNumbersRecursiveFunction(7)\n");
    
    return 0;
}

void printNumbersGoTo(int n) {
    int x = 0;
    
    start:
    if (n >= x) {
        printf("%i", x);
        printf("%s", " ");
        x++;
        goto start;
    }
    
    printf("%s", "= printNumbersGoto(7)\n");
}

void printNumbersFor(int n) {
    for (int x = 0; x <= n; x++) {
        printf("%i", x);
        printf("%s", " ");
    }
    
    printf("%s", "= printNumbersFor(7)\n");
}


void printNumbersRecursiveFunction(int n) {
    
    if (n > 0) {
        
        printNumbersRecursiveFunction(n - 1);

    }
    
    printf("%i", n);
    printf("%s", " ");
    
}
