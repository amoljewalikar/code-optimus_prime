import sqlite3
get_std_info = []
def insert_info():
    count = int(input("Enter how many student details you want to insert : "))
    for info in range(count):
        roll = int(input("Enter Roll Number : "))
        name = input("Enter Name of Student : ")
        surname = input("Enter Surame of Student : ")
        maths = int(input("Enter Maths Subject Marks : "))
        sci = int(input("Enter Science Subject Marks : "))
        eng = int(input("Enter English Subject Marks : "))
        prg = int(input("Enter Programming Subject Marks : "))
        ele = int(input("Enter Electronics Subject Number : "))
        get_std_info.append((roll, name, surname, maths, sci, eng, prg, ele))
    print(get_std_info)
    try:
        db = sqlite3.connect('Student_DB')
        cursor = db.cursor()
        cursor.executemany('''insert into Student_Info values(?,?,?,?,?,?,?,?)''', get_std_info)
        print('Record(s) Inserted successfully')
        cursor.close()
    except Exception as E:
        print('Unable to interact with database ! ', E)
    else:
        db.commit()
