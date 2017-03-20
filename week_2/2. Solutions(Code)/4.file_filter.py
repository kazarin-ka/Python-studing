# -*- encoding: utf-8 -*-
"""
Напишите приложение, фильтрующее файл по первому слову в строке и выводящее результат на консоль.

короче аналог grep - юзер вводи мя файла и слово а мы должны вывести все строки где есть слово
"""
import sys

if len(sys.argv) > 1 :
	try:
		FileName=str(sys.argv[1])
	except(ValueError):
		print "File name must be a string" 
		exit(1)

	try:
		SearchWord=str(sys.argv[2])
	except(ValueError):
		print "Search word must be a string/word" 
		exit(1)
else:
	try:
		FileName=str(raw_input("Enter File name: "))
	except(ValueError):
		print "File name must be a string" 
		exit(1)

	try:
		SearchWord=str(raw_input("Enter search word: "))
	except(ValueError):
		print "Search word must be a string/word" 
		exit(1)
	
try:
	File=open(FileName,"r")
except(Exception):
	print "Can't open file: No such file name or directory!"
	exit(1)

# делаем поисковое слово строчным
SearchWord = SearchWord.lower()

FindList=list()
for line in File.readlines():
	# убираем из строки точки, двоеточие и запятые
	TempString = line.replace(".","").replace(",","").replace(":","")
	# приводим все к одному размеру букв
	TempString=TempString.lower()
	# если в этой строке есть наше слово тогда изначальную строчку кладем в массив "найденышей"))
	if TempString.find(SearchWord) > 1:
		FindList.append(line)

for line in FindList:
	print line