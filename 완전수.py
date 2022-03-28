n = int(input())
count = 0  # 완전수의 개수
# 완전수를 판별하는 함수


def perfect(a):
    sum = 0
    for b in range(1, a):
        if a % b == 0:
            sum += b
    if a == sum:
        return True
    else: return False


for a in range(2, n+1):
    if perfect(a):
        count += 1

print(count)