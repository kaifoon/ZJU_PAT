

# 思路：这是最短路径问题。
# 稠密图，数据结构采用邻接矩阵。
# 用Floyd算法求出任两点间的最短路径；
# 然后找出一点到其余点的路径最大值；
# 再找出这些最大值的最小值
Inf = 65535


def main():
    firstline = input()
    n, m = [int(i) for i in firstline.split(' ')]
    G = BuildG(n, m)
    Floyd(G, n)

    # 找出路径最大值的最小值；
    min_len = 101
    num = 0
    for i in range(1, n + 1):
        t = Find_Max(G, i, n)
        if t == Inf:
            print(0)
            exit()
        if t < min_len:
            num = i
            min_len = t
    print('{0} {1}'.format(num, min_len))


def BuildG(nv, m):
    G = []
    for i in range(nv + 1):
        G.append([])
        for k in range(nv + 1):
            if i == k:
                G[i].append(0)  # 0表示无边；
            else:
                G[i].append(Inf)  # 最大值表示两点不可达；
    for i in range(m):
        line = input()
        a, b, v = [int(k) for k in line.split(' ')]  # 读入数据，赋值
        G[a][b] = G[b][a] = v
    return G


def Find_Max(G, row, n):
    max_v = 0
    for i in range(1, n + 1):
        max_v = max(max_v, G[row][i])

    return max_v


def Floyd(G, nv):
    for k in range(1, nv + 1):
        for i in range(1, nv + 1):
            for j in range(1, nv + 1):
                if G[i][k] + G[k][j] < G[i][j]:
                    G[i][j] = G[i][k] + G[k][j]


if __name__ == '__main__':
    main()
