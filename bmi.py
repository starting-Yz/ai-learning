height = float(input())
weight = float(input())
bmi = weight / (height ** 2)
if bmi < 18.5:
    level = "偏瘦"
elif bmi < 24:
    level = "正常"
else:
    level = "偏胖"
print(f"你的 BMI 是{bmi:.1f},  属于{level}")
