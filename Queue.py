from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

# -------------Exercise 1-----------------------
food_order_queue = Queue()

def place_order(order_list):
    for order in order_list:
        print(f"Place order for {order}.")
        food_order_queue.enqueue(order)
        time.sleep(0.5)
        

def serve_order():
    while True:
        order = food_order_queue.dequeue()
        print(f"Now order {order} is served.")
        time.sleep(2)


# -------------Exercise 2-----------------------
def print_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for elem in range(n):
        front = numbers_queue.front()
        print("  ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()



if __name__ == "__main__":
    # orders = ['pizza','samosa','pasta','biryani','burger']
    # t1 = threading.Thread(target=place_order, args=(orders,))
    # t2 = threading.Thread(target=serve_order)

    # t1.start()
    # t2.start()
    print_binary_numbers(10)

    