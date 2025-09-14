def calculate_average(marks):
    return sum(marks) / len(marks)

num_students = int(input("Enter number of students: "))
students = {}

for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    marks_input = input("Enter marks : ")
    marks = [int(x.strip()) for x in marks_input.split(",") if x.strip().isdigit()]
    students[name] = marks

average_marks = {}
for name, marks in students.items():
    avg = calculate_average(marks)
    average_marks[name] = round(avg, 2)

top_performer = max(average_marks, key=average_marks.get)

print("\nAverage Marks:", average_marks)
print("Top Performer:", top_performer)