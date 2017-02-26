# -*- encoding: utf-8 -*-
"""
Напишите приложение для формирования файла соответствия имён хостов и их IP адресов
и приложение для поиска записей в этом файле.

Формат файла:
<адрес> <имя>
например:
127.0.0.1 localhost

При запуске приложения необходимо считать файл, сформировать словарь, парами ключ-значение которого служат строчки этого файла, затем вывести словарь на консоль и предоставить 
пользователю возможность ввести новую пару.
Пару следует добавить в конец файла.

Второе приложение должно обеспечивать поиск по имени и адресу в том же файле.
==========================
Это первое приложение, которое работает с базой
"""

File=open('hosts', 'r')

HostsDictionary={}

for Line in File.readlines():
    List=Line.split()
    HostsDictionary[List[0]]=List[1]

File.close()

print "File Hosts conststs of:\n"

for Host in HostsDictionary:
	print "%s %s" % (Host, HostsDictionary[Host])

print "\n"

while 1:
	UserAnswer = raw_input ("Do You want to add record in file? (y/n)")
	UserAnswer = str(UserAnswer)

	if UserAnswer == "y":
		break
	elif UserAnswer == "n":
		exit(0)
	else:
		print "Choose Yes or No only!"

UserAnswer = raw_input ("Enter new host name resolution (ip host): ")
UserAnswer = str(UserAnswer)
print "\n"

File=open('hosts', 'a')
File.writelines('\n')
File.writelines(UserAnswer)
File.close()

List=UserAnswer.split()
HostsDictionary[List[0]]=List[1]

print "Now hosts list in file look like this:\n"
for Host in HostsDictionary:
	print "%s %s" % (Host, HostsDictionary[Host])

exit(0)