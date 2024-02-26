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

    ''' Запускаем консольную программу '''
    while True:
        ''' name - переменная, содержащая имя персонажа '''
        name = input('Введите имя персонажа >>> ')

        ''' При вводе "game" завершаем работу программы '''
        if name == 'game':
            exit()

        else:
            ''' result - список для названий игр'''
            result = []

            ''' Поиск персонаей в списке списков data '''
            for line in data:
                if line[1] == name and line[0] not in result:
                    result.append(line[0])

            ''' Вывод содержимого списка result в требуемом формате '''
            if len(result) > 5:
                print(f'Персонаж {name} встречается в играх:')
                for game in result[:5]:
                    print(game)
                print('и др.')

            elif len(result) == 0:
                print('Этого персонажа не существует')

            else:
                print(f'Персонаж {name} встречается в играх:')
                for game in result:
                    print(game)
