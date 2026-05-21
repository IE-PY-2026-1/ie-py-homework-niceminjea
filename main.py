# 파일이름 :특급전사 판독기
# 작 성 자 :김민재
name = input('평가할 병사의 이름을 입력하시오:')

subjects = ['팔굽혀펴기','뜀걸음','사격','윗몸일으키기','정신전력']
grades = []
specialcount = 0

print(f'{name} 병사의 특급전사 판별 시작')

for i in range (len(subjects)):
    subject = subjects[i]
    score = int(input(f'{subject}점수를 입력하세요:'))

    if score < 0:
        print('음수이므로 오류입니다.')
        grades.append('미응시')
        continue

    if score > 100 :
        print('초과이므로 오류 입니다.')
        grades.append('미응시')
        continue

    if score > 100 :
        print('100점 초과는 오류입니다.')
        break

    if score >= 90:
        grade = '특급'
        specialcount += 1
    elif score >= 80:
        grade = '1급'
    elif score >= 70:
        grade = '2급'
    else:
        grade = '불합격'

    grades.append(grade)
    print(f'결과: {grade}')
if len(grades) == 5:
    if specialcount == 5:
        print(f'축하합니다 특급전사입니다')
        print(f'포상으로 2박3일 휴가 지급!')
    else:
        print(f'당신은 특급전사가 아닙니다.')
        print(f'특급전사가 되기 위한 목표')
        for j in range (5):
            if grades[j] != '특급':
                print(f'{subjects[j]} 종목에서 특급을 달성해야합니다.')
print(f'건강한 군생활 하십쇼 프로그램 종료.')