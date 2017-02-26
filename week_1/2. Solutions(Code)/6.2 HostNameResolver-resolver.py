# -*- encoding: utf-8 -*-
"""
Напишите приложение для формирования файла соответствия имён хостов и их IP адресов
и приложение для поиска записей в этом файле.

Формат файла:
<адрес> <имя>
например:
127.0.0.1 localhost

При запуске приложения необходимо считать файл, сформировать словарь, парами ключ-значение которого служат строчки этого файла, затем вывести словарь на консоль и предоставить пользователю возможность ввести новую пару.
Пару следует добавить в конец файла.

Второе приложение должно обеспечивать поиск по имени и адресу в том же файле.
================================
Это второе приложение -резолвер
"""
import sys

File=open('hosts', 'r')

HostsDictionary={}

for Line in File.readlines():
    List=Line.split()
    HostsDictionary[List[0]]=List[1]

File.close()

if len(sys.argv) > 1:
	ResolvObject=sys.argv[1]
else:
	ResolvObject = raw_input ("Enter ip addr or host name: ")
	ResolvObject = str(ResolvObject)

KeyList=HostsDictionary.keys()
ValList=HostsDictionary.values()
#сначала поиск по ключам, т.е. адресам
if ResolvObject in KeyList:
	print HostsDictionary[ResolvObject]
elif ResolvObject in ValList: #потом поиск по значениям
	for Key, Value in HostsDictionary.items():
		if Value == ResolvObject:
			print Key
else:
	print "No shuch host or ip addr"
