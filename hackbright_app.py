import sqlite3

DB = None
CONN = None

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()


def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    
    return "Successfully added student: %s %s" % (first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    return "Successfully added project: %s" % title

def make_new_grade(title, description, max_grade):
    query = """INSERT into Grades values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))

    CONN.commit()
    return "Successfully added grade: %d" % max_grade

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row
    

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    return row
    
   
def get_grade_from_grades(max_grade):
    query = """SELECT title, description, max_grade FROM Grades WHERE max_grade = ?"""
    DB.execute(query, (max_grade,))
    row = DB.fetchone()
    return row

def get_all_grades_for_one_student(title):
    query = """SELECT title, description, max_grade FROM Grades WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchall()
    return row

def get_students_and_grades_by_project_name(description):
    query = """SELECT title, description, max_grade FROM Grades WHERE description = ?"""
    DB.execute(query, (description,))
    row = DB.fetchall()
    return row

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("Your Python App That Accesses The Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            print get_student_by_github(*args) 
        elif command == "new_student":
            print make_new_student(*args)
        elif command == "project":
            print get_project_by_title(*args)
        elif command == "new_project":
            print make_new_project(*args)
        elif command == "max_grade":
            print get_grade_from_grades(*args)
        elif command == "make_new_grade":
            print make_new_grade(*args)
        elif command == "get_grades":
            print get_all_grades_for_one_student(*args)
        elif command == "project_name":
            print get_students_and_grades_by_project_name(*args)


    CONN.close()

if __name__ == "__main__":
    main()