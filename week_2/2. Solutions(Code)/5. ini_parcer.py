# -*- encoding: utf-8 -*-
"""
Парсер ini формата

Напишите приложение, предназначенное для считывания файлов в ini формате.
Файл состоит из секций, имя секции задаётся в двойных квадратных скобках.
Каждая секция содержит переменные в формате <имя>=<значение>
Пример:
        [[config]]
                controlPort=8900
                idleTimeout=20
        [[admin]]
                login=petrovich
                email=petrovich@zavod.ru
                password=secret

После анализа файла его содержимое должно быть представлено в виде
словаря, ключами которого являются имена секций, а значениями - словари переменных.
Выведите на консоль количество секций и кол-во переменных в каждой секции.
"""

# filename=str(input("input file name: "))
filename = "test.ini"
File = open(filename, 'r')

IniFileParceDict = dict()
TempDict = dict()

MainKeyword = ""
SecondKeyword = ""
Entry = ""

# подсчет
TotalSections = 0
VarInSectNumDict = dict()

for ReadFileLine in File.readlines():

    # убираем пробелы, табуляции, переводы строк из строк
    FileString = ReadFileLine.replace(" ", "").replace("\t", "").replace("\n", "")

    # если наш словарь был пусть и первая строка начинается как имя секции
    if (len(IniFileParceDict) == 0) and (FileString.startswith("[[") and FileString.endswith("]]")):
        # очищаем от скобочек
        MainKeyword = FileString.replace("[[", "").replace("]]", "")
        # записываем ключ с пустым значением
        IniFileParceDict[MainKeyword] = ""
        # увеличиваем счетчик числа секций
        TotalSections += 1

    # если это шаблон который начинается с [[ и заканчивается ]] те. имя секции
    elif FileString.startswith("[[") and FileString.endswith("]]"):
        # копируем словарь в словарь, тем самым записываем соответствие названия секции и ее параметры
        IniFileParceDict[MainKeyword] = TempDict.copy()
        # считаем сколько в секции переменных
        VarInSectNumDict[MainKeyword] = len(TempDict)
        # очищаем от скобочек, получая новый ключ
        MainKeyword = FileString.replace("[[", "").replace("]]", "")
        # записываем ключ с пустым значением
        IniFileParceDict[MainKeyword] = ""
        # вычищаем временынй словарь
        TempDict.clear()
        # увеличиваем счетчик числа секций
        TotalSections += 1

    # иначе это у нас переменная внутри секции
    elif FileString.find("=") > 1:
        # разделяем строку по знаку = и забиваем в подсловарь
        FileList = FileString.split("=")
        SecondKeyword = FileList[0]
        Entry = FileList[1]

        TempDict[SecondKeyword] = Entry

File.close()

# завершающий шаг
IniFileParceDict[MainKeyword] = TempDict.copy()
VarInSectNumDict[MainKeyword] = len(TempDict)
TempDict.clear()


for MainKeyword in IniFileParceDict:
    print("[[" + MainKeyword + "]]")
    TempDict = IniFileParceDict[MainKeyword]
    for SecondKeyword in TempDict:
        print("\t" + SecondKeyword + " : " + TempDict[SecondKeyword])

print("\n")
print ("Total Sections: " + str(TotalSections) )
for MainKeyword in VarInSectNumDict:
    print("[[" + MainKeyword + "]] var:" + str(VarInSectNumDict[MainKeyword]))


