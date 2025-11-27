#producer consumer
import threading
import time
from collections import deque

BUFFER_SIZE = 5
buffer = deque()

lock = threading.Lock()
not_empty = threading.Condition(lock)
not_full = threading.Condition(lock)

def producer():
    item = 0
    for _ in range(10):
        with not_full:
            while len(buffer) == BUFFER_SIZE:
                not_full.wait()

            buffer.append(item)
            print(f"Produced: {item}")
            item += 1

            not_empty.notify()

        time.sleep(1)

def consumer():
    for _ in range(10):
        with not_empty:
            while not buffer:
                not_empty.wait()

            item = buffer.popleft()
            print(f"Consumed: {item}")

            not_full.notify()

        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
