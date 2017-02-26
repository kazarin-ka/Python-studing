# -*- encoding: utf-8 -*-
"""
Напишите приложение, производящее копирование файлов.
Имена файлов должны вводится пользователем.
"""
import sys
# если ввели и файл источник и файл назначение
if len(sys.argv) > 2:
	SrcFileName=sys.argv[1]
	DstFileName=sys.argv[2]
# если ввели только один файл, считаем его источником и просим файл назначения
elif 1 < len(sys.argv) < 2:
# иначе нас просто запустили и мы просим оба файла ввести
	SrcFileName=sys.argv[1]
	DstFileName=raw_input ("Enter name of Dst file: ")
	DstFileName=str(DstFileName)
else:
	SrcFileName=raw_input ("Enter name of Src file: ")
	SrcFileName=str(SrcFileName)
	DstFileName=raw_input ("Enter name of Dst file: ")
	DstFileName=str(DstFileName)

SrcFile=open(SrcFileName,"r")
DstFile=open(DstFileName,"w")

for line in SrcFile.readlines():
	DstFile.write(line)

SrcFile.close()
DstFile.close()