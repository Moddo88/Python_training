# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование строк
# %
string_with_team1_num = "В команде Мастера кода участников: %d !" % team1_num
string_with_both_teams = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
# format
string_with_score_2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
string_with_team2_time = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
# f строка
string_with_scores = f"Команды решили {score_1} и {score_2} задач."
string_with_challenge_result = f"Результат битвы: {challenge_result}"
string_with_tasks_and_time = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"


print(string_with_team1_num)
print(string_with_both_teams)
print(string_with_score_2)
print(string_with_team2_time)
print(string_with_scores)
print(string_with_challenge_result)
print(string_with_tasks_and_time)