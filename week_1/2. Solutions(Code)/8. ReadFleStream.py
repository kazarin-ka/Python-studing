# -*- encoding: utf-8 -*-
"""
Напишите приложение, считывающее из файла последовательность
чисел, разделённых запятыми и выводящее её на экран в прямом и 
обратном порядке.
"""
import sys
if len(sys.argv) > 1 :
	FileName=str(sys.argv[1])
else:
	FileName=str(raw_input(""))
	
File=open(FileName,"r")
Line=File.readline()
Numbers=Line.replace(',','')

print "Forward: " + Numbers
print "Reverce: " + Numbers[::-1]

#print Line
File.close()
