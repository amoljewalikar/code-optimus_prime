def string_remove(s):
    r = ''
    for i in range(len(s)):
        if i == 5:
            r += s[i].upper()
        else:
            r += s[i]
    return r[3:]

print(string_remove(input()))



'''
i/p

amoljewalikar

o/p

ljEwalikar

'''
