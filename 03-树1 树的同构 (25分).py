

class TreeNode():
    def __init__(self,ch,left,right):
        self.ch=ch
        self.left=left
        self.right=right

def main():
    m1,tr1= TreeBuild()
    m2,tr2= TreeBuild()

    if isOmorphic(tr1,m1,tr2,m2):
        print('Yes')
    else:
        print('No')

def TreeBuild():
    n = int(input())
    m=0
    check = []
    tNode = []
    for i in range(n):
        check.append(0)

    for i in range(n):
        line = input()
        ch,left,right=[k for k in line.split(' ')]
        tmp = TreeNode(ch,left,right)
        if left == '-':
            tmp.left=-1
        else:
            tmp.left=int(left)
            check[tmp.left] = 1
        if right =='-':
            tmp.right=-1
        else:
            tmp.right=int(right)
            check[tmp.right]=1
        tNode.append(tmp)

    for i in range(n):
        if check[i]==0:
            m=i
            break
    return m,tNode

def isOmorphic(tnode1,root1,tnode2,root2):
    if root1==-1 and root2 == -1:
        return 1
    if (root1==-1 and root2 != -1) or (root1 != -1 and root2 == -1):
        return 0
    if tnode1[root1].ch != tnode2[root2].ch:
        return 0

    t1 = isOmorphic(tnode1,tnode1[root1].left,tnode2,tnode2[root2].left) and isOmorphic(tnode1,tnode1[root1].right,tnode2,tnode2[root2].right)
    t2 = isOmorphic(tnode1,tnode1[root1].right,tnode2,tnode2[root2].left) and isOmorphic(tnode1,tnode1[root1].left,tnode2,tnode2[root2].right)
    return t1 or t2


if __name__ == '__main__':
    main()
