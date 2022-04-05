import student_oop
from student_oop import Student
from student_oop import Course

#1. input number of students in a class
def CountStudents():
	count = int(input("How many students are there in the class ?"))
	return count

#3. input number of courses :
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses

list_system = []
while True :
    print(f'''\n
    0.close tab
    1.number of student
    2.add student information
    3.delete student information
    4.number of course
    5.add student course
    6.delete student course
    ''')
    select = input("Enter your choice : ")

    if str(select).isdigit():
        select = int(select)
        if select == 0 :
            break
        elif select == 1:
            CountStudents()
        
        elif select == 2 :
            id = input("Enter the student ID:")
            name = input("Enter the student name :")
            dob = input("Enter the student dob :")
            st = Student(id,name,dob)
            list_system.append(st)

        elif select == 3 :
            id = input("Enter the student ID must change : ")
            for i in list_system:
                if i.get_id() == id:
                    i.set_name(input("Enter the new student name : "))
                    i.set_dob(input("Enter the new student dob : "))
                    i.StudentInformation()

        elif select == 4 :
            NumberOfCourses()

        elif select == 5 :
            courseID = input("Enter the Course ID : ")
            courseName = input("Enter the course name : ")
            mark = input("Enter the mark : ")
            course = Course(courseID,courseName,mark)
            list_system.append(course)

        elif select == 6 :
            courseID = input("Enter the course ID must change : ")
            for i in list_system:
                if i.set_courseID() == courseID:
                    i.set_courseName("Enter the new course name : ")
                    i.set_mark("Enter the new course mark")
                    i.CourseInformation()
    else:
        print("You must enter a number . Please enter again !")



    

