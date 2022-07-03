class ArrayList:
	def __init__(self):
		self.addrList =  ["www.hufs.ac.kr"]	#히스토리를 관리하는 리스트
		self.real = ["www.hufs.ac.kr"] #실제 이동할 수 있는 페이지를 관리하는 리스트
		self.current = 0	#현재의 위치를 나타내기 위한 변수
		
	def size(self):	#현재 리스트에 들어있는 원소의 수
		return len(self.addrList)
	
	def insert(self, pos, e):
		if pos < 0 or pos > self.size():
			print("위치 error")
			return None
		else:
			self.addrList.insert(pos, e)

	def go(self, addr):
		self.addrList.insert(self.size(), addr)	#히스토리를 관리하는 리스트에 추가
		self.real.insert(self.current+1, addr)	#실제 이동할 수 있는 페이지에 추가
		self.current += 1
		self.real = self.real[:self.current+1]	#slicing으로 다음 페이지들을 무시
		print(self.real[self.current])
		
	def forward(self):
		if self.current != len(self.real)-1:	#현재 위치가 끝이 아닐때
			self.current+=1
			print(self.real[self.current])
			
	def backward(self):
		if self.current != 0:	#현재 위치가 처음이 아닐 때
			self.current-=1
			print(self.real[self.current])
			
	def history(self):
		self.addrList.reverse()
		result = dict.fromkeys(self.addrList)	#리스트의 각 원소를 key값으로 갖는 딕셔너리를 생성
		result = list(result)	#딕셔너리를 리스트로 변환(key)
		for i in range(len(result)):
			print(result[i])
			

browserList = ArrayList()
print(browserList.addrList[0])
while True:
	browser = [x for x in input().split()]
	
	if browser[0] == "quit":
		break
	elif browser[0] == "go":
		browserList.go(browser[1])
	elif browser[0] == "backward":
		browserList.backward()
	elif browser[0] == "forward":
		browserList.forward()
	elif browser[0] == "history":
		browserList.history()