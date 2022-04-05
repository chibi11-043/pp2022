#include "StudentInformation"
#include "CourseInformation"

studentList=[]
from itertools import count
#1. input number of students in a class
def CountStudents():
	count = int(input("How many students are there in the class ?"))
	return count

#2. input student information
class Student:
    count = 0
    pass
    # initializer/object attributes
    def __init__(self,id,name,dob):
        print("Enter your Student Information :")
        self.id=id  
        self.name=name
        self.dob=dob
        Student.count +=1
        A = {'id' : id, 'name' : name, 'dob' : dob}
        Student.append(A)
        
    #id
    def get_id(self):
        return self.id
    #name
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    #dob
    def set_dob(self,dob):
        self.dob = dob
    def get_dob(self):
        return self.dob
    
#3. input number of courses :
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses

#4. input courses information :
class Course :
    count = 0
    pass
    def __init__(self,courseID,courseName,mark):
        self. courseID=courseID 
        self.courseName=courseName
        self.mark=mark
        Course.count +=1
        B = {"id":courseID,"name":courseName,"mark":mark}
        Course.append(B)
    #courseID
    def set_courseID(self,courseID):
        self.courseID = courseID
    def get_courseID(self):
        return self.courseID
    #courseName
    def set_courseName(self,courseName):
        self.courseName = courseName
    def get_courseName(self):
        return self.courseName
    #mark
    def set_mark(self,mark):
        self.mark = mark
    def get_mark(self):
        return self.mark

#5.Select a course , input marks for student in this course

        

class test_oop:
    Students = []
    Courses = []
    
    def listStudent (self) :
        print(Student)

    def listCourse (self) :
        print(Course)
    
    
    def start (self):  
        A = int(input('How many student are there in the course : '))
        for i in range (A) :
            self.id=input(f"Enter the student ID :")  
            self.name=input(f"Enter the student name :")
            self.dob=input(f"Enter the student dob :")
            temp_Student = Student(self.id,self.name,self.dob)
            
            
        B = int(input('Enter number of courses :'))
        for y in range (B):
            courseID = input("Enter the course id : ")
            courseName = input("Enter the course name : ")
            mark = input("Enter the mark of course :")
            temp_Course = Course(self,courseID,courseName,mark)
        
    

if __name__ == '__main__':
    t = test_oop()
    t.start()
    
