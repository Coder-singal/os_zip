import threading
import time

read_count = 0
read_count_lock = threading.Lock()
resource_lock = threading.Lock()

def reader(id):
    global read_count

    with read_count_lock:
        read_count += 1
        if read_count == 1:
            resource_lock.acquire()

    print(f"Reader {id} is reading")
    time.sleep(1)

    with read_count_lock:
        read_count -= 1
        if read_count == 0:
            resource_lock.release()

def writer(id):
    resource_lock.acquire()
    print(f"Writer {id} is writing")
    time.sleep(1)
    resource_lock.release()

threads = []

threads.append(threading.Thread(target=reader, args=(1,)))
threads.append(threading.Thread(target=writer, args=(1,)))
threads.append(threading.Thread(target=reader, args=(2,)))
threads.append(threading.Thread(target=writer, args=(2,)))
threads.append(threading.Thread(target=reader, args=(3,)))

for t in threads:
    t.start()

for t in threads:
    t.join()
