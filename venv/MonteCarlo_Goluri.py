from numpy import random
from random import randrange

average_home = 1.436
average_away = 1.042

#vectorul de echipe o sa fie de forma a[gf_home,ga_home,gf_away,ga_away,puncte,g_marcate,g_primite]

real = [2.105,0.578,1.578,0.77,0,0,0,'Real Madrid    ']
barca = [2.736,0.8421,1.789,1.157,0,0,0,'Barcelona      ']
atletico = [1.473,0.578,1.210,0.8421,0,0,0,'Atletico Madrid']
sevilla = [1.368,0.736,1.473,1.052,0,0,0,'Sevilla        ']
villareal = [1.947,1.315,1.368,1.263,0,0,0,'Villareal      ']
realsociedad = [1.736,1.052,1.210,1.473,0,0,0,'Real Sociedad  ']
granada = [1.368,0.842,1.210,1.473,0,0,0,'Granada        ']
getafe = [1.315,1.052,0.947,0.894,0,0,0,'Getafe         ']
valencia = [1.526,0.842,0.894,1.947,0,0,0,'Valencia       ']
osasuna = [1.368,1.526,1.052,1.315,0,0,0,'Osasuna        ']
bilbao = [1.105,0.736,1.052,1.263,0,0,0,'Athletic Bilbao']
levante = [1.421,1,1.052,1.789,0,0,0,'Levante        ']
valladolid = [0.947,0.789,0.736,1.473,0,0,0,'Real Valladolid']
eibar = [1.315,1.315,0.736,1.631,0,0,0,'Eibar          ']
betis = [1.789,1.421,0.736,1.736,0,0,0,'Betis          ']
alaves = [1.052,1,0.736,2.105,0,0,0,'Alaves         ']
celta = [1.157,1.052,0.789,1.526,0,0,0,'Celta Vigo     ']
leganes = [0.894,1.368,0.684,1.315,0,0,0,'Leganes        ']
mallorca = [1.315,1.157,0.789,2.263,0,0,0,'Mallorca       ']
espanyol = [0.789,1.631,0.631,1.421,0,0,0,'Espanyol       ']


teams = [real,barca,atletico,sevilla,villareal,realsociedad,granada,getafe,valencia,osasuna,bilbao,levante,valladolid,eibar,betis,alaves,celta,leganes,mallorca,espanyol]

k = 0

def match_poisson(team1,team2):
    team1_att = team1[0] / average_home
    team1_def = team1[1] / average_away
    team2_att = team2[2] / average_away
    team2_def = team2[3] / average_home
    team1_rating = team1_att * team2_def * average_home
    team2_rating = team2_att * team1_def * average_away
    print(team1_rating,team2_rating)
    x = random.poisson(lam = team1_rating)
    y = random.poisson(lam = team2_rating)
    #x = random.weibull(a=team1_rating)
    #y = random.weibull(a=team2_rating)
    print("%s vs %s" % (team1[7],team2[7]))
    print("%d-%d" % (x,y))
    team1[5] += x
    team1[6] += y
    team2[5] += y
    team2[6] += x

    if x > y:
        team1[4] += 3
    elif x == y:
        team1[4] += 1
        team2[4] += 1
    else :
        team2[4] += 3

def match_poisson_mc(team1,team2):
    team1_att = team1[0] / average_home
    team1_def = team1[1] / average_away
    team2_att = team2[2] / average_away
    team2_def = team2[3] / average_home
    team1_rating = team1_att * team2_def * average_home
    team2_rating = team2_att * team1_def * average_away
    print(team1_rating,team2_rating)
    x = random.poisson(lam= team1_rating,size=100)
    y = random.poisson(lam = team2_rating,size=100)
    x.sort()
    y.sort()
    rand_x = randrange(100)
    rand_y = randrange(100)
    print("%s vs %s" % (team1[7],team2[7]))
    print("%d-%d" % (x[rand_x],y[rand_y]))
    team1[5] += x[rand_x]
    team1[6] += y[rand_y]
    team2[5] += y[rand_y]
    team2[6] += x[rand_x]

    if x[rand_x] > y[rand_y]:
        team1[4] += 3
    elif x[rand_x] == y[rand_y]:
        team1[4] += 1
        team2[4] += 1
    else :
        team2[4] += 3

def match_gama(team1,team2):
    team1_att = team1[0] / average_home
    team1_def = team1[1] / average_away
    team2_att = team2[2] / average_away
    team2_def = team2[3] / average_home
    team1_rating = team1_att * team2_def * average_home
    team2_rating = team2_att * team1_def * average_away
    print(team1_rating,team2_rating)
    x = random.gamma(shape = team1_rating)
    y = random.gamma(shape = team2_rating)
    print("%s vs %s" % (team1[7],team2[7]))
    print("%d-%d" % (x,y))
    team1[5] += x
    team1[6] += y
    team2[5] += y
    team2[6] += x

    if x > y:
        team1[4] += 3
    elif x == y:
        team1[4] += 1
        team2[4] += 1
    else :
        team2[4] += 3

def match_gama_mc(team1,team2):
    team1_att = team1[0] / average_home
    team1_def = team1[1] / average_away
    team2_att = team2[2] / average_away
    team2_def = team2[3] / average_home
    team1_rating = team1_att * team2_def * average_home
    team2_rating = team2_att * team1_def * average_away
    print(team1_rating,team2_rating)
    x = random.gamma(shape=team1_rating,size=100)
    y = random.gamma(shape=team2_rating,size=100)
    x.sort()
    y.sort()
    rand_x = randrange(100)
    rand_y = randrange(100)
    print("%s vs %s" % (team1[7],team2[7]))
    print("%d-%d" % (x[rand_x],y[rand_y]))
    team1[5] += x[rand_x]
    team1[6] += y[rand_y]
    team2[5] += y[rand_y]
    team2[6] += x[rand_x]

    if x[rand_x] > y[rand_y]:
        team1[4] += 3
    elif x[rand_x] == y[rand_y]:
        team1[4] += 1
        team2[4] += 1
    else :
        team2[4] += 3

n = input('nr iteratii:\n')

n = int(n)

p = input('poisson , gama, poisson_mc sau gama_mc:\n')

if p == 'poisson':
    for k in range(0,n):
        for i in range (0,19):
            for j in range(i+1,20):
                match_poisson(teams[i],teams[j])
                match_poisson(teams[j], teams[i])
                k += 2

elif p == 'gama':
    for k in range(0, n):
        for i in range(0, 19):
            for j in range(i + 1, 20):
                match_gama(teams[i], teams[j])
                match_gama(teams[j], teams[i])
                k += 2

elif p == 'poisson_mc':
    for k in range(0, n):
        for i in range(0, 19):
            for j in range(i + 1, 20):
                match_poisson_mc(teams[i], teams[j])
                match_poisson_mc(teams[j], teams[i])
                k += 2

else:
    p = 'gama_mc'
    for k in range(0, n):
        for i in range(0, 19):
            for j in range(i + 1, 20):
                match_gama_mc(teams[i], teams[j])
                match_gama_mc(teams[j], teams[i])
                k += 2


for i in range(20):
    for j in range(0,20-i-1):
        if teams[j][4] < teams[j+1][4]:
            teams[j],teams[j+1] = teams[j+1],teams[j]
        elif teams[j][4] == teams[j+1][4]:
            if teams[j][5] - teams[j][6] < teams[j + 1][5] - teams[j + 1][6]:
                teams[j], teams[j + 1] = teams[j + 1], teams[j]

i=1
n = float(n)
print("Clasament dupa %d iteratii folosind %s:\n                   Pct         Gm-Gp" % (n,p))
for x in teams:
    if i < 10:
        print(" %d.%s   %f         %f-%f" % (i,x[7],x[4]/n,x[5]/n,x[6]/n))
    else:
        print("%d.%s   %f         %f-%f" % (i, x[7], x[4]/n, x[5]/n, x[6]/n))
    i+=1