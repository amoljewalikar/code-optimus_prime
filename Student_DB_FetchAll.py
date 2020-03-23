import sqlite3

def fetch_ALL():
    try:
        db = sqlite3.connect('Student_DB')
        cursor = db.cursor()
        cursor.execute('''select * from Student_Info''')
        all_rec = cursor.fetchall()
        if all_rec == []:
            print("Empty !!")
        else:
            for record in all_rec:
                print("Roll : ", record[0], "Name :", record[1], "Surname :", record[2],
                      "Maths :", record[3], "Science :", record[4], "English :", record[5],
                      "Programming : ", record[6], "Electronics :", record[7], "\n")
    except Exception as E:
        print('Unable to interact with database ! ', E)
    finally:
        db.close()
