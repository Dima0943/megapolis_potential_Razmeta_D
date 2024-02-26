''' Подключаем библтотеку csv для работы с cvs файлами '''
import csv

''' Открытаем файл game.txt и создаём файл game_counter.csv, в который будем записывать изменённые данные '''
with open('game.txt', encoding='utf-8') as f1, open('game_counter.csv', 'w', encoding='utf-8', newline='') as f2:

    '''
    data - список списков для хранения информации из файла game.txt
    headers - заголовки столбцов
    '''

    data = [i.split('$') for i in f1.read().strip().split('\n')]
    headers = data[0] + ['counter']
    data = data[1:]

    ''' bug - словарь для счёта количества ошибок в играх '''
    bugs = dict()

    ''' Алгоритм подсчёта багов в играх '''
    for line in data:
        game_name = line[0]
        if game_name in bugs:
            bugs[game_name] += 1
        else:
            bugs[game_name] = 1

    ''' Дописываем к каждой строке списка data количество ошибок, соответствующее игре '''
    for i in range(len(data)):
        line = data[i]
        game_name = line[0]
        data[i] += [bugs[game_name]]

    ''' Сортируем файл game.txt по количеству ошибок в порядке возрастания '''
    data.sort(key=lambda x: x[4])

    ''' Записываем обновлённые данные в файл game_counter.csv c разделитлем "$" '''
    writer = csv.writer(f2, delimiter='$', quotechar='"')
    writer.writerow(headers)
    for i in data:
        writer.writerow(i)