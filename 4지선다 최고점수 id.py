ans = [int(x) for x in input().split()]
score = [int(x) for x in input().split()]
n = int(input())
put = []

# 2차원 리스트로 리스트안의 리스트에 id 와 제출한 답안을 차례대로 입력함
for i in range(n):
    put.append([int(x) for x in input().split()])

# 제출한 답안이 정답과 일치하는지를 알아보는 함수
def correct(i, j):
    if ans[j] == put[i][j+1]:
        return True
    return False


# 점수를 계산하는 과정
sumList = []  # 점수를 순서대로 모아놓은 리스트
for i in range(n):
    sum = 0
    for j in range(len(ans)):
        if correct(i, j):
            sum += score[j]
    sumList.append(sum)

# sumList에서 최고점을 가진 index들과 그들의 점수를 알아내기
maxIndex = 0
max = sumList[0]
for x in range(len(sumList)):
    if max <= sumList[x]:
        maxIndex = x
        max = sumList[x]

# 최고점을 가지는 index 리스트
max_index_list = []

for x in range(len(sumList)):
    if max == sumList[x]:
        max_index_list.append(x)

# 최고점을 가지는 id들을 따로 리스트로 만든 후 정렬
id = []
for x in range(len(max_index_list)):
    id.append(put[max_index_list[x]][0])  # put 리스트에서 id는 각각 0번째 index에 있음을 이용
id.sort()

print(max)
for x in range(len(id)):
    print(id[x], end=' ')