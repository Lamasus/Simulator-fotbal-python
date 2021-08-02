from random import random
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import array as arr


def final_points(x):
    points = 0
    for n in range(0,38):
        result=random()
        if result <= x['winpct']:
            points += 3
        elif result <= x['drawpct'] + x['winpct']:
            points += 1
    return points

def setup_vals_barca():
    return {'team':'Barcelona','winpct':0.71,'drawpct':0.18}

def setup_vals_real():
    return {'team':'RealMadrid','winpct':0.66,'drawpct':0.19}

def setup_vals_atl():
    return {'team':'Atletico','winpct':0.60,'drawpct':0.26}

def setup_vals_sevilla():
    return {'team':'Sevilla','winpct':0.46,'drawpct':0.25}

def setup_vals_valencia():
    return {'team':'Valencia','winpct':0.40,'drawpct':0.28}

def setup_vals_real_s():
    return {'team':'RealSociedad','winpct':0.40,'drawpct':0.22}

def setup_vals_villareal():
    return {'team':'Villareal','winpct':0.43,'drawpct':0.25}

def setup_vals_getafe():
    return {'team':'Getafe','winpct':0.38,'drawpct':0.31}

def setup_vals_bilbao():
    return {'team':'Bilbao','winpct':0.39,'drawpct':0.28}

def setup_vals_levante():
    return {'team':'Levante','winpct':0.31,'drawpct':0.27}

def setup_vals_betis():
    return {'team':'Betis','winpct':0.33,'drawpct':0.24}

def setup_vals_celta():
    return {'team':'Celta','winpct':0.32,'drawpct':0.27}

def setup_vals_valladolid():
    return {'team':'Valladolid','winpct':0.25,'drawpct':0.34}

def setup_vals_eibar():
    return {'team':'Eibar','winpct':0.32,'drawpct':0.27}

def setup_vals_alaves():
    return {'team':'Alaves','winpct':0.34,'drawpct':0.23}

alaves = 0
betis = 0
eibar = 0
valladolid = 0
celta = 0
levante = 0
bilbao = 0
getafe = 0
villareal = 0
realsociedad = 0
valencia = 0
sevilla = 0
atletico = 0
real = 0
barca = 0

barca_c = 0
real_c = 0
atletico_c = 0
anomalie_c = 0
egalitate = 0

n = input('nr iteratii:\n')

n = int(n)

for i in range(0,n):

    alaves1 = final_points(setup_vals_alaves())
    betis1 = final_points(setup_vals_betis())
    eibar1 = final_points(setup_vals_eibar())
    valladolid1 = final_points(setup_vals_valladolid())
    celta1 = final_points(setup_vals_celta())
    levante1 = final_points(setup_vals_levante())
    bilbao1 = final_points(setup_vals_bilbao())
    getafe1 = final_points(setup_vals_getafe())
    villareal1 = final_points(setup_vals_villareal())
    realsociedad1 = final_points(setup_vals_real_s())
    valencia1 = final_points(setup_vals_valencia())
    sevilla1 = final_points(setup_vals_sevilla())
    atletico1 = final_points(setup_vals_atl())
    real1 = final_points(setup_vals_real())
    barca1 = final_points(setup_vals_barca())

    alaves = alaves1 + alaves
    betis = betis1 + betis
    eibar = eibar1 + eibar
    valladolid = valladolid1 + valladolid
    celta = celta1 + celta
    levante = levante1 + levante
    bilbao = bilbao1 + bilbao
    getafe = getafe1 + getafe
    villareal = villareal1 + villareal
    realsociedad = realsociedad1 + realsociedad
    valencia = valencia1 + valencia
    sevilla = sevilla1 + sevilla
    atletico = atletico1 + atletico
    real = real1 + real
    barca = barca1 + barca



    c = [alaves1,betis1,eibar1,valladolid1,celta1,levante1,bilbao1,getafe1,villareal1,realsociedad1,valencia1,sevilla1,atletico1,real1,barca1]
    c.sort(reverse=True)
    print(c)
    if c[0] == c[1]:
        egalitate+=1
        print('Egalitate')
    elif c[0] == barca1 :
       barca_c += 1
       print('Barca Campioana')
    elif c[0] == real1 :
       real_c += 1
       print('Real Campioana')
    elif c[0] == atletico1 :
       atletico_c += 1
       print('Atletico Campioana')
    else :
       anomalie_c += 1
       print('Anomalie')




alaves = alaves/n
betis = betis/n
eibar = eibar/n
valladolid = valladolid/n
celta = celta/n
levante = levante/n
bilbao = bilbao/n
getafe = getafe/n
villareal = villareal/n
realsociedad = realsociedad/n
valencia = valencia/n
sevilla = sevilla/n
atletico = atletico/n
real = real/n
barca = barca/n


x = ('Alaves', 'Betis', 'Eibar', 'Valladolid', 'Celta', 'Levante','Bilbao','Getafe','Villareal','RSociedad','Valencia','Sevilla','Atletico','Real','Barca')
y = [alaves,betis,eibar,valladolid,celta,levante,bilbao,getafe,villareal,realsociedad,valencia,sevilla,atletico,real,barca]
y.sort()

fig, ax = plt.subplots()
width = 0.3
ind = np.arange(len(y))
ax.barh(ind, y, width, color="black")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plt.title('Campionat')
plt.xlabel('Numar Mediu Puncte %d iteratii' %(n))
plt.ylabel('Echipe')
for i, v in enumerate(y):
    ax.text(v + 3,i, str(v), color='blue')
plt.show()


print("Campionate barca %d Campionate Real %d  Campionate Atletico %d Campionate restul %d Egalitati %d" % (barca_c, real_c,atletico_c,anomalie_c,egalitate))


#objects = ('Alaves', 'Betis', 'Eibar', 'Valladolid', 'Celta', 'Levante','Bilbao','Getafe','Villareal','RealSociedad','Valencia','Sevilla','Atletico','Real','Barca')
#y_pos = np.arange(len(objects))
#performance = [alaves,betis,eibar,valladolid,celta,levante,bilbao,getafe,villareal,realsociedad,valencia,sevilla,atletico,real,barca]
#performance.sort()

#plt.barh(y_pos, performance, align='center', alpha=0.5)
#plt.yticks(y_pos, objects)
#plt.ylabel('Usage')
#plt.title('Programming language usage')

#plt.show()
