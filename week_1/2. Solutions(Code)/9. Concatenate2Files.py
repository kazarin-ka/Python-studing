# -*- encoding: utf-8 -*-
"""
Напишите приложение, объединяющее заданные файлы в один и
записывающее результат в файл, имя которого формируется 
из первых букв исходных файлов.
"""
import sys

if len(sys.argv) > 2:
	FirstFilleName = sys.argv[1]
	SecondFileName = sys.argv[2]
else:
	FirstFilleName = str(raw_input("Enter First file name: "))
	SecondFileName = str(raw_input("Enter Second file name: "))

OutputFileName = FirstFilleName[:1] + SecondFileName[:1]
OutputFile = open(OutputFileName,'w')

FirstInputFile = open(FirstFilleName,'r')

for line in FirstInputFile.readlines():
	OutputFile.write(line)

OutputFile.write('\n')
FirstInputFile.close()

SecondInputFile = open(SecondFileName,'r')

for line in SecondInputFile.readlines():
	OutputFile.write(line)

OutputFile.write('\n')
SecondInputFile.close()

OutputFile.close()