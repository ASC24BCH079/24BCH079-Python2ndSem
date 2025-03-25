def enqueue(queue, value):
    queue.append(value)
    print(value, "added to the queue.")

def dequeue(queue):
    if not queue:
        print("Oops! The queue is empty. Nothing to remove.")
        return None
    value = queue.pop(0)
    print(value, "removed from the queue.")
    return value

def front(queue):
    if not queue:
        print("The queue is empty. No front element.")
        return None
    return queue[0]

def is_empty(queue):
    return len(queue) == 0

def menu():
    queue = []
    
    while True:
        print("\n===== Queue Operations =====")
        print("1. Enqueue a value")
        print("2. Dequeue the front value")
        print("3. Peek at the front value")
        print("4. Check if queue is empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            value = input("Enter value to enqueue: ").strip()
            enqueue(queue, value)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            front_value = front(queue)
            if front_value is not None:
                print("Front element is:", front_value)
        elif choice == '4':
            if is_empty(queue):
                print("The queue is empty.")
            else:
                print("The queue is NOT empty.")
        elif choice == '5':
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
