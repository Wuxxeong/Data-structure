class Student:
	def __init__(self, st_no, name):
		self.st_no = st_no
		self.name = name
	
class Course:
	def __init__(self):
		self.st_list = []	#학생들의 정보를 관리하는 리스트
	
	def register(self, st_no, name):	#수강신청(N)
		st = Student(st_no, name)
		self.st_list.append(st)	#학생을 추가해줌
	
	def withdraw(self, st_no):	#수강 취소(C)
		for i in range(len(self.st_list)):
			if self.st_list[i].st_no == st_no:	#해당 학번의 학생을 찾았을 경우
				self.st_list.pop(i)	#학생을 삭제
				break
	
	def find(self, st_no):	#정보 출력(R)
		for i in range(len(self.st_list)):
			if self.st_list[i].st_no == st_no:	#학생 정보가 일치할 때 
				print(self.st_list[i].st_no, self.st_list[i].name) #학번과 이름 출력
				break

	def printList(self):	#수강생 정보 출력(P)
		print(len(self.st_list))
		no_list = []	#학생의 학번만 관리하는 리스트
		for i in range(len(self.st_list)):	
			no_list.append(self.st_list[i].st_no)
		no_list.sort()
		for i in range(len(self.st_list)):
			self.find(no_list[i])

course = Course()
while True:
	command = input().split()
	if command[0] == 'N':
		course.register(command[1], command[2])
	elif command[0] == 'C':
		course.withdraw(command[1])
	elif command[0] == 'R':
		course.find(command[1])
	elif command[0] == 'P':
		course.printList()
	elif command[0] == 'Q':
		break