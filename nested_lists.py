if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
sorted_keys = sorted(students)
new_students = {key: students[key] for key in sorted_keys}

grade = []
for key, value in new_students.items():
  grade.append(value)
min_number = min(grade)

while min_number in grade:
  grade.remove(min_number)
  
for key, value in new_students.items():
  if value == min(grade):
    print(key)