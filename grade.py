score = float(input())
if score >= 90:
    grade = "优"
elif score >= 80:
    grade = "良"
elif score >= 70:
    grade = "中"
elif score >= 60:
    grade = "及格" 
else:
    grade = "不及格"
print(f"你的成绩是{score},  属于{grade}")