import math
import random
def nok(amount=3):
    
    numbers = [random.randint(0, 100) for _ in range(amount)]
    phrase = f'Найди наименьшее общее кратное для чисел: {" ".join(map(str, numbers))}'
    nok1 = int(abs(numbers[0]* numbers[1])/math.gcd(numbers[0], numbers[1]))
    return phrase, abs(numbers[0]* nok1)//math.gcd(numbers[0], nok1)
