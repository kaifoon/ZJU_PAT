

# 思路：Prim算法。结构是邻接矩阵。
# 但要比真正的Prim算法简略，因为题目只要输出总权值，所以我们就不用
# 同时建立最小生成树，只需要累加边权值
INF = 65535


def main():
    firstline = input()
    n, m = [int(i) for i in firstline.split(' ')]
    G = BuildG(n, m)
    wt = Prim(G, n)
    print(wt)


def Build(n, m):
    G = []
    for i in range(n + 1):
        G.append([])
        for j in range(n + 1):
            if i == j:
                G[i].append(0)
            else:
                G[i].append(INF)

    for i in range(m):
        line = input()
        s, d, wt = [int(k) for k in line.split(' ')]
        G[s][d] = wt
        G[d][s] = wt


def Prim(G, n):
    sumw = 0
    vcnt = 1
    dist = []
    for i in range(n + 1):
        dist.append(G[1][i])
    while True:
        v = FindMin(n)
        if v == -1:
            break
        sumw += dist[v]
        dist[v] = 0  # 收录进生成树，不为0表示不是生成树的点；
        vcnt += 1
        for i in range(n + 1):
            if dist[i] and G[v][i] < INF:
                if G[v][i] < dist[i]:
                    dist[i]=G[v][i]

    if vcnt < n:
        return -1
    else:
        return sumw

def FindMin(n):
    min_ = INF
    minv = 0
    for i in range(n+1):
        if dist[i] and dist[i] < min_:
            min_ = dist[i]
            minv=i
    if min_ == INF: # 顶点不存在
        return -1
    else:
        return minv
        


if __name__ == '__main__':
    main()
