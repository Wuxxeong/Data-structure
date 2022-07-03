class Node():
	def __init__(self, e):
		self.data = e
		self.link = None

class LinkedStack():
	def __init__(self):
		self.top = None
		
	def isEmpty(self):
		return self.top == None
	
	def push (self, e):
		newNode = Node(e)
		newNode.link = self.top	#top이 참조하고 있던 것을 새로운 노드의 링크가 참조하게끔 함
		self.top = newNode	#top은 새로운 노드를 참조하게 함
		
	def pop(self):
		try:
			element = self.top.data	#top이 참조하고 있는 노드의 데이터
			self.top = self.top.link #top의 link가 참조하고 있는 것(뒤에서 두번째로 들어온 노드)을 top이 참조
			return element
		except IndexError:
			print("Stack is Empty")
			

def cal(postfix_List):	#매개변수를 스트링으로 받음
	op = LinkedStack()
	i = 0 
	c = postfix_List[0] #첫번째 스트링
	while c != ';' :	#;가 나오기 전까지 loop을 실행
		if c in ('+', '-', '*', '//', '%'):	#만약 문자가 연산자일때
			if not op.isEmpty():	#숫자 있을 때 꺼내서 2번째 피연산자로 지정
				op2 = op.pop()
				if not op.isEmpty():
					op1 = op.pop()	#첫번째 피연산자로 지정
					if c == '+':
						tmp_result = op1 + op2
						op.push(tmp_result)	
					elif c == '-':
						tmp_result = op1 - op2
						op.push(tmp_result)
					elif c == '*':
						tmp_result = op1 * op2
						op.push(tmp_result)
					elif c == '//':
						tmp_result = op1 // op2
						op.push(tmp_result)
					elif c == '%':
						tmp_result = op1 % op2
						op.push(tmp_result)
			#연산자 1개당 피연산자가 2개가 아닐 때 0을 반환하면서 종료
				else:
					return 0
			else:
				return 0
		else:	#문자가 숫자일때
			c = int(c) #int로 바꾸고
			op.push(c) #피연산자를 저장하는 linkedStack에 저장
		i += 1
		c = postfix_List[i] #다음 문자를 지정
	return op	#계산 결과를 갖고 있는 스택을 반환

postfix = input().split()

if cal(postfix) == 0:
	print("error")
else:
	result = LinkedStack()
	result = cal(postfix)
	r = result.pop()
	if not result.isEmpty():	#스택을 pop하고 난 후 다른 피연산자가 남아있으면 에러
		print("error")
	else:
		print(r) #스택을 pop하고 남아있는 피연산자가 없으면 pop한것이 결과 이므로 출력
	
	