from ast import While
import random
from time import clock_getres
import matplotlib.pyplot as plt


def rollDice():
    return random.randrange(1, 7)


print(rollDice())


def fiveRollDice():
    r1 = rollDice()
    r2 = rollDice()
    r3 = rollDice()
    r4 = rollDice()
    r5 = rollDice()
    return [r1, r2, r3, r4, r5]


print(fiveRollDice())


def countDice():
    counter = {}
    for dice in fiveRollDice():
        if dice in counter:
            counter[dice] = counter[dice] + 1
        else:
            counter[dice] = 1
    return counter


print(countDice())


def checkWinDice():
    con = countDice()
    w1 = 1
    w5 = 5
    if w1 in con:
        countw1 = con[w1]
        balls1 = countw1 * 10
    else:
        balls1 = 0
    if w5 in con:
        countw5 = con[w5]
        balls5 = countw5 * 5
    else:
        balls5 = 0

    balls = balls1 + balls5
    return balls


print(checkWinDice())


def calcVar(iterations):
    count = iterations
    end = 0
    listDice = list()
    while count != end:
        listDice.append(checkWinDice())
        count -= 1
    return listDice


resultvar = calcVar(100000)


def countVar(resultvar):
    numvar = dict()
    for key in resultvar:
        if key in numvar:
            numvar[key] += 1
        else:
            numvar[key] = 1
    return numvar


checked_result = countVar(resultvar=resultvar)
print(f"List of roll dice times: {checked_result}")


def resultForPlot(checked_result):
    a = []
    b = []
    for key, value in checked_result.items():
        a.append(key)
        b.append(value)
    return a, b


forplot = resultForPlot(checked_result=checked_result)

myplot = plt.plot(forplot[0], forplot[1])
print(myplot)
