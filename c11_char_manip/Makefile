CC = gcc
CFLAGS = -Wall -std=c11
TARGET = string_manipulation

all: $(TARGET)

$(TARGET): src/main.c src/string_manipulation.c
	$(CC) $(CFLAGS) -o build/$(TARGET) src/main.c src/string_manipulation.c

test: $(TARGET)
	./build/$(TARGET)

clean:
	rm -f build/$(TARGET)

.PHONY: all clean test
