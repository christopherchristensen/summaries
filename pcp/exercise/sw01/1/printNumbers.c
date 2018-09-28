#include "printNumbersGoto.h"
#include "printNumbersFor.h"
#include "printNumbersRecursiveFunction.h"

int main(int argc, char const *argv[])
{
    printf("\n");
    printNumbersGoto(7);
    printf(" = printNumbersGoto(7)\n");
    printNumbersFor(7);
    printf(" = printNumbersFor(7)\n");
    printNumbersRecursiveFunction(7);
    printf(" = printNumbersRecursiveFunction(7)\n\n");
    return 0;
}
