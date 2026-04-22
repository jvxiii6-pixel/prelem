#Mark Castillano Prelem
#BSIT 2-4           

def get_Letter_grade(grade):
    if grade >= 90 :
        return "A"
    elif grade >= 80 :
        return "B"
    elif  grade >= 75 :
        return "C"
    else:
        return "D"



def get_check_grade(grade):
    if grade > 75 :
        return "Passed"
    else:
        return "Failed"

def save_student_record(first_name, last_name, grade, letter_grade, status):
    with open('C:\\Castillano_Prelem\\gradedata.txt', 'a') as file:
        file.write(f"First name: {first_name} | last name: {last_name} | grade: {grade} | letter_grade: {letter_grade} | status: {status} |\n")

while True:
    first_name = input("enter the student's first name: ")
    last_name = input("enter the student's last name: ")
    grade = int(input("enter the student's grade: " ))

    letter_grade = get_Letter_grade(grade)
    status = get_check_grade(grade)

    print("Letter Grade: " + letter_grade)
    print("Status: " + status)

    save_student_record(first_name, last_name, grade, letter_grade, status)
    print("record saved successfully!\n")

    choice = input("do you want to add another student? (yes or no):  ").lower()
    if choice != "yes":
        print(" all student record have been saved. goodbye!!")
        break
