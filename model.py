import sqlite3

class DB():
    def __init__(self):
        self.database = "db_student.db"
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.database)
        
    # Create table if not exist
    def create_table(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
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
            cursor.execute(table_create_query)
            self.connection.commit()
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()

    # select all data in database
    def select_all_in_db(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM student")
            fetchData = cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()
        
    # search data in database
    def search_in_db(self, query_string):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM student WHERE firstName_student LIKE ? OR secondName_student LIKE ? OR birthday_student LIKE ? OR academicYear_student LIKE ? OR level_student LIKE ?"
            cursor.execute(query, (f'%{query_string}%', f'%{query_string}%', f'%{query_string}%', f'%{query_string}%', f'%{query_string}%'))
            fetchData = cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()
        
    # search data in database
    def search_in_db_advanced(self, data_tuple):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM student WHERE academicYear_student = ? AND level_student = ?"
            cursor.execute(query, data_tuple)
            fetchData = cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()

    # select one data in database
    def select_one_data_in_db(self, level):
        try:
            self.connect()
            cursor = self.connection.cursor()
            student_level = (level,)
            cursor.execute("SELECT * FROM student WHERE level_student = ?", student_level)
            fetchData = cursor.fetchall()
            return fetchData
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()
    
    # insert data in database
    def add_student(self, data_tuple):
        try:
            self.connect()
            cursor = self.connection.cursor()
            data_insert_query = '''
                INSERT INTO student (
                    firstName_student, secondName_student, 
                    birthday_student, academicYear_student, 
                    level_student, comment_student, semOne_student, semTwo_student, general_student) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
            cursor.execute(data_insert_query, data_tuple)
            self.connection.commit()
            return True
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()
        
    # update data in database
    def update_row_in_db(self, data_tuple):
        try:
            self.connect()
            cursor = self.connection.cursor()
            data_update_query = '''
                UPDATE student SET
                semOne_student = ?,
                semTwo_student = ?,
                general_student = ?,
                comment_student = ?
                WHERE id_student = ?'''
            cursor.execute(data_update_query, data_tuple)
            self.connection.commit()
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()
          
    # delete data from database
    def delete_row_in_db(self, id_student):
        try:
            self.connect()
            cursor = self.connection.cursor()
            data_delete_query = '''
                DELETE FROM student 
                WHERE id_student = ?'''
                
            cursor.execute(data_delete_query, (id_student,))
            self.connection.commit()
            
        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.close_db()

    # close database
    def close_db(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
        
