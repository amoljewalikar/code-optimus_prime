import sqlite3
def creation():
    try:
        db = sqlite3.connect('Student_DB')
        my_cur = db.cursor()
        my_cur.execute('''create table if not exists Student_Info
        (Roll int NOT NULL,
        Name text, Surname text,
        Maths int NOT NULL, Science int NOT NULL, English int NOT NULL,
        Programming int NOT NULL, Electronics int NOT NULL, PRIMARY KEY (Roll))''')
        my_cur.close()
    except Exception as E:
        print("Unable to interact : ", E)
    finally:
        db.close()
