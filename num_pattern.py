def num_pat(n):
    l = 1
    for i in range(1,n+1):
        for j in range(0,i):
            print(l,end=' ')
            l += 1
        print()
    
num_pat(int(input()))




'''
i/p

5

o/p

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
