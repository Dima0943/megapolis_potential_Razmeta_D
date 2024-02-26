''' Подключаем библтотеку csv для работы с cvs файлами '''
import csv

''' Открытаем файл game.txt и создаём файл game_new.csv, в который будем записывать изменённые данные '''
with open('game.txt', encoding='utf-8') as f1, open('game_new.csv', 'w', encoding='utf-8', newline='') as f2:

    '''
    data - список списков для хранения информации из файла game.txt
    headers - заголовки столбцов
    '''

    data = [i.split('$') for i in f1.read().strip().split('\n')]
    headers = data[0]
    data = data[1:]
    for line in data:
        if '55' in line[2]:

            ''' Отчет в формате: “У персонажа\t<characters>\tв игре\t<GameName>\tнашлась ошибка с кодом:\t <nameError>.\tДата фиксации:\t <date>” '''
            print(f"У персонажа\t{line[1]}\tв игре\t{line[0]}\tнашлась ошибка с кодом:\t{line[2]}.\tДата фиксации:\t{line[3]}")

            ''' Замена данных (в столбцах "nameError" и "date") '''
            line[2] = 'Done'
            line[3] = '0000-00-00'

    ''' Записываем обновлённые данные в файл game_new.csv c разделитлем "$" '''
    writer = csv.writer(f2, delimiter='$', quotechar='"')
    writer.writerow(headers)
    for i in data:
        writer.writerow(i)