"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 4 = Write a program that takes in grades one at a time until a -1 is seen to mark the end of the list.  
    Each grade will be separated by an enter key.  When you are done, output the average (as an int) 
    followed by the grades in order that you saw them.
"""

grades = []

while True:
    grade = int(input("Enter a grade (-1 to end): "))
    if grade == -1:
        break
    grades.append(grade)

if len(grades) > 0:
    print(int(sum(grades) / len(grades)))
    for grade in grades:
        print(grade)
else :
    print("No Grades Entered")