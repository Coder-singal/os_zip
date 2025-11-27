# Page Replacement Algorithms in Python

def fifo(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)          # remove oldest
            memory.append(page)        # insert new page
        # if page already in memory → no change

    return page_faults


def lru(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)          # remove least recently used (front)
            memory.append(page)        # add as most recently used
        else:
            # page hit → move it to end (most recently used)
            memory.remove(page)
            memory.append(page)

    return page_faults


def optimal(pages, capacity):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]

        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                # decide which page to replace
                future = pages[i+1:]
                indices = []

                for m in memory:
                    if m in future:
                        indices.append(future.index(m))
                    else:
                        indices.append(float('inf'))   # not used again

                victim = memory[indices.index(max(indices))]
                memory.remove(victim)

            memory.append(page)

    return page_faults


if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3

    print("Reference string:", pages)
    print("Frame capacity:", capacity)
    print("FIFO Page Faults    :", fifo(pages, capacity))
    print("LRU Page Faults     :", lru(pages, capacity))
    print("Optimal Page Faults :", optimal(pages, capacity))
