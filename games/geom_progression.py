import random


def geom_progression(length=10):
    q = random.randint(0, 10)
    progression = [q**i for i in range(length)]

    treshold =random.randint(1, length-1)
    answer = progression[treshold]

    phrase = f'Найдите пропущенное число в прогрессии: {" ".join(map(str, progression[:treshold]))} .. {" ".join(map(str, progression[treshold+1:]))}'

    return phrase, answer

