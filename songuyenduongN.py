# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:03:13 2024

@author: HDM 
"""
N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
if N < 10 or N > 99:
    print("N phải là số có 2 chữ số!")
else:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    
print ("Tổng các chữ số của (N) là: ", hang_chuc + hang_don_vi)

