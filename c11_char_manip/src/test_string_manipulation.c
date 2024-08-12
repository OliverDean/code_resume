#include <stdio.h>
#include <string.h>
#include "string_manipulation.h"

void test_reverse_string() {
    char str[] = "hello";
    reverse_string(str);
    if (strcmp(str, "olleh") == 0) {
        printf("Reverse string test passed.\n");
    } else {
        printf("Reverse string test failed.\n");
    }
}

void test_bitshift_string() {
    char str[] = "abc";
    bitshift_string(str, 1);
    // Expecting ASCII values to shift
    printf("Bitshift string output: %s\n", str); 
}

void run_tests() {
    test_reverse_string();
    test_bitshift_string();
    // Add more tests here
}

int main() {
    run_tests();
    return 0;
}
