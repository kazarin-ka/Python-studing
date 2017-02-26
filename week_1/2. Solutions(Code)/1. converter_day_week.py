# -*- encoding: utf-8 -*-
"""
Напишите приложение, конвертирующее номер дня недели в его название.
Номер должен вводится пользователем.
Для хранения пар номер-имя используйте словарь.
"""

WeekDictionary = { 1:"Monday",
2:"Tuesday",
3:"Wednesday",
4:"Thursday",
5:"Friday",
6:"Saturday",
7:"Sunday"
}

DayNumber = raw_input ("Enter Day number: ")
DayNumber = int (DayNumber)

print WeekDictionary[DayNumber]
