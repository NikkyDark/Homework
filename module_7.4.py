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
team1_time = 1552.512
team2_time = 2153.31451
task_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = "победа команды Мастера кода"
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = "победа команды Волшебники данных"
else:
    challenge_result = "ничья"

tasks_total = score_1 + score_2

total_time = team1_time + team2_time
time_avg = total_time / tasks_total


print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы:{challenge_result}!')
print(f'Сегодня было решено {task_total} задач, в среднем за {time_avg} секунды за задачу!')

