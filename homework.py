import csv
import xlsxwriter
from pathlib import Path


def yr_chice():
    print('Выберите способ ввода (консоль\файл), консоль - 1, файл - 2')
    while True:
        a = input()
        if a in ('1','консоль','Консоль','КОНСОЛЬ'):
            return 1
        elif a in ('2','файл','Файл','ФАЙЛ'):
            return 2
        else: print('Неккорекный ввод, попробуйте снова')


def get_input():
    print('Вы выбрали консоль!')
    print('Можете вводить строки, если хотите закончить напишите на конце строки "&"')
    spisok = []
    while True:
        stroka = input()
        if stroka.endswith('&'):
            print('Вы ввели "&", конец ввода')
            break
        spisok.append(stroka)
    return spisok


def get_file():
    print('Вы выбрали файл!')
    spisok = [-1]
    while spisok==[-1]:
        try:
            way = input('Укажите путь к файлу: ')
            spisok = Path(way).read_text(encoding='utf-8').splitlines()
            print(spisok)
        except Exception as e:
            print(f'Произошла ошибка {e}, попробуйте снова')
            spisok=[-1]
    return spisok
    

def add_to_csv(spisok):
    with open( 'newfile.csv','w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        for row in spisok:
            writer.writerow([row])
    print('csv файл успешно создан!')
    a = input('хотите посмотреть, что в файле?  Напишите Да\Нет ')
    if a in ['да','Да','ДА']:
        print(Path('newfile.csv').read_text(encoding = 'utf-8'))
        
def add_to_xlsx(spisok):
    workbook = xlsxwriter.Workbook('My_name_is_FILE.xlsx')
    worksheet= workbook.add_worksheet('Я лист')
    row = 0
    for item in (spisok):
        item = str(item)
        worksheet.write(row,0,item)
        row+=1
    workbook.close()
    print('xlsx файл успешно создан!')
    
choice =  yr_chice()
if choice == 1: 
    data = get_input()
    if data == []:
        print('Нечего записывать, список пустой')
    else:
        add_to_csv(data)
        add_to_xlsx(data)
else:
    data = get_file()
    if data != []:
        add_to_csv(data)
        add_to_xlsx(data)
    else:
        print('В вашем файле ничего не было ')
    
