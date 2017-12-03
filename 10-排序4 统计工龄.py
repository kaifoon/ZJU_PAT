from collections import Counter


def BucketSort(array):
    tmp_arr = []
    for i in range(50):
        tmp_arr.append(0)
    for i in array:
        tmp_arr[i] += 1
    for k, v in enumerate(tmp_arr):
        if v != 0:
            print('{0}:{1}'.format(k, v))


def BucketIns(array):

    for k, v in sorted(Counter(array).items()):
        print('{0}:{1}'.format(k, v))


def main():
    num = int(input())
    line = input()
    nums = [int(i) for i in line.split(' ')]
    # BucketSort(nums)
    BucketIns(nums)


if __name__ == '__main__':
    main()
