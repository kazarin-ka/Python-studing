# -*- encoding: utf-8 -*-
"""
Напишите приложение, считывающее слова из файла и 
выводящее их в произвольном порядке на консоль.
"""
import sys
import random

if len(sys.argv) > 1 :
	FileName=str(sys.argv[1])
else:
	FileName=str(raw_input("Enter file Name: "))
	
File=open(FileName,"r")
WordArray=list()

for line in File.readlines():
	String=line.split(' ')[:-1]
	for word in String:
		WordArray.append(word)

File.close()

random.shuffle(WordArray)

for word in WordArray:
	#print word
	sys.stdout.write(word + ' ')