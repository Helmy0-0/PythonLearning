input1 = input("Enter name: ")
input2 = float(input("Enter grade: "))
student = {}
student[input1] = input2

more_students = True
while more_students:
    input1 = input("Enter name: ")
    input2 = float(input("Enter grade: "))
    student[input1] = input2
    more_students = input("Do you want to add another student? (yes/no): ").lower() == 'yes'

average_grade = sum(student.values()) / len(student)
print(f"The average grade is: {average_grade:.2f}")