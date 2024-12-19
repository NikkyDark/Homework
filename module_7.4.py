# Форматирование с помощью %

team1_num = 5
team2_num = 6

print('В команде мастера кода участников %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Форматирование с помощью format()

score_2 = 42
team1_time = 18015.2

print("Команда волшебники данных решила задач: {}!".format(score_2))
print('Волшебники данных решили задачи за {:.1f} с !'.format(team1_time))

# Форматирование с использованием f - строк

score_1 = 40
score_2 = 42
challenge_result = ' победа команды Мастера кода'
task_total = 82
time_avg = 350.4

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы:{challenge_result}!')
print(f'Сегодня было решено {task_total} задач, в среднем за {time_avg} секунды за задачу!')

