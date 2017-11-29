from collections import deque


visited = []


class Avnode:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class Graph(object):
    """docstring for Graph"""

    def __init__(self, nv, ne=0):
        super(Graph, self).__init__()
        self.nv = nv
        self.ne = ne
        self.ah = []
        for i in range(self.nv + 1):
            tmp = Avnode(i)
            self.ah.append(tmp)


def main():
    firstline = input()
    v, e = [int(i) for i in firstline.split(' ')]
    G = BuildG(v, e)
    OutputE(G)


def Init_Graph(v):
    for i in range(v + 1):
        visited.append(0)
    G = Graph(v)

    return G


def OutputE(G):
    for i in range(1, G.nv + 1):
        cnt = BFS(G, i)

        for j in range(1, G.nv + 1):
            visited[j] = 0
        print('{0}: {1:.2f}%'.format(i, cnt * 100 / G.nv))


def BuildG(v, e):
    G = Init_Graph(v)
    for i in range(e):
        edges = input()
        v1, v2 = [int(k) for k in edges.split(' ')]
        Insert_E(G, v1, v2)
    return G


def Insert_E(G, v1, v2):

    av = Avnode(v2)
    av.next = G.ah[v1].next  # 将点插入到头部
    G.ah[v1].next = av

    av2 = Avnode(v1)
    av2.next = G.ah[v2].next  # 无向图两边都要插入；
    G.ah[v2].next = av2


def BFS(G, v):
    visited[v] = 1
    cnt = 1
    queue = deque()
    last = v
    queue.append(v)

    tail = 0
    level = 0
    while queue != deque([]):
        v = queue.popleft()
        w = G.ah[v].next
        while w:
            if not visited[w.data]:
                visited[w.data] = 1
                cnt += 1
                tail = w.data
                queue.append(w.data)
            w = w.next

        if v == last:
            level += 1
            last = tail
        if level == 6:
            break
    return cnt


if __name__ == '__main__':
    main()
