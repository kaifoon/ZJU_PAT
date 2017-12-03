
def PopSort(num, array):

    for i in range(num):
        flag = 0
        for k in range(i, num):
            if array[i] > array[k]:
                swap(array, i, k)
                flag = 1
        if not flag:
            break
    print('Pop Sort')
    for i in array:
        print(i, end=' ')


def InsertSort(num, array):

    for i in range(1, num):
        tmp = array[i]  # 摸下一张牌
        k = i
        while k > 0 and array[k - 1] > tmp:
            array[k] = array[k - 1]  # 移出空位
            k -= 1
        array[k] = tmp  # 新牌落位

    print('Insert Sort')
    for i in array:
        print(i, end=' ')


def swap(array, i, k):
    tmp = array[i]
    array[i] = array[k]
    array[k] = tmp


def main():
    num = int(input())
    line = input()
    nums = [int(i) for i in line.split(' ')]
    PopSort(num, nums)
    InsertSort(num, nums)


if __name__ == '__main__':
    main()
