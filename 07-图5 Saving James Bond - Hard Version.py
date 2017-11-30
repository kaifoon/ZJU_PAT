import math
from collections import deque

# 思路：问题核心是无向图单源最短路径问题，所以算法采用BFS了；
# 需解决：
# 1. 单独处理第一跳。题目要求存在多个最短时，输出第一跳的距离最小，所以我们可以把所有点距原点距离从小到大排序，
# 然后再对各点进行BFS。
# 2.路径输出的话，只有采用栈了。



def main():
    firstline = input()
    n, r = [int(k) for k in firstline.split(' ')]
    np = []
    fp = []
    BuildG(np, n)
    FirstStep(np, fp, r)
    if r > 42.5:
        print(1)
    else:
        for i in fp:
            BFS(i, np, n, r)


def BuildG(np, n):
    for i in range(n):
        line = input()
        x, y = [int(k) for k in line.split(' ')]
        dis = math.sqrt(x**2 + y**2)
        if max(abs(x), abs(y)) >= 50 or max(abs(x), abs(y)) <= 7.5:
            continue
        np.append({'x': x, 'y': y, 'distance': dis})


def FirstStep(np, fp, r):
    for i, k in enumerate(np):
        if k['distance'] <= r + 7.5:
            fp.append(i)


def BFS(first_p, np, n, r):
    n_path = []  # 存储路径，表示从起点first_p 到i 的上一个节点
    dist = []   # 存储路径长度
    for i in range(len(np)):
        n_path.append(-1)  # 存储父节点，-1表示无父节点
    for i in range(len(np)):
        if first_p == i:
            dist.append(1)  # 如果遇到第一个点，设置路径为1
        else:
            dist.append(0)

    flag = 0
    queue = deque()
    queue.append(first_p)
    while queue != deque([]):
        x = queue.popleft()
        if IsBorder(np, x, r):  # 判断从该点能否跳到岸上
            flag = 1
            break
        else:
            for i,v in enumerate(np):
                if dist[i] == 0 and Distance(np[x],v) <= r:
                    n_path[i] = x
                    dist[i] = dist[x] + 1
                    queue.append(i)

    if flag:
        print(dist[x] + 1)
        Print(n_path, x, np)
        exit(0)

def Distance(a, b):
    return math.sqrt(pow(a['x'] - b['x'], 2) + pow(a['y'] - b['y'], 2))


def IsBorder(np, v, r):
    if (50 - abs(np[v]['x']) <= r) or (50 - abs(np[v]['y']) <= r):
        return 1
    else:
        return 0


def Print(n_path, x, np):
    if n_path[x] != -1:
        Print(n_path, n_path[x], np)
    print(np[x]['x'], np[x]['y'])


if __name__ == '__main__':
    main()
