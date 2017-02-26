# -*- encoding: utf-8 -*-
"""
Напишите приложение, конвертирующее название месяца в его номер.

Название должно вводится пользователем.
Для хранения пар название-номер используйте словарь.
"""

MonthDictionary = { "January":1,
"February":2,
"March":3,
"April":4,
"May":5,
"June":6,
"July":7,
"August":8,
"September":9,
"October":10,
"November":11,
"December":12
}

MonthNumber = raw_input ("Enter Month name: ")
MonthNumber = str (MonthNumber)

print MonthDictionary[MonthNumber]
