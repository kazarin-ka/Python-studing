# -*- encoding: utf-8 -*-
"""
Напишите приложение, конвертирующее номер дня недели в его название.
Номер должен вводится пользователем.
Для хранения пар номер-имя используйте словарь.
https://ru.wikipedia.org/wiki/Математическая_константа
"""

MathConstDictionary = { "pi":3.14159265358979323846264338327950288,
"e":2.7182818284590452353602874713526625,
"a":2.50290787509589282228390287321821578,
"C2":0.66016181584686957392781211001455577,
"M1":0.26149721284764278375542683860869585,
"G":0.91596559417721901505460351493238411,
"K":0.76422365358922066,
"J":3.058198247456354132564564787888767,
"A":1.28242712910062263687534256886979173
}

MathConst = raw_input ("Enter math const Name and Accuracy (format name:acc): ")
MathConst = str (MathConst)

TempList=MathConst.split(":")

MathConstName = str(TempList[0])
MathConstAccuracy = int(TempList[1])

print "%s = %.*f" % (MathConstName, MathConstAccuracy, MathConstDictionary[MathConstName])