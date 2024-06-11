student_marks = {"Krishna": [67, 68, 69],
                 "Arjun": [70, 98, 63],
                 "Malika": [25, 26.5, 28]}

def calculate(data, name):
	notes = 0
	turn = 0
	for key, value in data.items():
		if key == name:
			for i in data[name]:
				turn += 1
				notes += i
	print(f"{(notes / turn):.2f}")

calculate(student_marks, "Malika")