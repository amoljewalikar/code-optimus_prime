
''' Que.
N = no. of string input
A = array of string
slice 3 strings sharing common vowel, check possible con=mbinations and print
count.
'''

from itertools import combinations

def countWays(A):
    ls_a, ls_e, ls_i, ls_o, ls_u = [], [], [], [], []
    ls_vowel = []
    for ele in A:
        if 'a' in ele:
            ls_a.append(ele)
        if 'e' in ele:
            ls_e.append(ele)
        if 'i' in ele:
            ls_i.append(ele)
        if 'o' in ele:
            ls_o.append(ele)
        if 'u' in ele:
            ls_u.append(ele)
    if len(ls_a) >= 3:
        ls_vowel.append(ls_a)
    if len(ls_e) >= 3:
        ls_vowel.append(ls_e)
    if len(ls_i) >= 3:
        ls_vowel.append(ls_i)
    if len(ls_o) >= 3:
        ls_vowel.append(ls_o)
    if len(ls_u) >= 3:
        ls_vowel.append(ls_u)

    #print(ls_vowel)
    fls = []
    for sets in ls_vowel:
        tmp = []
        if len(sets) == 3:
            fls.append(tuple(sets))
        else:
            tmp = list(combinations(sets,3))
            for i in tmp:
                if tuple(sorted(i)) not in fls:
                    fls.append(i)
                    
    return len(set(fls))                
        
if __name__ == "__main__":
    '''N = int(input("Test cases count : "))
    for arr in range(N+1):
        l = []                         <- take proper input 1) number of tatse cases
                                                            2) list of string in array_list
        for j in range(arr):
            l.append(input().split())
    print(l)'''
    array_str = [['aei','aeo','aou','eou'],['aeiou','abuoe','xyzio','ozooi','eeiio']]
    for A in array_str:
        print(countWays(A))
