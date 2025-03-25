def push(stack, value):
    stack.append(value)
    print(value, "pushed to stack.")

def pop(stack):
    if not stack:
        print("Oops! The stack is empty. Nothing to pop.")
        return None
    value = stack.pop()
    print(value, "popped from stack.")
    return value

def peek(stack):
    if not stack:
        print("The stack is empty. No top element.")
        return None
    return stack[-1]

def is_empty(stack):
    return len(stack) == 0

def menu():
    stack = []
    
    while True:
        print("\n===== Stack Operations =====")
        print("1. Push a value")
        print("2. Pop the top value")
        print("3. Peek at the top value")
        print("4. Check if stack is empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            value = input("Enter value to push: ").strip()
            push(stack, value)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            top_value = peek(stack)
            if top_value is not None:
                print("Top element is:", top_value)
        elif choice == '4':
            if is_empty(stack):
                print("The stack is empty.")
            else:
                print("The stack is NOT empty.")
        elif choice == '5':
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
