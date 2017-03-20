# -*- encoding: utf-8 -*-
"""
В Григорианском календаре високосный год определяется по следующему алгоритму: 
високосным является каждый четвертый год, но каждый сотый високосным не является, 
при этом каждый 400-й год все таки високосный. Т.е. 1823 - не високосный, 1824 - високосный, 
1900 - не високосный, 2000 - високосный.
Напишите программу, предлагающую пользователю ввести год, и выводящую информацию о его "високосности"
Предусмотрите проверку корректности ввода и вывод сообщений об ошибках.
"""

import sys
if len(sys.argv) > 1 :
	try:
		Year=int(sys.argv[1])
	except(ValueError):
		print "That was not a Year number!" 
		exit(1)
else:
	try:
		Year=int(raw_input("Enter year: "))
	except(ValueError):
		print "That was not a Year number!"
		exit(1)

# является ли он четвертым годом  - если без остатка делится на 4 то да, иначе нет
if Year%4:
	b004Year = False
else:
	b004Year = True

# является ли он 100-ым годом
if Year%100:
	b100Year = False
else:
	b100Year = True

# является ли он 400-ым годом
if Year%400:
	b400Year = False
else:
	b400Year = True

bResult=(b004Year and (not b100Year)) or b400Year

if bResult:
	print "%d is leap year" % (Year)
else:
	print "%d is NOT leap year" % (Year)
