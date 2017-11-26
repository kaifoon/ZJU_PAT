
# 思路：考察并查集操作


def main():
    n = int(input())

    co = Create(n)
    while True:
        line = input().split(' ')
        nodes = [int(num) for num in line[1:]]
        if line[0] == 'C':

            CheckCon(co, nodes)
        elif line[0] == 'I':
            Insert(co, nodes)
        elif line[0] == 'S':
            CheckNet(co, n)
            break


def Create(n):
    co = []
    for i in range(n + 1):  # 下标表示编号，值表示父节点
        co.append(-1)    # 每个节点根节点值为-1，表示各节点独立

    return co


def FindRoot(co, d):  # 找出根节点
    if co[d] < 0:
        return d
    else:
        # 表示将所有子节点均指向一个总根，用到了路径压缩思想；以缩减查找规模；
        co[d] = FindRoot(co, co[d])
        return co[d]


def CheckCon(co, line):
    # 检查连通性
    root1 = FindRoot(co, line[0])
    root2 = FindRoot(co, line[1])

    if root1 == root2:
        print('yes')
    else:
        print('no')


def Union(co, root1, root2):  # 合并
    if co[root1] < co[root2]:  # 用到了按秩归并， 把小树并到大树上；
        co[root1] += co[root2]
        co[root2] = root1
    else:
        co[root2] += co[root1]
        co[root1] = root2


def Insert(co, line):

    root1 = FindRoot(co, line[0])
    root2 = FindRoot(co, line[1])

    if root1 != root2:
        Union(co, root1, root2)


def CheckNet(co, n):
    cnt = 0
    for i in range(1, n + 1):
        if co[i] < 0:
            cnt += 1
    if cnt == 1:
        print('The network is connected.')
    else:
        print('There are {0} components.'.format(cnt))


if __name__ == '__main__':
    main()
