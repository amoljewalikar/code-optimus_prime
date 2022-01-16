def matrix_sum(m):
    ls = m
    r = 2
    mtx = []
    mtx_inv = []
    i = 0
    while i < len(ls):
        mtx.append(sum(ls[i:i+r]))
        i+=r
    row_max_sum = max(mtx)

    i = 0
    l1,l2 = [],[]
    while i < len(ls):
        if i%2 == 0:
            l1.append(ls[i])
        else:
            l2.append(ls[i])
        i+=1
    mtx_inv.append(sum(l1))
    mtx_inv.append(sum(l2))
    col_max_sum = max(mtx_inv)

    return row_max_sum+col_max_sum


if __name__ == "__main__":
    row = 2#int(input())
    col = 2#int(input())
    m = [1,2,5,6,4,9]
    print(matrix_sum(m))
