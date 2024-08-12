#include <stdio.h>
#include <string.h>
#include "string_manipulation.h"

int main() {
    char input[100];
    char temp[100];
    int shift_value = 4;

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; // Remove newline character

    // Reverse the string
    strcpy(temp, input);  // Copy original string to temp
    reverse_string(temp);
    printf("Reversed: %s\n", temp);

    // Bitshift the string
    strcpy(temp, input);  // Copy original string to temp
    bitshift_string(temp, 1);
    printf("Bitshifted: %s\n", temp);

    // Convert to lowercase
    strcpy(temp, input);  // Copy original string to temp
    to_lower_string(temp);
    printf("Lowercase: %s\n", temp);

    // Convert to uppercase
    strcpy(temp, input);  // Copy original string to temp
    to_upper_string(temp);
    printf("Uppercase: %s\n", temp);

    // Apply Caesar Cipher
    strcpy(temp, input);  // Copy original string to temp
    caesar_cipher(temp, shift_value);
    printf("Caesar Cipher (shift %d): %s\n", shift_value, temp);

    return 0;
}
