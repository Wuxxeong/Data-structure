class Student:
	def __init__(self, st_no, name, dept, grade, score=None):
		self.st_no = st_no	#학번
		self.name = name	#이름
		self.dept = dept	#학과
		self.grade = grade	#학년
		self.score = score	#성적
		
class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right
		
class Course:
	def __init__(self):
		self.root = None
		self.dept_cnt = 0	#해당 학과의 학생들의 수
		self.dept_list = []	#해당 학과의 학생들을 관리하는 리스트
	#========================단말 노드의 수==========================
	def size(self):
		return self._subtreeSize(self.root)
	
	def _subtreeSize(self, p):
		if p is None:
			return 0
		else:
			return 1 + self._subtreeSize(p.left) + self._subtreeSize(p.right)
	
	
	def printInorder(self):	#전체 학생들 출력을 위한 중위 순회
		self._subtreeInorder(self.root)
		
	def _subtreeInorder(self, p):
		if p is not None:
			self._subtreeInorder(p.left)
			if p.key.score == None:	#학점 입력을 하지 않은 경우 학년까지만 출력
				print(p.key.st_no, p.key.name,p.key.dept,p.key.grade)
			else:	#학점 입력이 되어있을 경우 학점까지 출력
				print(p.key.st_no, p.key.name,p.key.dept,p.key.grade,p.key.score)
			self._subtreeInorder(p.right)
	
	
	
	def inorder_dept(self, dept):	#해당 학과의 학생들만 출력하기 위한 중위 순회
		self._subtreeInorderDept(self.root, dept)
		
	def _subtreeInorderDept(self, p, dept):
		if p is not None:
			self._subtreeInorderDept(p.left, dept)
			if p.key.dept == dept:	#현재 단말 노드에 있는 학생의 학과와 일치하면
				self.dept_cnt += 1	#학생의 수 +1
				self.dept_list.append(p.key)	#학생을 리스트에 넣어줌
			self._subtreeInorderDept(p.right, dept)

	#========================삽입 연산================================
	def insert(self, key):
		self.root = self._insertSubtree(self.root, key)

	def _insertSubtree(self, node, key):
		if node == None:	#아무것도 없을 때 그 위치에 삽입
			return Node(key)
		elif key.st_no < node.key.st_no:	#학번이 더 적으면 왼쪽 트리로 이동
			node.left = self._insertSubtree(node.left, key)
		elif key.st_no > node.key.st_no:	#학번이 더 크면 오른쪽 트리로 이동
			node.right = self._insertSubtree(node.right, key)
		elif key.st_no == node.key.st_no:	#해당학번이 수강신청을 하였을 경우 에러 출력
			print("error1")
			return node
		return node
	#========================삭제 연산================================
	def _minNode(self, node):	#가장 왼쪽에 있는 노드를 반환하는 함수
		if node.left == None:
			return node
		else:
			return self._minNode(node.left)	

	def delete(self, key):
		self.root = self._deleteNode(self.root, key)
		
	def _deleteNode(self, node, key):
		if node == None:	#해당 노드가 없으면 에러를 출력
			print("error2")
			return None
		if key < node.key.st_no:	#찾고 있는 학번이 더 작을 경우 왼쪽 트리로 이동
			node.left = self._deleteNode(node.left, key)
			return node
		elif key > node.key.st_no:	#찾고 있는 학번이 더 클 경우 오른쪽 트리로 이동
			node.right = self._deleteNode(node.right, key)
			return node
		else:	#node가 삭제할 키의 노드인 경우
			if node.right == None:	#node의 오른쪽 자식노드가 없을 경우
				return node.left
			if node.left == None:	#node의 왼쪽 자식노드가 없을 경우
				return node.right
			
			rightMinNode = self._minNode(node.right)	#node의 오른쪽 부트리에서 최소키의 노드를 찾음
			node.key = rightMinNode.key	#node의 오른쪽 부트리에서 최소키의 노드를 node에 복사
			node.right = self._deleteNode(node.right, rightMinNode.key.st_no) #노드의 오른쪽 부트리에서 최소키의 노드를 삭제
			return node


	def search_st_no(self, key):	#해당 학번의 학생의 객체를 반환하는 함수
		node = self.root
		while node is not None:
			if key == node.key.st_no:
				return node.key
			elif key < node.key.st_no:
				node = node.left
			else:
				node = node.right
		return None
	
	def register(self, st_no, name, dept, grade):	#수강신청(N) 학번, 이름, 학과, 학년
		st = Student(st_no, name, dept, grade)	#학생의 정보를 저장한 객체를 생성하고 삽입함
		self.insert(st)
	
	def Score(self, st_no, score):	#성적 수정(G)
		result = self.search_st_no(st_no)	#해당 학번의 학생의 객체를 받아옴
		if result == None:	#객체가 존재하지 않을 경우 에러 출력
			print("error2")
		else:	#객체가 존재하면 그 학생의 학점을 수정
			result.score = score

	def withdraw(self, st_no):	#수강 취소(C)
		self.delete(st_no)
	
	def find(self, st_no):	#정보 출력(R)
		result = self.search_st_no(st_no)	#해당 학번의 학생의 객체를 받아옴
		if result == None:	#객체가 존재하지 않을 경우 에러 출력
			print("error2")
		else:	#객체가 존재할 경우
			if result.score == None:	#학점에 대한 정보가 없을 경우
				print(result.st_no, result.name, result.dept, result.grade)
			else:	#학점에 대한 정보가 있을 경우
				print(result.st_no, result.name, result.dept, result.grade, result.score)

	def printDept(self, dept):	#학과의 수강 학생수, 학생의 정보 출력(D)
		self.inorder_dept(dept)
		print(self.dept_cnt)	#학과의 수강 학생수 출력
		
		no_list = []	#해당 학과를 수강하는 학생들의 학번을 관리하는 리스트
		for i in range(len(self.dept_list)):
			no_list.append(self.dept_list[i].st_no)	#리스트에 있는 student객체의 학번을 추가
		no_list.sort()	#오름차순으로 정렬 후
		
		for i in range(len(self.dept_list)):
			self.find(no_list[i])	#학번에 해당하는 정보 출력
			
		self.dept_cnt = 0	#해당 학과에 대한 정보들 초기화(여러번 호출 될 수 있기 때문)
		self.dept_list = []

	def printList(self):	#수강생 전체 수 및 정보 출력(P)
		print(self.size())	
		self.printInorder()


course = Course()
while True:
	command = input().split()
	if command[0] == 'N':	#수강신청
		course.register(command[1], command[2], command[3], command[4])
	elif command[0] == 'G':	#학번, 성적
		course.Score(command[1], command[2])
	elif command[0] == 'C':	#수강 취소
		course.withdraw(command[1])
	elif command[0] == 'R':	#학번 학생 조회
		course.find(command[1])
	elif command[0] == 'D':	#학과 학생
		course.printDept(command[1])
	elif command[0] == 'P':	#수강학생 수 출력, 학생 정보 출력
		course.printList()
	elif command[0] == 'Q':
		break
