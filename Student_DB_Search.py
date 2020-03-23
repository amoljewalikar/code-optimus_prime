import sqlite3

def search_info(rolls):
    try:
        db = sqlite3.connect('Student_DB')
        cursor = db.cursor()
        cursor.execute('''select * from Student_Info where Roll = ?''', (rolls,))
        record = cursor.fetchone()
        if not record:
            print("Record of ", rolls, " not Found!!")
            return record
        else:
            print("\nRoll : ", record[0], "\nName :", record[1], "\nSurname :", record[2],
                  "\nMaths :", record[3], "\nScience :", record[4], "\nEnglish :", record[5],
                  "\nProgramming : ", record[6], "\nElectronics :", record[7])
            return record
    except Exception as E:
        print('Student Record could NOT Found! ', E)
    finally:
        db.close()
