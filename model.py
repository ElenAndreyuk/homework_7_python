
def extract_txt():
    path_1 = 'D:\learningCode\python\homework_7\phones.txt'
    data_1 = open(path_1, 'r', encoding='utf-8')
    list_cont = []
    for line in data_1:
        list_cont.append(line)         
    data_1.close() 
    return list_cont   

def extract_cvs():
    path_2 = 'D:\learningCode\python\homework_7\phonebook.csv'
    data_2 = open(path_2, 'r', encoding='utf-8')
    list_cont_2 = []
    for line in data_2:
        list_cont_2.append(line)
    data_2.close()
    return list_cont_2        

def write_contact(x):
    with open ('phones.txt', 'a', encoding='utf-8') as data:
        for line in x:
            data.write(line +'\n')
    # data = open('phones.txt', 'a', encoding='utf-8')
    # data.write('\n line 2\n')
    # data.close()