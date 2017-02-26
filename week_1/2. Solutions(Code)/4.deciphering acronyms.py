# -*- encoding: utf-8 -*-
"""
Напишите приложение, генерирующее расшифровки аббревиатур.
Для этого создайте словарь, ключом которого будет является буква, а значением - список слов, начинающихся с этой буквы.
Затем cгенерируйте расшифровку для введённой пользователем аббревиатуры.

Например:
	Ввод: PPSP
	Вывод: Pretty Pig Swimming Protocol
"""
import random

AcronymsListDictionary = { "A":["Actual", "Annus", "Azimuth", "Arch", "Area", "Axial"],
"B":["Background", "Bag", "Ballistic", "Balloon", "Bath", "Before"],
"C":["Capacitance", "Capacity", "Cathode", "Center", "Centimeter", "Circuit" ],
"D":["Deci", "Deuteron", "Deutron", "Dried", "Dry"],
}

#print AcronymsListDictionary["C"]

AcronymString = raw_input ("Enter Your Acronim: ")
AcronymString = str (AcronymString)

AcronymList=list(AcronymString)
ResultList=[]

for Letter in AcronymList:
	TempList=AcronymsListDictionary[Letter]
	ListLen=len(TempList)
	RandomNumber=random.randint(0, ListLen-1)
	TempWord=TempList[RandomNumber]
	ResultList.append(TempWord)

print " ".join(ResultList)