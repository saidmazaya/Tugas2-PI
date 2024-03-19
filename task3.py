"""
Nama : Said Muhammad Mazaya
NIM : 221402129

Soal 3 = Write a class that calculates and stores the height and weight of a person in metric.
"""

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / self.height ** 2

person = BMI(55, 1.67)
print(person.BMI_Value()) 