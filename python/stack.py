class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)
    
if __name__ == "__main__":
    stack = Stack()
    
    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Stack: {stack.items}")  # [10, 20, 30]
    print(f"Top item: {stack.peek()}")  # 30

    # Pop items and show stack state
    print(f"Popped: {stack.pop()}")  # 30
    print(f"Popped: {stack.pop()}")  # 20
    print(f"Stack after popping: {stack.items}")  # [10]

    print(f"Top item: {stack.peek()}")  # 10
    print(f"Popped: {stack.pop()}")  # 10
    print(f"Popped: {stack.pop()}")  # "Stack is empty"
    print(f"Is stack empty? {stack.is_empty()}")  # True