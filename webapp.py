from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.get_all_grades_for_one_student(student_github)
    print "GRADES TO FOLLOW..."
    print grades
    print row
    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2],
                                                grades=grades)
    return html

@app.route("/all_grades")
def get_students_and_grades_by_project_name():
	hackbright_app.connect_to_db()
	student_project = request.args.get("project")
	row = hackbright_app.get_students_and_grades_by_project_name(student_project)
	#grades = hackbright_app.get_students_and_grades_by_project_name(student_project)
	html = render_template("project_info.html", student_grades=row,
												project=student_project)

	return html

if __name__ == "__main__":
    app.run(debug=True)



