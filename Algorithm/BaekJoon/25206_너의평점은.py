import sys
input = sys.stdin.readline

subjects = [list(input().split()) for _ in range(20)]   # 과목명, 학점, 등급(과목평점)
grades = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
    'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

credit_sum = 0  # 학점 총합
sum_ = 0        # 학점 * 등급 합
for subject in subjects:
    if subject[2] != 'P':
        credit_sum += float(subject[1])
        sum_ += float(subject[1]) * grades[subject[2]]

print(sum_ / credit_sum)   # 학점 * 등급의 합을 학점의 총합으로 나누기