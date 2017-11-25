def main():
    firstline=input()
    m,n,k=[int(i) for i in firstline.split(' ')]
    flag=[]
    st=[]
    for i in range(k):
        flag.insert(i,1)
        t=1
        secondline = input()
        nums=secondline.split(' ')
        for j in range(n):
            num=int(nums[j])
            if flag[i]:
                while st == [] or st[-1] != num: # 不相等的值就栈递增，等到相等时候就弹出
                    st.append(t)
                    t+=1

                    if len(st) > m:  # 检查栈满，如果满就flag 为0 失败，跳到下一行
                        flag.insert(i,0)
                        break

            if flag[i] and st != [] and st[-1] == num: # 相等就模拟弹出，每个值进行比对
                st.pop()

        while st!=[]: #清空栈
            st.pop()

    for i in range(k):
        if flag[i]:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
