from collections import deque


class TreeNode():
    def __init__(self, left, right):
        self.left = left
        self.right = right


def TreeBuild():
    n = int(input())
    check = []
    tr = []
    for i in range(n):
        check.append(0)

    for i in range(n):
        left, right = [k for k in input().split(' ')]
        tmp = TreeNode(left, right)
        if left == '-':
            tmp.left = -1
        else:
            tmp.left = int(left)
            check[tmp.left] = 1

        if right == '-':
            tmp.right = -1
        else:
            tmp.right = int(right)
            check[tmp.right] = 1
        tr.append(tmp)

    for i in range(n):
        if check[i] == 0:
            r = i
            break

    return r, tr


def LevelOrder(tree, root):
    queue = deque()
    queue.append(root)
    while queue != deque([]):
        tmp = queue.popleft()
        if tree[tmp].left == -1 and tree[tmp].right == -1:
            print(tmp, end=' ')
        else:
            if tree[tmp].left != -1:
                queue.append(tree[tmp].left)
            if tree[tmp].right != -1:
                queue.append(tree[tmp].right)


def main():
    root, tr = TreeBuild()
    LevelOrder(tr, root)


if __name__ == '__main__':
    main()
