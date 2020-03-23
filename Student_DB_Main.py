import Student_DB_Delete
import Student_DB_FetchAll
import Student_DB_Insert
import Student_DB_Percent
import Student_DB_Search
import Create_DB_Table

while True:
    print("\nTo Insert student(s) detail press '1' :\nTo Delete student's detail press '2' :\n\
To Search student's detail press '3' :\nTo see ALL students record press '4' :\nTo calculate Percentage of student press '5' :\n\
To exit press '6' :")
    ch = int(input())
    if ch == 1:
        Create_DB_Table.creation()
        Student_DB_Insert.insert_info()
    if ch == 2:
        Student_DB_Delete.delete_info()
    if ch == 3:
        search_student = int(input('Enter a roll number to search record of a student : '))
        Student_DB_Search.search_info(search_student)
    if ch == 4:
        Student_DB_FetchAll.fetch_ALL()
    if ch == 5:
        search_student = int(input('Enter a roll number to search record of a student : '))
        record = Student_DB_Search.search_info(search_student)
        print("Percentage :", Student_DB_Percent.calc_Percentage(record))
    if ch == 6:
        break
