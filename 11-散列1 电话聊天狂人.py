
class HashNode():
    def __init__(self, data=None, count=0):
        self.data = data
        self.count = count
        self.next = None


def CreateHashTbl():
    H = []
    for i in range(10**4):
        H.append(HashNode())
    return H


def InsertHashTal(hashtable, p1):

    addr1 = int(p1[-5:]) % 9999
    if not hashtable[addr1].data:
        hashtable[addr1].data = p1
        hashtable[addr1].count += 1
    else:
        tmp = hashtable[addr1].next
        while tmp and tmp.data != p1:
            tmp = tmp.next
        if tmp:
            tmp.count += 1
        else:
            newn = HashNode(p1, count=1)
            newn.next = hashtable[addr1].next
            hashtable[addr1].next = newn


def ScanAndOutput(num, hashtable):
    for i in range(num):
        line = input()
        for k in line.split(' '):
            InsertHashTal(hashtable, k)
    maxn = 0
    partner = 0
    res = ''
    for node in hashtable:
        if node.data==None:
            continue
        if maxn < node.count:
            maxn = node.count
            partner = 1
            res = node.data
        elif maxn == node.count:
            partner += 1
            for i, k in enumerate(res):
                if int(k) == int(node.data[i]):
                    continue
                elif int(k) < int(node.data[i]):
                    res = node.data
                    break
        tmp = node.next
        while tmp:
            if maxn < tmp.count:
                maxn = tmp.count
                partner = 1
                res = tmp.data
            elif maxn == tmp.count:
                partner += 1
                for i, k in enumerate(res):
                    if int(k) == int(tmp.data[i]):
                        continue
                    elif int(k) < int(tmp.data[i]):
                        res = tmp.data
                        break
            tmp = tmp.next
    if partner == 1:
        print('{0} {1}'.format(res, maxn))
    else:
        print('{0} {1} {2}'.format(res, maxn, partner))


def main():
    hashtal = CreateHashTbl()
    num = int(input())
    ScanAndOutput(num, hashtal)


if __name__ == '__main__':
    main()
