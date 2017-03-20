# -*- encoding: utf-8 -*-
"""
Напишите приложение, считывающее из файла последовательность чисел и находящую
связи между ними.
Виды искомых связей: сумма, разность, произведение, частное, степень, логарифм по основанию 2.
Выведите найденные комбинации чисел и вид зависимости.

Пример:
Исходная последовательность:
25,2357,32,5,75,2356,3,1
Вывод:
2356,1,sum,2357
25,3,mul,75
32,log2,5
и т.д.
"""
import math

filename = "sequence.txt"
File = open(filename, 'r')

NumberSequence = File.readline()
NumberList=NumberSequence.split(",")

# сумма
SumDict = dict()
# разность
DiffDict = dict()
# произведение
ProdDict = dict()
# частное
QuotDict = dict()
# степень
DegrDict = dict()
# Логарифм
LogDict = dict()

for MainNumber in NumberList:
    for TempNumber in NumberList:

        nSum = int(MainNumber) + int(TempNumber)
        if str(nSum) in NumberList:
            SumDict[nSum]=(MainNumber, TempNumber)

        nDiff = abs(int(MainNumber) - int(TempNumber))
        if str(nDiff) in NumberList:
            DiffDict[nDiff] = (MainNumber, TempNumber)

        nProd = int(MainNumber) * int(TempNumber)
        if str(nProd) in NumberList:
            ProdDict[nProd] = (MainNumber, TempNumber)

        nQuot1 = int(MainNumber) / int(TempNumber)
        nQuot2 = int(TempNumber) / int(MainNumber)
        if str(nQuot1) in NumberList:
            QuotDict[nQuot1] = (MainNumber, TempNumber)
        elif str(nQuot2) in NumberList:
            QuotDict[nQuot2] = (TempNumber, MainNumber)

        nDegr1 = int(MainNumber) ** int(TempNumber)
        nDegr2 = int(TempNumber) ** int(MainNumber)
        if str(nDegr1) in NumberList:
            DegrDict[nDegr1] = (MainNumber, TempNumber)
        elif str(nDegr2) in NumberList:
            DegrDict[nDegr2] = (TempNumber, MainNumber)

    nLog = math.log2(int(MainNumber))
    if str(nLog) in NumberList:
        LogDict[nLog] = MainNumber


for Key in sorted(SumDict.keys()):
    print("Sum " + str(Key) + ' from ' + str(SumDict[Key]))

for Key in sorted(DiffDict.keys()):
    print("Diff " + str(Key) + ' from ' + str(DiffDict[Key]))

for Key in sorted(ProdDict.keys()):
    print("Prod " + str(Key) + ' from ' + str(ProdDict[Key]))

for Key in sorted(QuotDict.keys()):
    print("Quot " + str(Key) + ' from ' + str(QuotDict[Key]))

for Key in sorted(DegrDict.keys()):
    print("Degr " + str(Key) + ' from ' + str(DegrDict[Key]))

for Key in sorted(LogDict.keys()):
    print("Log " + str(Key) + ' from ' + str(LogDict[Key]))

