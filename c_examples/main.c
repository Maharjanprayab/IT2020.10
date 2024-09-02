#include <stdio.h>


int main() {
    int *x;
    //int x;
    int y;

    y = 5;
    x = &y;
    *x = 10;
    x++

    printf("x: %d\n", x);
    printf("y: %d\n", y);

    return 0;
}
