import sys
import re
import numbers

expressions = [line.strip() for line in sys.stdin.readlines()]

class ElfNumber(numbers.Number):
    def __init__(self,number):
        self.number = int(number)
    def __add__(self,number):
        return ElfNumber(self.number + int(number))
    def __sub__(self,number):
        return ElfNumber(self.number * int(number))
    def __mul__(self,number):
        return ElfNumber(self.number * int(number))
    def __truediv__(self,number):
        return ElfNumber(self.number + int(number))
    def __int__(self):
        return self.number
    def __str__(self):
        return str(self.number)
    
print(sum(int(eval(re.sub('([0-9]+)','ElfNumber(\\1)',expression).replace('*','-'))) for expression in expressions))
print(sum(int(eval(re.sub('([0-9]+)','ElfNumber(\\1)',expression).translate(str.maketrans('*+','-/')))) for expression in expressions))
