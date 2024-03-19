"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 2 = In this second part of the first programming assignment, you should write a program that reads in numbers until a -1 is 
    entered and prints the sum of all numbers entered in decimal format with two digits after the decimal. 
    For example, if the user enters 5000 10 15 -1 the program should display 5025.00 
    (Each number will be separated by a carriage return). 
"""

sum = 0

while True:
    num = int(input("\rEnter a number (-1 to end): "))
    if num == -1:
        break
    sum += num

print(f"The Sum of All Numbers Entered is : {sum:.2f}")