# -*- encoding: utf-8 -*-
"""
Напишите приложение, подсчитывающее количество размещений,
перестановок и сочетаний для последовательностей, параметры которых заданы пользователем.
"""

#	Последовательность: https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C
#	Размещение: https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D0%B5
#	Перестановка: https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0
#	Сочетание:	https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%87%D0%B5%D1%82%D0%B0%D0%BD%D0%B8%D0%B5

# похоже, суть в том что мы вводим последовательность, а так же параметры n и k для расчета размещений, перестановок и сочетаний

import sys
if len(sys.argv) > 1 :
	try:
		Sequence=str(sys.argv[1])
		k_param=int(sys.argv[1])
	except(ValueError):
		print "Input error" 
		exit(1)
else:
	try:
		Sequence=str(raw_input("Enter sequencer: "))
		k_param=int(raw_input("Enter k param: "))
	except(ValueError):
		print "Input error"
		exit(1)

n_param=len(Sequence)

# нам полюбому нужны значениф акториалов для n, k и n-k
# считаем три факториала. Да, мне еще влом запилить под это функцию)))

Fn=1
i=0
while i < n_param:
	i += 1
	Fn = Fn * i

Fk=1
i=0
while i < k_param:
	i += 1
	Fk = Fk * i

Fn_k=1
nk= n_param - k_param
i=0
while i < nk:
	i += 1
	Fn_k = Fn_k * i

# сочетание = (n!) / ((n-k)! * k!)
Combination = Fn / (Fn_k * Fk)
# перестановка = n!
Permutation = Fn
# размещение = (n!) / ((n-k)!)
Placement = Fn / Fn_k

print "Combination: %d, Permutation: %d, Placement: %d" % (Combination, Permutation, Placement)