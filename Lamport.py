# Lamport Clock + Simple Mutual Exclusion (Fixed)

n = int(input("Processes: "))
clock = [0]*n
queue = []

while True:
    print("\n1.Request  2.Release  3.Show  4.Exit")
    c = int(input("Choice: "))

    if c == 1:
        p = int(input("Process ID (0 to %d): " % (n-1)))
        if p < 0 or p >= n:
            print("Invalid ID!")
            continue
        clock[p] += 1
        queue.append((clock[p], p))

    elif c == 2:
        if queue:
            queue.sort()
            print("Released:", queue.pop(0))
        else:
            print("Queue empty")

    elif c == 3:
        print("Clocks:", clock)
        print("Queue:", sorted(queue))

    else:
        break
