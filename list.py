hulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [hulsu, younghee, yong, minsu]

for student in students:
    total = 0
    for s in student:
        total += s
    avg = int(total / 3)
    print(avg)