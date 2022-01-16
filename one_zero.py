def one_zero(n):
    for i in range(0,n):
        for j in range(0,i+1):
            if ((j+i)%2) == 0:
                print('0',end='')
            else:
                print('1',end='')
        print('')

one_zero(5)



'''
i/p

5

o/p

1
01
101
0101
10101
'''
