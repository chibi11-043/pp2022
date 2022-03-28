studentList=[]
from itertools import count
#1. input number of students in a class
def CountStudents():
	count = int(input("How many students are there in the class ?"))
	return count

#2. input student information
#4. input course information
class Student:
    count = 0
    pass
    # initializer/object attributes
    def __init__(self,id,name,dob,courseID,courseName,mark):
        print("Enter your Student Information :")
        self.id = id
        self.name = name 
        self.dob = dob
        Student.count +=1
        #self.courseID = courseID
        #self.courseName = courseName 
        #self.mark = mark
        
    #def get_id(self,id)
    #    self.id=id
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
    id=input(f"Enter the student ID :")  
    name=input(f"Enter the student name :")
    dob=input(f"Enter the student dob :")
    print(f"Enter the Course Information :")
    courseID=input(f"Enter the Course ID :") 
    courseName=input(f"Enter the Course Name :")
    mark=input(f"Enter the mark :") 

    #main
    sv = Student(id,name,dob,courseID,courseName,mark)
    studentList.append(sv)


#3. input number of courses :
def NumberOfCourses() :
    NumberOfCourses = int(input("Enter number of courses : "))
    return NumberOfCourses


