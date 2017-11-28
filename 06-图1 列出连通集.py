from collections import deque
G = []
visited = []


# 思路：考虑到要按照从小到大的顺序遍历输出，结构用邻接矩阵（邻接表不方便，要用小根堆才能实现）。
# 1.建立图（用数组表示）， 依次读入各边；
# 2.DFS遍历输出；
# 3.BFS遍历输出；


# todo dfs 邻边遍历有问题，按序输出

def main():
    firstline = input()
    v, e = [int(k) for k in firstline.split(' ')]
    BuildG(v, e)
    ListDfs(v)
    InitVisited(v)
    ListBfs(v)


def BuildG(vetex, edge):
    for i in range(vetex):
        visited.append(0)
    for i in range(int(vetex * (vetex + 1) / 2)):
        G.append(0)
    for k in range(edge):
        edges = input()
        v1, v2 = [int(i) for i in edges.split(' ')]
        G[int(max(v1,v2) * (max(v1,v2) + 1)/2 + min(v2,v1))] = 1


def ListDfs(vetex):

    for i in range(vetex):
        if not visited[i]:
            print('{', end=' ')
            Dfs(i, vetex)
            print('}')


def ListBfs(v):
    for i in range(v):
        if not visited[i]:
            print('{', end=' ')
            Bfs(i, v)
            print('}')


def Dfs(n,vetex):
    visited[n] = 1
    print(n, end=' ')
    for i in range(n+1):
        if not visited[i] and G[int(n * (n + 1) / 2 + i)]:
            n+=1
            if n>vetex:
                return
            Dfs(n,vetex)


def Bfs(n, v):
    queue = deque()
    print(n)
    visited[n] = 1
    queue.append(n)
    while queue != deque([]):
        tv = queue.popleft()
        for i in range(n+1):
            if not visited[i] and G[int(tv * (tv + 1) / 2 + i)]:
                n+=1
                if n>v:
                    break
                print(i, end=' ')
                visited[i] = 1
                queue.append(i)


def InitVisited(v):
    for i, k in enumerate(visited):
        visited[i] = 0


if __name__ == '__main__':
    main()
