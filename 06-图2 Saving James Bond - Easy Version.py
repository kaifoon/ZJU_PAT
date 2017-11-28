import math

MinD =42.5


# 圆圈直径15m
# 把每个点存入一维数组，递归两点距离是否满足即可；
def main():
    pv = []
    Firstp = []
    firstline = input()
    n, d = [int(i) for i in firstline.split(' ')]
    Build_array(pv, n)

    if d >= MinD:  # 检查是否一步就能跳上岸
        print('Yes')
        exit()
# 由于圆圈直径  15m，所以不能把圆圈看作一个点，检查第一步周围有没有可跳点
    Create_first(pv, Firstp, n, d)
    if Firstp == []:
        print('No')
        exit()
    # 如果周围有可挑点就从第一个周围点进行深度优先图遍历
    for i in Firstp:
        Search_dfs(pv, i, d, n)
    print('No')


def Distance(a, b):
    return math.sqrt(pow(a['x'] - b['x'], 2) + pow(a['y'] - b['y'], 2))


def Build_array(point_arr, n):
    for i in range(n):
        cor = input()
        x, y = [int(k) for k in cor.split(' ')]
        point_arr.append({'x': x, 'y': y, 'visited': 0})


def Create_first(point_arr, firstp, n, d):
    for i in range(n):
        if Distance(point_arr[i], {'x': 0, 'y': 0, 'visited': 1}) <= (d + 7.5):
            firstp.append(i)


def Search_dfs(point_arr, i, d, n):
    point_arr[i]['visited'] = 1
    # 如果发现鳄鱼离岸距离小于最大跳长度，结束递归打印Yes
    if (50 - abs(point_arr[i]['x'])) <= d or (50 - abs(point_arr[i]['y'])) <= d:
        print('Yes')
        exit()
    for j in range(n):
        if not point_arr[j]['visited'] and Distance(point_arr[i], point_arr[j]) <= d:
            Search_dfs(point_arr, j, d, n)


if __name__ == '__main__':
    main()
