import threading
import time

BUFFER_SIZE = 5
buffer = []
mutex = threading.Lock()
cond_producer = threading.Condition(mutex)
cond_consumer = threading.Condition(mutex)

def producer():
    for i in range(10):
        with cond_producer:
            while len(buffer) == BUFFER_SIZE:
                cond_producer.wait()
            buffer.append(i)
            print(f"Produced: {i}")
            cond_consumer.notify()
        time.sleep(1)

def consumer():
    for _ in range(10):
        with cond_consumer:
            while len(buffer) == 0:
                cond_consumer.wait()
            item = buffer.pop()
            print(f"Consumed: {item}")
            cond_producer.notify()
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()