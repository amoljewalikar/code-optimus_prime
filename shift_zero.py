def string_shift_zero(s):
    r = ''
    for i in s:
        if i != '0':
            r += i
    return r + ('0'*s.count('0'))


print(string_shift_zero(input()))



'''
i/p

1A0SHK063730A00VVFA00UU0

o/p

1ASHK6373AVVFAUU00000000

'''

