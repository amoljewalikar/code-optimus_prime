import sqlite3

def delete_info():
    del_student = int(input('Enter a roll number to delete record of student : '))
    try:
        db = sqlite3.connect('Student_DB')
        cursor = db.cursor()
        cursor.execute('''delete from Student_Info where Roll = ?''', (del_student,))
        db.commit()
        print('Record deleted successfully')
        cursor.close()
    except Exception as E:
        print('Student Record could NOT be deleted. ', E)
    else:
        db.close()
