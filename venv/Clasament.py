from random import random


def final_points_Lazio():
    points_L = 62
    for n in range(0,12):
        result=random()
        if result <= 0.7308:
            points_L += 3
        elif result <= 0.1923 + 0.7308:
            points_L += 1
    return points_L


def final_points_Inter():
    points_I = 57
    for n in range(0,12):
        result=random()
        if result <= 0.6539:
            points_I += 3
        elif result <= 0.2308 + 0.6539:
            points_I += 1
    return points_I


def final_points_Juve():
    points_J = 63
    for n in range(0,12):
        result=random()
        if result <= 0.7692:
            points_J += 3
        elif result <= 0.1154 + 0.7692:
            points_J += 1
    return points_J

juve_championship = 0
inter_championship = 0
lazio_championship = 0
egalitati = 0
egalitati_perfecte = 0

for i in range(0,10000):
    juve = final_points_Juve()
    inter = final_points_Inter()
    lazio = final_points_Lazio()
    if juve > lazio and lazio > inter and juve > inter:
        print("Juve 1st with {} points,Lazio 2nd with {} points,Inter 3rd with {} points".format(juve,lazio,inter))
        juve_championship += 1
    elif juve > lazio and inter > lazio and juve > inter:
        print("Juve 1st with {} points,Inter 2nd with {} points,Lazio 3rd with {} points".format(juve, inter, lazio))
        juve_championship += 1
    elif lazio > juve and juve > inter and lazio > inter:
        print("Lazio 1st with {} points,Juve 2nd with {} points,Inter 3rd with {} points".format(lazio, juve, inter))
        lazio_championship += 1
    elif lazio > juve and inter > juve and lazio > inter:
        print("Lazio 1st with {} points,Inter 2nd with {} points,Juve 3rd with {} points".format(lazio, inter, juve))
        lazio_championship += 1
    elif inter > juve and juve > lazio and inter > lazio:
        print("Inter 1st with {} points,Juve 2nd with {} points,Lazio 3rd with {} points".format(inter,juve,lazio))
        inter_championship += 1
    elif inter > juve and lazio > juve and inter > lazio:
        print("Inter 1st with {} points,Lazio 2nd with {} points,Juve 3rd with {} points".format(inter,lazio,juve))
        inter_championship += 1
    elif juve == inter and lazio > juve:
        print("Lazio 1st with {} points,Juve and Inter 2nd with {} points".format(lazio, juve))
        lazio_championship += 1
        egalitati += 1
    elif juve == inter and lazio < juve:
        print("Inter and Juve 1st with {} points ,Lazio 2nd with {} points".format(inter, lazio))
        egalitati += 1
        result = random()
        if(result >= 0.5):
            print("Inter won the Championship")
            inter_championship += 1
        else:
            print("Juve won the Championship")
            juve_championship += 1
    elif juve == lazio and inter > juve:
        print("Inter 1st with {} points,Juve and Lazio 2nd with {} points".format(inter, lazio))
        inter_championship += 1
        egalitati += 1
    elif juve == lazio and inter < juve:
        print("Lazio and Juve 1st with {} points ,Inter 2nd with {} points".format(lazio, inter))
        egalitati += 1
        result = random()
        if (result >= 0.5):
            print("Lazio won the Championship")
            lazio_championship += 1
        else:
            print("Juve won the Championship")
            juve_championship += 1
    elif lazio == inter and juve > lazio:
        egalitati += 1
        print("Juve 1st with {} points,Inter and Lazio 2nd with {} points".format(juve, lazio))
        juve_championship += 1
    elif inter == lazio and juve < lazio:
        egalitati += 1
        print("Lazio and Inter 1st with {} points ,Juve 2nd with {} points".format(lazio, juve))
        result = random()
        if (result >= 0.5):
            print("Lazio won the Championship")
            lazio_championship += 1
        else:
            print("Inter won the Championship")
            inter_championship += 1
    else:
        print("Lazio,Inter and Juve have {} points".format(lazio))
        egalitati_perfecte += 1


print("Probabilitati castigare campionat:   Lazio:{}%  Juventus:{}% Inter:{}%   Egalitate intre doua echipe:{}%   Egalitati_Perfecte:{}%".format(lazio_championship/100,juve_championship/100,inter_championship/100,egalitati/100,egalitati_perfecte/100))
