spisok=[]
dannie=['TAR','TIT','gv','pv','num']
slovo='Tallinn'
slovo_list=list(slovo.lower())#переводим слово в список маленькими буквами
print(slovo)
print(slovo_list)
while True:
    valik=int(input("1 - Добавить букву в список\n2 - Склеить списки\n3 - Добавить букву на определенную позицию\n4 - Удалить элемент\n5 - Удалить элемент по номеру позиции\n6 - Узнать индекс элемента\n7 - Перевернуть список\n"))
    if valik==1:
        a=input("Введите символ: ")
        slovo_list.append(a)#добавляем символ в конец списка
        print(f"Вы добавили {a} в список!\n")
    elif valik==2:
        slovo_list.extend(dannie)#добавляем в конец списка другой список
    elif valik==3:
        a=input("Введите символ: ")
        i=int(input("Введите номер позиции: "))
        slovo_list.insert(i-1,a)#вставляем введённый символ на определенную позицию
    elif valik==4:
        a=input("Введите символ: ")
        n=slovo_list.count(a.lower())#подсчитывает количество элементов в списке
        if n>0:
            for i in range(n):
                slovo_list.remove(a)#удаляет символ
        else:
            print("Данного символа нет!")
    elif valik==5:
        i=int(input("Введите номер позиции: "))
        n=len(slovo_list)
        if i<n:
            slovo_list.pop(i)#удаляет символ под определённым номером в списке
        else:
            print("Данный номер больше последней позиции!")
    elif valik==6:
        a=input("Введите символ: ")
        if a in slovo_list:
            i=slovo_list.index(a)#пишет номер позиции элемента в списке
            print(f"Элемент {a} стоит на {i+1}-ом месте")
        else:
            print("Данного символа нет в списке!")
    elif valik==7:
        slovo_list.reverse()#переворачивает список
    print(slovo_list)
