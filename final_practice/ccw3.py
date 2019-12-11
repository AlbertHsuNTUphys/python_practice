def Count_Change_Ways(n, s):
    # s.sort()
    l = [0 for i in range(n+1+s[-1])]
    l[0] = 1
    for i in s:
        for k in range(i,len(l)):
            l[k] += l[k-i]

    # print(l)
    return l[n]

if __name__ == "__main__":
    print(Count_Change_Ways(25500, [1, 2, 5, 10, 50, 100, 101] ) )
    # print(Count_Change_Ways(20, [1,2]))


 
