yy1, yy2 = input().split()
day = input()
yy1, yy2 = int(yy1), int(yy2)
dayList = ["일", "월", "화", "수", "목", "금", "토"]
allDay = 0  # yy1년 1월1일부터 yy2년 1월 1일 사이의 날 수

# 년도가 윤년인지 판별하는 함수
def leap(yy):
    if yy % 400 == 0:
        isLeap = True
    elif yy % 100 == 0:
        isLeap = False
    elif yy % 4 == 0:
        isLeap = True
    else:
        isLeap = False
    return isLeap

	
# yy1년부터 yy2년 까지의 날 수
for yy in range(yy1, yy2):
    if leap(yy):
        allDay += 1
    allDay += 365

dayDiff = allDay % 7  # 입력한 요일로부터 며칠 차이는지 계산
# 입력한 요일의 인덱스를 찾고 요일 차이만큼 더한다음 7로나눈 나머지가yy2년 1월 1일에 해당하는 인덱스임
yy2Index = (dayList.index(day) + dayDiff) % 7
print(dayList[yy2Index])
