import sqlite3

class DB():
    def __init__(self):
        self.connect = sqlite3.connect("db_student.db")
        self.cursor = self.connect.cursor()
        
    # Create table if not exist
    def create_table(self):
        try:
            table_create_query = '''CREATE TABLE "student" (
                                        "id_student"	INTEGER NOT NULL UNIQUE,
                                        "firstName_student"	TEXT NOT NULL,
                                        "secondName_student"	TEXT NOT NULL,
                                        "birthday_student"	TEXT NOT NULL,
                                        "academicYear_student"	TEXT NOT NULL,
                                        "level_student"	TEXT NOT NULL,
                                        "comment_student"	TEXT,
                                        "semOne_student"	REAL DEFAULT 0,
                                        "semTwo_student"	REAL DEFAULT 0,
                                        "General_student"	REAL DEFAULT 0,
                                        PRIMARY KEY("id_student" AUTOINCREMENT)
                                    )'''
            self.conn.execute(table_create_query)
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()

    # select all data in database
    def select_all_in_db(self):
        try:
            self.cursor.execute("SELECT * FROM student")
            fetchData = self.cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()
        
    # search data in database
    def search_in_db(self, query_string):
        try:
            query = "SELECT * FROM student WHERE firstName_student LIKE ? OR secondName_student LIKE ?"
            self.cursor.execute(query, (f'%{query_string}%', f'%{query_string}%'))
            fetchData = self.cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()

    # select one data in database
    def select_one_data_in_db(self, level):
        try:
            student_level = (level,)
            self.cursor.execute("SELECT * FROM student WHERE level_student = ?", student_level)
            fetchData = self.cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()
    
    # insert data in database
    def insert_row_in_db(self, data_tuple):
        try:
            data_insert_query = '''
                INSERT INTO student (
                    firstName_student, secondName_student, 
                    birthday_student, academicYear_student, 
                    level_student, comment_student) 
                VALUES (?, ?, ?, ?, ?, ?)'''
            
            self.cursor.execute(data_insert_query, data_tuple)
            self.connect.commit()
            return True
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()
        
    # update data in database
    def update_row_in_db(self, data_tuple):
        try:
            data_update_query = '''
                UPDATE student SET 
                firstName_student = ?,
                secondName_student = ?,
                birthday_student = ?,
                academicYear_student = ?,
                level_student = ?,
                comment_student = ?
                WHERE id_student = ?'''
                
            self.cursor.execute(data_update_query, data_tuple)
            self.connect.commit()
            return True
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()
          
    # delete data from database
    def delete_row_in_db(self, id_student):
        try:
            data_delete_query = '''
                DELETE FROM student 
                WHERE id_student = ?'''
                
            self.cursor.execute(data_delete_query, (id_student,))
            self.connect.commit()
            return True
        except Exception as e:
            print("[ERREUR]", e)
            self.connect.rollback()

    # close database
    def close_db(self):
        self.connect.close()
        
"""
mydt = db()

name = "OM"

datas = mydt.search_in_db(name)

for data in datas:
    print(data)
"""