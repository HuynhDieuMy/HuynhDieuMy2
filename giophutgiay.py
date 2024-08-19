# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:17:08 2024

@author: HDM 
"""
thoi_gian = input("Nhập thời gian theo dạng hh:m:ss : ")
hh,mm,ss = map(int, thoi_gian.split(':'))
print("Tổng số giây: ", hh * 3600 + mm*60 + ss)
