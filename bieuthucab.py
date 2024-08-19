# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:00:44 2024

@author: HDM 
"""
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
a1 = math.sqrt(a)
a2 = math.sqrt(math.sqrt(a))
b1 = math.sqrt(b)
b2 = math.sqrt(math.sqrt(b))
ab = math.sqrt(math.sqrt(a * b))
print("Giá trị của biểu thức: ", ((a1 - b1)/(a2 - b2)) - ((a1 + ab)/(a2 +2
                                                                     b2)))