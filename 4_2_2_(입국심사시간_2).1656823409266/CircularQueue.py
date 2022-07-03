class CircularQueue():
	MAX_QSIZE = 200

	def __init__(self):
		self.items = [None] * CircularQueue.MAX_QSIZE
		self.front = -1
		self.rear = -1
		self.size = 0

	def isEmpty(self):
		return self.size == 0

	def isFull(self):
		return self.size == len(self.items)

	def resize(self, n):
		olditems = self.items	#원래 가지고 있던 값을 다른 변수에 저장
		self.items = [None] * n
		paste = (self.front+1)%self.size 
		for i in range(self.size):
			self.items[i] = olditems[paste]	
			paste = (paste + 1) % self.size
		self.front = -1	#복사한 후 front와 rear를 초기화 해줌
		self.rear = self.size - 1

	def enqueue(self, e):
		if self.isFull():	#만약 큐에 원소가 다 차 있을때
			self.resize(2 * len(self.items))	#resize함수를 이용하여 사이즈를 두배로 늘림
		self.rear = (self.rear + 1) % len(self.items)
		self.items[self.rear] = e
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			print("Queue is Empty")
		else:
			self.front = (self.front + 1) % len(self.items)
			e = self.items[self.front]
			self.size -= 1
			return e
		
	def peek(self):	#가장 먼저 들어간 원소를 확인하는 함수
		return self.items[(self.front + 1)% len(self.items)]


def waiting(t, a):
	if t < a:
		return 0
	return t - a

#해당 입국심사대에 입국심사가 끝난 사람이 있는지 확인하고 시행하는 함수
def isdequeue(i, entrance, testTimeLinked):	
	arrive = arriveTimeSum + people[i][0]	#해당하는 사람의 도착시간
	while not entrance.isEmpty():
		test = testTimeLinked.peek()	#가장 앞에 있는 사람의 입국심사가 끝나는 시간 확인
		if arrive >= test:	#도착시간이 더 늦으면, 즉 심사가 끝나 있는 상황이면
			testTimeLinked.dequeue()
			entrance.dequeue()
		else: break

n = int(input())
people = []
for i in range(n):
	people.append([int(x) for x in input().split()])
	
	
arriveTimeSum = 0	#도착 시간의 합을 저장하는 변수

entrance1 = CircularQueue()	#첫번째 심사대를 관리하는 큐
testTimeSum1 = 0	#첫번째 심사대에서 심사가 끝나는 시간의 합을 저장
wait_sum1 = 0	#첫번째 심사대에서 사람들이 기다리는 시간의 합
	
entrance2 = CircularQueue()	#두번째 심사대를 관리하는 큐
testTimeSum2 = 0	#두번째 심사대에서 심사가 끝나는 시간의 합을 저장
wait_sum2 = 0	#두번째 심사대에서 사람들이 기다리는 시간의 합

testTimeLinked1 = CircularQueue() #n번째 사람이 입국심사가 끝나는 시간을 연결큐로 저장
testTimeLinked2 = CircularQueue()

for i in range(n):
	if entrance1.isEmpty():	#심사대 1이 비어있으면 enqueue
		entrance1.enqueue(people[i])
		
		arriveTimeSum += entrance1.items[entrance1.rear][0]
		testTimeSum1 += entrance1.items[entrance1.rear][1]
		
		testTimeLinked1.enqueue(testTimeSum1)
		
		wait_sum1 += 0
	elif entrance2.isEmpty():	#심사대 2 비어있으면 enqueue
		entrance2.enqueue(people[i])
		
		arriveTimeSum += entrance2.items[entrance2.rear][0]
		testTimeSum2 += entrance2.items[entrance2.rear][1] + arriveTimeSum	
		#심사 소요 시간에 도착시간을 더해줘야 심사가 끝나는 시간을 알 수 있음
		testTimeLinked2.enqueue(testTimeSum1)
		
		wait_sum2 += 0
	else:
		#101 line: 전 사람까지의 심사 소요 시간의 합과 enqueue하기 전 사람의 도착시간을 매개변수로 기다리는 시간 계산 후 비교
		if waiting(testTimeSum1, arriveTimeSum + people[i][0]) < waiting(testTimeSum2, arriveTimeSum + people[i][0]):
			isdequeue(i,entrance1, testTimeLinked1)	#해당하는 사람, 입국심사대, 각 사람의 심사소요시간을 매개로 dequeue해야되는지 확인
			
			entrance1.enqueue(people[i])	#조건문에서 심사대1이 걸리는 시간이 적을때 해당 심사대로 줄 세우기
			
			arriveTimeSum += entrance1.items[entrance1.rear][0]
			
			wait = waiting(testTimeSum1, arriveTimeSum)
			if wait == 0:	#기다리는 시간이 0이면
				testTimeSum1 += arriveTimeSum - testTimeSum1	#차이만큼 소요시간에 더해줌
			wait_sum1 += wait
			
			testTimeSum1 += entrance1.items[entrance1.rear][1]
			testTimeLinked1.enqueue(testTimeSum1)
			
		else:	#심사대 2의 대기시간이 더 짧을때 위와 같은 방식으로 구현
			isdequeue(i,entrance2,testTimeLinked2)
			
			entrance2.enqueue(people[i])
			
			arriveTimeSum += entrance2.items[entrance2.rear][0]
			
			wait = waiting(testTimeSum2, arriveTimeSum)
			if wait == 0:
				testTimeSum2 += arriveTimeSum - testTimeSum2
			wait_sum2 += wait
			
			testTimeSum2 += entrance2.items[entrance2.rear][1]
			testTimeLinked2.enqueue(testTimeSum2)

print(f'{(wait_sum1 + wait_sum2)/n:.2f}')	#소수점 셋째자리에서 반올림

