import csv
import xlsxwriter
from pathlib import Path

def get_input():
    print('Вы выбрали консоль!')
    print('Можете вводить строки, если хотите закончить напишите на конце строки "&"')
    spisok = []
    while True:
        string = input()
        if string.endswith('&'):
            print('Вы ввели "&", конец ввода')
            spisok.append(string.strip('&'))
            break
        spisok.append(string)
    return spisok


def get_file():
    print('Вы выбрали файл!')
    spisok = []
    while  not spisok:
        try:
            way = input('Укажите путь к файлу: ')
            spisok = Path(way).read_text(encoding='utf-8').splitlines()
            print(spisok)
        except Exception as e:
            print(f'Произошла ошибка {e}, попробуйте снова')
    return spisok
    

def add_to_csv(spisok):
    with open( 'newfile.csv','w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        for row in spisok:
            writer.writerow([row])
    print('csv файл успешно создан!')
    a = input('хотите посмотреть, что в файле?  Напишите Да\Нет ').lower()
    if a in ['да']:
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


def yr_choice():
    print('Выберите способ ввода (консоль\файл), консоль - 1, файл - 2')
    while True:
        a = input().lower()
        if a in ('1','консоль'):
            main = get_input()
            return main
        elif a in ('2','файл'):
            main = get_file()
            return main 
        else: print('Неккорекный ввод, попробуйте снова')


def all_function (main):
    add_to_csv(main)
    add_to_xlsx(main)

main =  yr_choice()
all_function(main)

   
