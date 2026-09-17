# Name: Ellie Khoo
# Period: AM
# Student Performance Analyzer

# Program introduction
print()
print("================================================")
print("          STUDENT PERFORMANCE ANALYZER          ")
print("================================================")
print()

# get user information throught asking and input
name = input("What is the student's name? ")
grade_level = float(input("What grade are you in? "))
assignment_avg = float(input("What is your assignment average? "))
quiz_avg = float(input("What is your quiz average? "))
test_avg = float(input("What is your test average? "))
attendance_percent = float(input("What is your attendance percentage? "))
missing_assignments = int(input("How many missing assignments do you have? "))
print()

# create funcgtion to calculate overall grade
def calculate_grade(assignment, quiz, test):
    grade = (assignment * 0.3) + (quiz * 0.3) + (test * 0.4) #calculates all the portions by adding them together
    return grade
overall_grade = calculate_grade(assignment_avg, quiz_avg, test_avg) #result of calculating portions is stored in variable
print("Overall Grade:", overall_grade)

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
print("Letter Grade:", letter_grade(overall_grade))
print()

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
print("Attendance Status:", attendance_status(attendance_percent))

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
print("Missing Assignment Status:", assignment_status(missing_assignments))
print()

# create function to check academic eligibility
# checks if student's grade, attendance, and missing assignments to determine whether the student has academic eligibilty
# returns if they do and the reason why
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
print()

