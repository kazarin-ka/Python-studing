# -*- encoding: utf-8 -*-
"""
Напишите приложение, генерирующее доклады.

Доклад в основном состоит из следующих частей:
	Вступление
	Обзор
	Постановка задачи
	Решение задачи
	Выводы
	Заключение

Создайте по нескольку вариантов каждой из частей в виде списка строк и организуйте их вывод в различных комбинациях.
"""
import random

List_Introductions = [ "Уважаемые коллеги, Вашему вниманию представляю доклад", 
"Уважаемые члены государственной комиссии предоставляю вашему вниманию дипломную работу. ", 
"Господа члены ООН, прослушайте доклад на озвученную тему."
]

List_Overviews = [ "Обратите внимание на обзор возможных вариантов от сторонних производителей. ", 
"На слайде Вы можете видеть обзорную карту Иранских ядерных шахт. ", 
"В ходе дипломной работы был проведен обзор предметной области. Результаты Вы видите на экране. "
]

List_FormulationsOfTheProblems = [ "Итак, наша основная задача - не допустить эскалации конфликта на Ближнем Востоке!", 
"Наша основная задача - не дать конкурентам захватить рынок Полинезии. ", 
"Основной задачей моей дипломной работы была разработка автослива для унитаза."
]

List_SolutionsOfTheProblems = [ "Считаю, что простейшим решением нашей проблемы является демпинг цен.", 
"Введение миротворческого контенгента ООН, на мой взгля, является наиболее подходящим решением.", 
"Мое решение заключается в анализе изменения удельноо давления на площадь седушки унитаза "
]

List_Conclusions = [ "Поставленная задача решена в полном объеме. Унитаз производит автоматический слив. ", 
"Таким образом, доминирующая позиция на рынке остается за нами ", 
"Число жерт среди гражданского населения сведено к минимуму "
]

List_Ends = [ "Спасибо за внимание! Ваши вопросы.", 
"Дальнейшее развите работы планируется в области... ", 
"Прошу коллег дипломатов высказат ьсвои мнения по данному вопросу. "
]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
Introduction = List_Introductions[RandomNumber]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
Overview = List_Overviews[RandomNumber]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
Formulation = List_FormulationsOfTheProblems[RandomNumber]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
Solution = List_SolutionsOfTheProblems[RandomNumber]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
Conclusion = List_Conclusions[RandomNumber]

TempLen = len(List_Introductions)
RandomNumber = random.randint(0, TempLen-1)
End = List_Ends[RandomNumber]

print Introduction
print Overview
print Formulation
print Solution
print Conclusion
print End
