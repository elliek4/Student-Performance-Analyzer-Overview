# Name: Ellie Khoo
# Period: AM
# Student Performance Analyzer

# Program introduction
print()
print("================================================")
print("          STUDENT PERFORMANCE ANALYZER          ")
print("================================================")
print()

# get user information through asking and input
name = input("What is the student's name? ")
grade_level = float(input("What grade are you in? "))
assignment_average = float(input("What is your assignment average? "))
quiz_average = float(input("What is your quiz average? "))
test_average = float(input("What is your test average? "))
attendance_percent = float(input("What is your attendance percentage? "))
missing_assignments = int(input("How many missing assignments do you have? "))

# create function to calculate overall grade
def calculate_grade(assignment, quiz, test):
    grade = (assignment * 0.3) + (quiz * 0.3) + (test * 0.4) #calculates all the portions by adding them together
    return grade
overall_grade = calculate_grade(assignment_average, quiz_average, test_average) #result of calculating portions is stored in variable

# create function to determine student's letter grade
def letter_grade(overall_grade): # checks in which letter grade the student's overall grade lands and returns the letter grade
    if overall_grade >= 90:
        return "A" 
    elif overall_grade >= 80:
        return "B"
    elif overall_grade >= 70:
        return "C"
    elif overall_grade >= 60:
        return "D"
    else:
        return "F"

# create function to determine student's attendance status
def attendance_status(attendance): # checks what kind of attendance the student has and returns the quality of their attendance percentage
    if attendance >= 95:
        return "Excellent Attendance"
    elif attendance >= 90:
        return "Good Attendance"
    elif attendance >= 80:
        return "Attendance Warning"
    else:
        return "Poor Attendance"

# create function to determine student's assignment status
def assignment_status(missing_assignments): # checks the amount of assignments the student and returns the status of the amount
    if missing_assignments >= 5:
        return "Critical"
    elif missing_assignments >= 3:
        return "Warning"
    elif missing_assignments >= 1:
        return "Good" 
    else:
        return "Excellent"

# create function to check academic eligibility
# uses nested conditional to check if student's grade, attendance, and missing assignments determine whether the student has academic eligibilty
# returns if student qualifies and the reason why
def check_eligibility(overall_grade, attendance, missing_assignments): 
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligbility: ELIGIBLE")
                print("Reason: Student passed all three requirements")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low")
    else:
        print("Academic Eligbility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

# create function to check if student qualifies for high honors
# uses nested conditional to check if student's grade, attendance and missing assignments allow them to qualify for high honors
# returns if student qualifies and the reason why
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

# create function to check if student is in good standing
# uses conditional to check student's overall grade and attendance
# returns whether the student's grade and attendance qualify for good standing or not
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        return "YES"
    else:
        return "NO"

# create function to check if student should receive additional academic support
# uses conditional to check student's grade and attendance 
# returns whether student's grade and attendance suggest need for additional support
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        return "RECOMMENDED"
    else:
        return "NOT NEEDED"

# login simulator
print()
username = input("Enter username: ") # asks user for username and PIN
pin = int(input("Enter PIN: "))
print()
# displays whether login was successful using nested conditional to check if username and PIN are correct
if username == "student":
    if pin == 1234:
        print("Login Successful!")
    else:
        print("Login Failed: Incorrect PIN.")
else:
    print("Login Failed: Incorrect username.")
print()

# create function to display message depending on grade level
# uses conditional to check what grade the student is in
# displays message depending on grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        return "Welcome to your freshman year!"
    elif grade_level == 10:
        return "Keep building your skills!"
    elif grade_level == 11:
        return "Junior year - keep pushing!"
    elif grade_level == 12:
        return "Senior year - finish strong!"
    else:
        return "Invalid grade level."

# create function to determine which category has the student's highest score
# uses conditional to check which category is highest, returns the category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average and assignment_average >= test_average:
        return "Assignments"
    elif quiz_average >= assignment_average and quiz_average >= test_average:
        return "Quizzes"
    else:
        return "Tests"

# create function to check if student has advanced status
# uses conditional to check student's grade and attendance or grade and missing assignments
# returns student's status
def check_advanced_status(overall_grade, attendance, assignments):
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and assignments == 0):
        return "OUTSTANDING STUDENT"
    else:
        return "STANDARD STUDENT STATUS"

# displays final student summary by printing and calling functions
print()
print("========================================================")
print("                     STUDENT SUMMARY                    ")
print("========================================================")
print()
print(grade_level_message(grade_level))
print()
print("Student:", name)
print("Grade Level:",grade_level)
print()
print("Strongest Category:", strongest_category(assignment_average, quiz_average, test_average))
print()
print("Assignment Average:", assignment_average)
print("Quiz Average:", quiz_average)
print("Test Average:", test_average)
print()
print("Overall Grade:", overall_grade)
print("Letter Grade:", letter_grade(overall_grade))
print()
print("Attendance:", attendance_percent)
print("Attendance Status:", attendance_status(attendance_percent))
print()
print("Missing Assignments:", missing_assignments)
print("Missing Assignment Status:", assignment_status(missing_assignments))
print()
check_eligibility(overall_grade, attendance_percent, missing_assignments)
print()
check_high_honors(overall_grade, attendance_percent, missing_assignments)
print()
print("Good Standing:", check_good_standing(overall_grade, attendance_percent))
print("Additional Support:", check_support(overall_grade, attendance_percent))
print()
print("Advanced Status:", check_advanced_status(overall_grade, attendance_percent, missing_assignments))
print()
print("======================================================")