# Objective:
# To implement Readers–Writers problem using Monitors in Python.

import threading
import time
import random

# ----- Monitor for Readers–Writers -----
class RWMonitor:
    def __init__(self):
        self.read_count = 0
        self.read_count_lock = threading.Lock()   # protects read_count
        self.resource_lock = threading.Lock()     # shared resource lock

    def start_read(self):
        with self.read_count_lock:
            self.read_count += 1
            if self.read_count == 1:
                # first reader locks the resource
                self.resource_lock.acquire()

    def end_read(self):
        with self.read_count_lock:
            self.read_count -= 1
            if self.read_count == 0:
                # last reader releases the resource
                self.resource_lock.release()

    def start_write(self):
        # writer needs exclusive access
        self.resource_lock.acquire()

    def end_write(self):
        self.resource_lock.release()


monitor = RWMonitor()


# ----- Reader Thread Function -----
def reader(rid):
    for _ in range(3):  # read 3 times (you can change/remove this)
        time.sleep(random.uniform(0.5, 1.5))  # simulate arrival
        monitor.start_read()
        print(f"Reader {rid} is reading.")
        time.sleep(random.uniform(0.5, 1.0))  # simulate read time
        monitor.end_read()


# ----- Writer Thread Function -----
def writer(wid):
    for _ in range(3):  # write 3 times
        time.sleep(random.uniform(0.5, 2.0))  # simulate arrival
        monitor.start_write()
        print(f"Writer {wid} is writing.")
        time.sleep(random.uniform(0.5, 1.5))  # simulate write time
        monitor.end_write()


# ----- Create and Start Threads -----
threads = []

# 3 readers
for i in range(3):
    t = threading.Thread(target=reader, args=(i + 1,))
    threads.append(t)

# 2 writers
for i in range(2):
    t = threading.Thread(target=writer, args=(i + 1,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Program finished.")
