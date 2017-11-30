from collections import deque

# 思路：dijikstra算法求无向图的单源最短路径；
# 数据结构用邻接矩阵；
Inf = 65535


class Graph(object):
    """docstring for Graph"""

    def __init__(self, nv, ne):
        super(Graph, self).__init__()
        self.nv = nv
        self.ne = ne
        self.ma = []


def main():
    dist = []    # 存储路径长度；
    cost = []    # 存储路径费用；
    col = []     # 记录最短路径的点；
    firstline = input()
    n, m, s, d = [int(i) for i in firstline.split(' ')]

    G = BuildG(n, m)

    Dijkstra(G, s, d, dist, cost, col)


def BuildG(n, m):
    G = Graph(n, m)
    for i in range(n):
        G.ma.append([])
        for k in range(n):
            G.ma[i].append({'dis': Inf, 'fee': Inf})

    for i in range(m):
        line = input()
        c1, c2, d, f = [int(i) for i in line.split(' ')]
        G.ma[c1][c2] = {'dis': d, 'fee': f}
        G.ma[c2][c1] = {'dis': d, 'fee': f}

    return G


def Dijkstra(G, start, des, dist, cost, col):
    for i in range(G.nv):
        dist.append(G.ma[start][i]['dis'])
        cost.append(G.ma[start][i]['fee'])
        col.append(0)

    dist[start] = 0
    col[start] = 1  # 先收录起点
    while True:
        minv = FindMin(G, dist, col)
        if minv == -1:
            break
        col[minv] = 1
        for i in range(G.nv):
            if col[i] == 0:
                if dist[minv] + G.ma[minv][i]['dis'] < dist[i]:
                    dist[i] = dist[minv] + G.ma[minv][i]['dis']
                    cost[i] = cost[minv] + G.ma[minv][i]['fee']
                elif dist[minv] + G.ma[minv][i]['dis'] == dist[i]:
                    cost[i] = min(cost[minv] + G.ma[minv][i]['fee'], cost[i])

    print(dist[des], cost[des])


def FindMin(G, dist, col):
    mindi = 501
    for i in range(G.nv):
        if col[i] == 0 and dist[i] < mindi:
            mindi = dist[i]
            minv = i
    if mindi < 501:
        return minv
    else:
        return -1  # 不存在返回-1


if __name__ == '__main__':
    main()
