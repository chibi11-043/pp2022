def CountStudents():
	count = int(input("How many students are there in the course ?"))
	return count

def Studentin4():
	print("Enter Student Infor : ")
	id = input(" ID : ")
	name = input(" Name : ")
	Birthday = input(" Birthday : ")
	A = {"id":id,"name":name,"birthday":Birthday}
	return A
def Students_List(Students):
	for A in Students:
		print(f"id {A['id']},name is {A['name']},birthday is {A['birthday']} ")



# main 
Students = []
count = CountStudents()
for i in range(0,count):
	A = Studentin4()
	Students += [ A ] 



def CountCourse():
	count = int(input("How many course are there in the semester ?"))
	return count

def Coursein4():
	print("Enter Course Infor : ")
	id = input(" ID : ")
	name = input(" Name : ")
	B = {"id":id,"name":name}
	return B
def Courses_List(Courses):
	for B in Courses:
		print(f"id {B['id']},name is {B['name']} ")



# main 
Courses = []
count = CountCourse()
for i in range(0,count):
	B =  Coursein4()
	Courses += [ B ] 




print("All Students:")
Students_List(Students)
print("All Courses:")
Courses_List(Courses)