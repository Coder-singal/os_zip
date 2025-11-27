def is_safe(available, max_need, allocation):
    n = len(available)    # Number of resources
    p = len(allocation)   # Number of processes
    work = available[:]
    finish = [False] * p
    safe_seq = []

    while len(safe_seq) < p:
        found = False
        for i in range(p):
            if not finish[i]:
                # Check if Need <= Work
                need = [max_need[i][j] - allocation[i][j] for j in range(n)]
                if all(need[j] <= work[j] for j in range(n)):
                    for j in range(n):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_seq.append(i)
                    found = True
        if not found:
            return False, []
    return True, safe_seq

# Data
# Resources: A, B, C
avail = [3, 3, 2]
# Processes P0, P1, P2, P3, P4
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max_n = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]

safe, seq = is_safe(avail, max_n, alloc)
if safe:
    print(f"System is Safe. Sequence: {seq}")
else:
    print("System is in Deadlock!")