import model
def start_selection():
    print('выберите пункт меню')
    sel = int(input(''' 1 - поиск по имени, 
                        2 - поиск по фамилии,
                        3 - поиск по номеру телефона,
                        4 - огласите весь список пожалуйста,
                        5 - добавить контакт в справочник: ''' ))
    if 0< sel<6:
        return sel
    else:
        print('ошибка ввода')  

def show_all(x):
    x = [i.rstrip() for i in x]
    for i in x:
        if (x.index(i) + 1)%4 == 0:
            print(i, ) 
        else:
            print(i, end = ' ') 

def search_name(a):
    x = input('введите имя: ') 
    for i in range(1, len(a), 4):
        if x in  a[i]:
            print(a[i], a[i-1], a[i+1], a[i+2])
            break
    else:
        print('не найдено')


def search_surname(b):
    y = input('введите фамилию: ') 
    for i in range(0, len(b), 4):
        if y in b[i]:
            print(b[i], b[i+1], b[i+2], b[i+3])
            break
    else:
        print('не найдено')

def search_number(d):
    list_cont = d
    z = input('введите номер телефона: ') 
    for i in range(len(list_cont)):
        if z in list_cont[i]:
            print(list_cont[i], list_cont[i-1], list_cont[i-2], list_cont[i+1])
            break
    else:
        print('не найдено')

def write():
    cont = [] 
    cont.append(input("введите фамилию: "))
    cont.append(input("введите имя: "))
    cont.append(input("введите номер телефона: "))
    cont.append(input("введите описание: "))
    return cont
                

    

