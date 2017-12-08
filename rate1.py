from random import *


def putratings(r):
    probability1 = []
    if r is 1:
        zero = 51
        one = 36
        two = 6
        three = 1
        four = 12
        six = 9
        wicket = 34
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 2:
        zero = 51
        one = 37
        two = 6
        three = 1
        four = 13
        six = 10
        wicket = 30
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 3:
        zero = 51
        one = 34
        two = 10
        three = 1
        four = 13
        six = 10
        wicket = 28
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 4:
        zero = 46
        one = 34
        two = 16
        three = 3
        four = 15
        six = 10
        wicket = 24
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 5:
        zero = 43
        one = 34
        two = 21
        three = 3
        four = 16
        six = 12
        wicket = 19
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 6:
        zero = 42
        one = 34
        two = 22
        three = 4
        four = 19
        six = 12
        wicket = 15
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 7:
        zero = 40
        one = 34
        two = 22
        three = 4
        four = 22
        six = 13
        wicket = 12
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 8:
        zero = 37
        one = 34
        two = 25
        three = 4
        four = 24
        six = 13
        wicket = 10
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 9:
        zero = 31
        one = 36
        two = 28
        three = 4
        four = 25
        six = 15
        wicket = 9
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    elif r is 10:
        zero = 25
        one = 37
        two = 10
        three = 6
        four = 27
        six = 15
        wicket = 9
        while len(probability1) < 100:
            rand = randint(0, 6)
            if rand == 0:
                if zero > 0:
                    probability1.append(0)
                    zero -= 1
            elif rand == 1:
                if one > 0:
                    probability1.append(1)
                    one -= 1
            elif rand == 2:
                if two > 0:
                    probability1.append(2)
                    two -= 1
            elif rand == 3:
                if three > 0:
                    probability1.append(3)
                    three -= 1
            elif rand == 4:
                if four > 0:
                    probability1.append(4)
                    four -= 1
            elif rand == 5:
                if wicket > 0:
                    probability1.append(5)
                    wicket -= 1
            elif rand == 6:
                if six > 0:
                    probability1.append(6)
                    six -= 1
    return probability1
