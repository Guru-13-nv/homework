"""
Цель задания:
Освоить различные методы форматирования строк в Python.
Научиться применять эти методы в контексте описания соревнования. История: соперничество двух команд - Мастера кода и
Волшебники данных.
"""
# Использование %:
team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s и в команде Волшебники данных: %s !" % (team1_num, team2_num))
# Использование format():
score_1 = 40
score_2 = 42
print("Команда Волшебники данных решила задач: {} !\n"
      "Команда Мастера кода решила задач: {} !".format(score_2, score_1))
team1_time = 1552.512
team2_time = 2153.31451
print("Мастера кода решили задачи за {}\n"
      "Волшебники данных решили задачи за {}".format(team1_time, team2_time))
# Пример f строки:
print(f'Количество решённых задач по командам: {score_1}, {score_2}')
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
# Итог f строка:
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = team1_name
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = team2_name
else:
    result = 'Ничья!'
print(f'Результат битвы: победила команда {result}!')
