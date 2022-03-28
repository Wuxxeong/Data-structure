#매개변수로 받은 문자열이 회문인지 판단하는 함수
def isPal(L):
    for i in range(len(L) // 2):
        if L[i] != L[len(L) - i - 1]:
            return False
    return True

lit = input()
lit = lit.lower()
pal_list = [] #가장 긴 회문을 저장하는 리스트

#길이가 가장 긴것부터 내림차순으로 해당하는 길이에 회문이 있는지 판별
for l in range(len(lit), 0, -1):
    for start in range(len(lit) - l + 1):	#해당하는 길이의 모든 문자를 모두 탐색 
        if isPal(lit[start : l + start]):
            if lit[start : l + start] not in pal_list:	#회문이 중복되는 것을 방지하기 위함 
                pal_list.append(lit[start : l + start])
    if pal_list:	#만약 회문이 있어서 lit_list에 원소가 있다면 정렬하고 loop을 빠져나옴
        pal_list.sort()
        break

for x in range(len(pal_list)):
    print(pal_list[x], end=' ')
