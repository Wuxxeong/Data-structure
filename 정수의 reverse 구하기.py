n = int(input())
countAll = 0 #전체 자릿수
temp = n #n의 값을 유지해야하므로 temp에 임시 저장
#전체 자리수 countAll을 구하는 과정
while temp != 0:
	countAll += 1
	temp = temp // 10

reverse = 0 
i = 1
while n != 0:
	reverse += (n % 10) * (10**(countAll-i)) 
	n = n // 10
	i = i+1
print(reverse)