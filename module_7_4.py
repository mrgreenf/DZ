team1 = 'Мастера кода'
team2 = 'Волшебники данных'

# Использование %:

def num(team1_num, team2_num):
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('В команде %s участников: %s !' % (team1, team2_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format():

def score(score_1, score_2):
    team1_score = score_1
    team2_score = score_2

    print('Команда {} решила задач: {}'.format(team1, team1_score))
    print('Команда {} решила задач: {}'.format(team2, team2_score))

def time(time_1, time_2):
    team1_time = time_1
    team2_time = time_2

    print('{} решили задачи за {} с !'.format(team1, team1_time))
    print('{} решили задачи задачи за {} с !'.format(team2, team2_time))

# Использование f-строк:

def challenge_result(tasks_total, time_avg, time_one_task):
    print(f'Сегодня было решено {tasks_total} задач за {time_avg} минут, в среднем по {time_one_task} секунды на задачу!')

def score(score_1, score_2):

    print(f'Команды решили {score_1} и {score_2} задач.')

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print(f'Результат битвы: победа команды {team1}!')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print(f'Результат битвы: победа команды {team2}!')
    else:
        print('Ничья!')

num(team1_num = 5, team2_num = 6)
score(score_1 = 40, score_2 = 42)
time(time_1 = 1552.512, time_2 = 2153.31451)
challenge_result(tasks_total = 82, time_avg = 61.7, time_one_task = 45.2)
