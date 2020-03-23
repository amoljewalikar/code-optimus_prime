str1 = 'abaghfhtababajdhdh'
str2 = 'aba'

for i in range(len(str1)) :
    if str1[i:i+(len(str2))] == str2 :
       print(i)


