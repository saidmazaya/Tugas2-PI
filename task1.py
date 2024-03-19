"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 1 = Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.
"""

import datetime as dt

numb = int(input("Enter the number of days: "))

date = dt.date.today() + dt.timedelta(days=numb)

print(date.strftime("%A, %B %d, %Y"))
