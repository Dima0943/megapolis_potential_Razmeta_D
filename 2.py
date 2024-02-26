''' Открытаем файл game.txt '''
with open('game.txt', encoding='utf-8') as f1:

    '''
    data - список списков для хранения информации из файла game.txt
    headers - заголовки столбцов
    '''

    data = [i.split('$') for i in f1.read().strip().split('\n')]
    headers = data[0]
    data = data[1:]

    ''' Сортируем файл game.txt по столбцу игры в алфавитном порядке '''
    data.sort(key=lambda x: x[0])

    ''' bug - словарь для счёта количества багов в играх '''
    bugs = dict()

    ''' Алгоритм подсчёта багов в играх '''
    for line in data:
        game_name = line[0]
        if game_name in bugs:
            bugs[game_name] += 1
        else:
            bugs[game_name] = 1

    '''
    Отчет в формате:
        <Игра 1> - количество багов: <count>
        ...
        <Игра N> - количество багов: <count>
        
        Где N - количество уникальных игр
    '''
    for game in bugs:
        print(f"{game} - количество багов: {bugs[game]}")