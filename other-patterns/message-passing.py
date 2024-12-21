import threading
import queue

def message_handler(q):
    while True:
        message = q.get()  # Block until a message is received
        if message == "exit":
            break
        print(f"Received message: {message}")

def sender(q, message):
    q.put(message)

def main():
    q = queue.Queue()
    thread = threading.Thread(target=message_handler, args=(q,))
    thread.start()

    # Sending messages
    sender(q, "Hello")
    sender(q, "How are you?")
    sender(q, "exit")

    thread.join()

if __name__ == "__main__":
    main()