# -*- encoding: utf-8 -*-
"""
Напишите приложение, считывающее строки из файла и сохраняющее каждую строку в новый файл. Имена файлов должны состоять из первого слова в строке и расширения .txt
"""
import sys

if len(sys.argv) > 1 :
	try:
		FileName=str(sys.argv[1])
	except(ValueError):
		print "File name must be a string" 
		exit(1)
else:
	try:
		FileName=str(raw_input("Enter File name: "))
	except(ValueError):
		print "File name must be a string" 
		exit(1)
	
try:
	File=open(FileName,"r")
except(Exception):
	print "Can't open file: No such file name or directory!"
	exit(1)
"""
читаем построчно, каждую строку превращаем в список слов, разделяя пробелами, берем первое слово, т.е. 0-ой элемент
списка, к нему прибавляем расширение- поулчаем имя файла. открываем это имя на запись и запимсываем туда
только что прочитанную строку. закрываем
"""
for line in File.readlines():
	List=line.split(" ")
	GenFileName=List[0]+".txt"
	NewFile=open(GenFileName,"w")
	NewFile.write(line)
	NewFile.close()

File.close()
