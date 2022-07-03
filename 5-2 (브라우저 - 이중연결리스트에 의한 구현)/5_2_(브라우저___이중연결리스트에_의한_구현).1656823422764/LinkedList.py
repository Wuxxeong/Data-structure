class DNode:
	def __init__(self, e):
		self.data = e
		self.back = None
		self.next = None
		
class DLinkedList:
	def __init__(self):
		self.head = DNode("www.hufs.ac.kr")	#
		self.current = 0	#넣은 순서를 count 하는 변수
		
	def getNode(self, pos):
		if pos < 0:return None
		node = self.head
		while pos > 0 and node != None:
			node = node.next
			pos -= 1
		return node
	
	def getEntry(self, pos):	#pos번째 node에 있는 원소를 반환
		if pos < 0:return None
		node = self.head
		while pos > 0 and node != None:
			node = node.next
			pos -= 1
		return node.data
	
	def size(self):	#이중연결리스트의 사이즈를 구하는 함수
		count = 0
		now = self.head
		while now is not None:
			count += 1
			now = now.next
		return count
	
	def insert(self, pos, e):	#pos번째에 e값을 가지는 노드를 삽입하는 함수
		if pos < 0 or pos > self.size():
			return None
		else:
			location = self.getNode(pos)	
			node = DNode(e)
			node.next = location	#삽입하고 싶은 노드의 next는 pos번째에 있는 노드를 가리킴
			self.head = node	#go했을 때 뒤에 있는 나머지 주소들은 무시함을 위함
			location.back = node	

	def go(self, e):
		if self == browserList:	#실제 이동할 수 있는 리스트일때
			self.insert(self.size()-self.current-1, e)	#넣은 순서를 이용하여 pos를 나타내고 전달
			self.current+=1	
		elif self == historyList:	#history만 관리하는 리스트일때
			self.insert(0,e) #가장 첫번째에 삽입
			
	def forward(self):	#페이지를 다음 주소로 이동
		if self.size()-self.current-1 != 0:	#pos 가 0이 아닐때
			self.current +=1  #current가 1증가되면 pos는 1감소됨
			front = self.getNode(self.size()-self.current-1)
			print(front.data)
			
	def backward(self):	#페이지를 이전 주소로 이동
		if self.size()-self.current-1 != self.size()-1:	#pos가 마지막이 아닐때
			self.current -=1
			last = self.getNode(self.size()-self.current-1)
			print(last.data)
		
	def history(self):
		temp = []
		node = self.head
		while node != None:
			temp.append(node.data)	#비어있는 리스트에 노드의 모든 값들을 삽입
			node=node.next
		result = dict.fromkeys(temp)	#리스트의 각 원소를 key값으로 갖는 딕셔너리를 생성
		result = list(result)	#딕셔너리를 리스트로 변환(key)
		for i in range(len(result)):
			print(result[i])

	
browserList = DLinkedList() #실제 이동할 수 있는 페이지들
historyList = DLinkedList() #방문 기록을 모두 가지는 리스트

print(browserList.head.data)
while True:
	browser = [x for x in input().split()]
	if browser[0] == "quit":
		break
	elif browser[0] == "go":
		browserList.go(browser[1])
		historyList.go(browser[1])
		print(browser[1])
	elif browser[0] == "backward":
		browserList.backward()
	elif browser[0] == "forward":
		browserList.forward()
	elif browser[0] == "history":
		historyList.history()