import threading
import time
import random
import queue

buffer = queue.Queue(maxsize=5)

def producer():
    for _ in range(5):
        item = random.randint(1, 100)
        buffer.put(item)   # blocks if full
        print(f"Producer produced: {item} | Buffer: {list(buffer.queue)}")
        time.sleep(1)

def consumer():
    for _ in range(5):
        item = buffer.get()  # blocks if empty
        print(f"Consumer consumed: {item} | Buffer: {list(buffer.queue)}")
        time.sleep(1.5)

if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()