# -*- encoding: utf-8 -*-
"""
Напишите приложение, считывающее из файла последовательность чисел
и выводящее их сумму, произведение, среднее арифметическое и факториал каждого числа.
"""
filename = "sequence.txt"
File = open(filename, 'r')

NumberSequence = File.readline()
NumberList=list(NumberSequence)
# сумма
NumSumm = 0
# произведение
NumProduct = 1
# среднее арифметическое
NumAverage = 0
# факториал
DictFactorial = dict()

for Number in NumberList:
    NumSumm = NumSumm + int(Number)
    NumProduct = NumProduct * int(Number)

    # подсчитываем факториал для текузего числа
    nCout = 0
    nFactorial = 1
    while nCout < int(Number):
        nCout += 1
        nFactorial = nFactorial * nCout

    DictFactorial[Number] = nFactorial


NumAverage = NumSumm / len(NumberList)

print("Sum: " + str(NumSumm) )
print("Product: " + str(NumProduct))
print("Average: " + str(NumAverage))

for Key in sorted(DictFactorial.keys()):
    print("Factorial " + str(Key) + ' is ' + str(DictFactorial[Key]))

