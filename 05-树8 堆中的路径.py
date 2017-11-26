
Min = -1000


class Heap(object):
    """docstring for Heap"""

    def __init__(self):
        self.data = []
        self.size = 0


def main():
    firstline = input()
    n, t = [int(i) for i in firstline.split(' ')]
    heap = HeapCreate(n)
    vals = input()
    for val in vals.split(' ')[0:n]:
        Insert(heap, int(val))

    qnums = input()
    for k in qnums.split(' ')[0:t]:
        PrintPath(heap, int(k))


def HeapCreate(n):
    h = Heap()
    for i in range(n + 1):
        h.data.append(0)
    h.size = 0
    h.data[0] = Min

    return h


def Insert(heap, val):
    heap.size += 1
    i = heap.size
    while val < heap.data[int(i / 2)]:
        heap.data[i] = heap.data[int(i / 2)]
        i = int(i / 2)

    heap.data[i] = val


def PrintPath(heap, d):
    while d > 0:
        print(heap.data[d], end=' ')
        d = int(d / 2)
    print()


if __name__ == '__main__':
    main()
