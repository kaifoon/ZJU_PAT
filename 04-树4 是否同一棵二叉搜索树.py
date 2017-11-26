

# 思路：先建立模板树，然后依次将待测试树和其比较。
# 比较过的结点的标志设为1，若该结点未比较过且其数据不等，则两树不同。

class Node():
    def __init__(self, data, flag=0):
        self.data = data
        self.flag = flag
        self.left = None
        self.right = None


def main():
    firstline = input()
    n = int(firstline.split(' ')[0])
    while n:
        line = int(firstline.split(' ')[1])
        head = TreeBuild(n)
        for i in range(line):
            if Judge(head, n):
                print('Yes')
            else:
                print('No')
            FlagReset(head)
        TreeDelete(head)
        firstline = input()
        n = int(firstline.split(' ')[0])


def TreeBuild(num):
    nodes = input()
    d = nodes.split(' ')[0]
    head = NewNode(int(d))
    for i in nodes.split(' ')[1:num]:
        Insert(head, int(i))
    return head


def NewNode(data):
    p = Node(data)
    return p


def Insert(head, data):
    if head == None:
        head = NewNode(data)
    else:
        if data > head.data:
            Insert(head.right, data)
        else:
            Insert(head.left, data)
    T = head


def Judge(head, num):
    jnodes = input()
    T = head
    fflag = 1
    for node in jnodes.split(' '):
        node = int(node)
        while T != None and fflag != 0:
            if T.flag == 1:
                if node > T.data:
                    T = T.right
                else:
                    T = T.left
            elif T.flag == 0 and T.data == node:
                T.flag = 1
                break
            else:
                fflag = 0
                break

    if fflag == 0 or T == None:
        return 0
    else:
        return 1


def FlagReset(head):
    if head.left:
        FlagReset(head.left)
    if head.right:
        FlagReset(head.right)
    head.flag = 0


def TreeDelete(head):
    if head.left:
        TreeDelete(head.left)
    if head.right:
        TreeDelete(head.right)
    del head


if __name__ == '__main__':
    main()
