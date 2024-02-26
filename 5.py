''' Подключаем библтотеку csv для работы с cvs файлами '''
import csv
import string

def my_hash(text):
    alf = '_' + string.ascii_letters + '1234567890:-'
    for i in range(len(text)):
        pass


''' Открытаем файл game.txt и создаём файл game_counter.csv, в который будем записывать изменённые данные '''
with open('game.txt', encoding='utf-8') as f1, open('game_with_hash.csv', 'w', encoding='utf-8', newline='') as f2:

    '''
    data - список списков для хранения информации из файла game.txt
    headers - заголовки столбцов
    '''

    data = [i.split('$') for i in f1.read().strip().split('\n')]
    headers = ['hash'] + data[0]
    data = data[1:]

    for i in range(len(data)):
        line = data[i]
        game_name = line[0]
        cha_name = line[1]
        game_name = game_name.replace(' ', '')
        key = game_name + cha_name

my_hash('123')