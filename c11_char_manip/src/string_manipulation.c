#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "string_manipulation.h"

void reverse_string(char *str) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }
}

void bitshift_string(char *str, int shift) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = str[i] << shift;
    }
}

void to_lower_string(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(str[i]);
    }
}

void to_upper_string(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = toupper(str[i]);
    }
}

void caesar_cipher(char *str, int shift) {
    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i];
        if (ch >= 'a' && ch <= 'z') {
            ch = (ch - 'a' + shift) % 26 + 'a';
        } else if (ch >= 'A' && ch <= 'Z') {
            ch = (ch - 'A' + shift) % 26 + 'A';
        }
        str[i] = ch;
    }
}
