
def main():
    firstline = input()
    st,n,k=[int(i) for i in firstline.split(' ')]
    data={}
    next={}
    for i in range(n):
        eachline=input()
        addr,val,next_node =[int(k) for k in eachline.split(' ')]
        data[addr]=val
        next[addr]=next_node

    tmp=st
    adr=[]
    re=[]
    while tmp != -1:
        adr.append(tmp)
        tmp=next[tmp];

    for i in range(n):
        re.append(adr[i])

    i=0
    while k!=1 and i<n-n%k: # 不足k值的组不处理
        re[i]=adr[k-i%k-1+int(i/k)*k] # k=k-i + i int(i/k)*k 决定了第几次k
        i+=1

    for i in range(n-1):
        print("{0:05d} {1:d} {2:05d}".format(re[i],data[re[i]],re[i+1]))
    print("{0:05d} {1:d} -1".format(re[i+1],data[re[i+1]]))




if __name__ == '__main__':
    main()
