class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1

    def push(self, x):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = x
        print(f"Pushed {x} into the stack") 

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped_element = self.stack[self.top]
        self.top -= 1
        return popped_element

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            return None

# Example usage
if __name__ == "__main__":
    stack = Stack(3)

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Top element is {stack.peek()}")

    print(f"Popped element is {stack.pop()}")
    print(f"Top element is {stack.peek()}")

    stack.pop()
    stack.pop()

    if stack.is_empty():
        print("The stack is empty")
    else:
        print("The stack is not empty")
