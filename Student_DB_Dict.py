std={}
while True:
    print("\nTo Insert student's detail press '1' :\nTo Delete student's detail press '2' :\n\
To Search student's detail press '3' :\nTo see all students record press '4' :\nTo calculate Percentage of student press '5' :\n\
To exit press '6' :")
    i=int(input())
    if i==1:
        n=int(input("Enter how many student details you want to insert : "))
        for i in range(n):
            roll=int(input("Enter a Roll Number : "))
            std[roll]={}
            std[roll]['Name']=input("Enter a name of Student : ")
            std[roll]['Class']=input("Enter student's class std : ")
            std[roll]['Marks']={}
            std[roll]['Marks']['Maths']=input("Enter marks of Maths subject : ")
            std[roll]['Marks']['Science']=input("Enter marks of Science subject : ")
            std[roll]['Marks']['English']=input("Enter marks of English subject : ")
            std[roll]['Marks']['Programming']=input("Enter marks of Programming subject : ")
            std[roll]['Marks']['Electronics']=input("Enter marks of Electronics subject : ")
    elif i==2:
        roll=int(input("Enter a Roll Number to delete student record : "))
        if roll in std:
            del(std[roll])
            print("\nStudent's Record Deleted Successfully.")
        else:
            print("\nEntered Roll number Does not Exists!")
    elif i==3:
        roll=int(input("Enter a Roll Number to find Student: "))
        if roll not in std:
            print("\nEntered Roll number Does not Exists!")
        else:
            print("\n Details of entered Roll number :\n",std[roll])
    elif i==4:
        print("\n Students Database:\n",std)
    elif i==5:
        roll=int(input("Enter a Roll Number to check Percentage and Grade of student : "))
        if roll not in std:
            print("\nEntered Roll number Does not Exists!")
        else:
            per=(int(std[roll]['Marks']['Maths'])+int(std[roll]['Marks']['Science'])+int(std[roll]['Marks']['English'])+\
                 int(std[roll]['Marks']['Programming'])+int(std[roll]['Marks']['Electronics'])) / 5
            if (int(std[roll]['Marks']['Maths']) or int(std[roll]['Marks']['Science']) or int(std[roll]['Marks']['English']) \
               or int(std[roll]['Marks']['Programming']) or int(std[roll]['Marks']['Electronics'])) < 40:
                print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : F ")
            else:
                if per>=75:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : O ")
                elif per>=65 and per<75:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : A ")
                elif per>=55 and per<65:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : B ")
                elif per>=50 and per<55:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : C ")
                elif per>=45 and per<50:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : D ")
                elif per>=40 and per<45:
                    print("Name:",std[roll]['Name'],"Percentage : ",per,"Grade : E ") 
    elif i==6:
        break
    
          
