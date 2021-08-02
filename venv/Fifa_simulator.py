from numpy import random
from random import randrange
import numpy as np

Bilbao = [4,3,3,'Simon',79,'Capa',79,'Yerray',80,'Martinez',81,'Beriche',81,'Lopez',78,'Garcia',80,'Muniain',83,'Inaki',82,'Garcia',80,'Cordoba',77]
Atletico = [4,4,2,'Oblak',91,'Trippier',81,'Savic',83,'Gimenez',85,'Lodi',79,'Correa',82,'Koke',86,'Partey',84,'Saul',85,'Morata',83,'Felix',80]
Osasuna = [4,4,2,'Herrera',75,'Vidal',72,'Aridane',74,'Garcia',73,'Estupian',75,'Torres',74,'Oier',73,'Brasanac',75,'Garcia',76,'Gallego',73,'Lopez',77]
Leganes = [5,4,1,'Cuellar',75,'Rosales',76,'Bustinza',76,'Omeruo',75,'Siovas',76,'Silva',74,'Oscar',73,'Mesa',79,'Recio',75,'Rodrigues',74,'Carillo',75]
Alaves = [4,4,2,'Pacheho',82,'Navarro',75,'Laguardia',79,'Ely',75,'Duarte',76,'Vidal',76,'Camarasa',76,'Garcia',77,'Rioja',73,'Joselu',75,'Perez',78]
Barcelona = [4,3,3,'Ter Stegen',90,'Roberto',82,'Pique',88,'Lenglet',86,'Alba',86,'Busquets',88,'De Jong',86,'Arthur',85,'Messi',94,'Suarez',89,'Griezmann',89]
Getafe = [4,4,2,'Soria',82,'Suarez',79,'Djene',83,'Rodriguez',73,'Olivera',76,'Nyom',75,'Arambarri',78,'Maksimovic',79,'Cucurella',79,'Mata',80,'Molina',80]
Granada = [4,5,1,'Silva',78,'Diaz',75,'Duarte',75,'Vallejo',76,'Neva',73,'Puertas',75,'Herrera',72,'Gonalons',76,'Machis',76,'Fernandez',75,'Soldado',76]
Levante = [4,4,2,'Aitor',80,'Miramon',75,'Vezo',78,'Postigo',75,'Garcia',75,'Morales',81,'Campana',80,'Vukcevic',75,'Bardhi',78,'Roger',78,'Mayoral',77]
RealValladolid = [4,4,2,'Masip',81,'Moyano',69,'Olivas',76,'Salisu',75,'Carnero',72,'Plano',75,'Michel',74,'Alcaraz',79,'Villa',77,'Unal',77,'Guardiola',78]
Celta = [4,4,2,'Blanco',76,'Mallo',77,'Murillo',78,'Araujo',76,'Olaza',75,'Rafinha',81,'Beltran',76,'Yokuslu',78,'Sisto',76,'Smolov',78,'Aspas',85]
Espanyol = [4,4,2,'Lopes',79,'Lopez',75,'Espinosa',75,'Cabrera',79,'Vila',75,'Embarba',76,'Lopez',78,'Roca',78,'Darder',80,'Calleri',77,'De Tomas',79]
Mallorca = [4,5,1,'Reina',71,'Sasire',71,'Valjent',74,'Raillo',73,'Agbenyenu',71,'Kubo',72,'Baba',72,'Sevilla',75,'Rodriguez',73,'Hernandez',75,'Budimir',76]
Betis = [4,5,1,'Robles',78,'Emerson',75,'Mandi',80,'Feddal',78,'Moreno',77,'Joaquin',80,'Bartra',83,'Guardado',80,'Canales',84,'Fekir',85,'Iglesias',81]
RealMadrid = [4,3,3,'Courtois',88,'Carvajal',85,'Varane',86,'Ramos',89,'Marcelo',84,'Casemiro',88,'Modric',89,'Kroos',89,'Bale',85,'Vinicius',79,'Benzema',88]
RealSociedad = [4,3,3,'Remiro',77,'Zaldua',77,'Elustondo',77,'Le Normand',75,'Monreal',79,'Zubledia',77,'Merino',80,'Odegaard',82,'Portu',83,'Oyarzabal',83,'Isak',78]
Eibar = [4,5,1,'Dmitrovic',80,'Arbilla',76,'Burgos',71,'Bigas',73,'Cote',78,'Diop',78,'Exposito',76,'Pedro Leon',80,'Inui',79,'Orellana',79,'Garcia',79]
Sevilla = [4,3,3,'Vaclik',81,'Navas',82,'Gomez',79,'Diego Carlos',80,'Reguillon',80,'Fernando',82,'Banega',84,'Jordan',79,'Torres',78,'Ocampos',80,'Luuk de Jong',81]
Valencia = [4,2,2,'Jaume',77,'Wass',80,'Garay',83,'Paulista',83,'Gaya',81,'Torres',79,'Parejo',87,'Kondogbia',81,'Soler',80,'Rodrigo',83,'Gomez',81]
Villareal = [4,5,1,'Asenjo',82,'Pena',79,'Albiol',83,'Funes Mori',76,'Moreno',76,'Gerarrd Moreno',82,'Triguerios',79,'Iborra',78,'Cazorla',83,'Gomez',75,'Alcacer',82]


def overall(team):
    i = 0
    k = 4
    de = 0
    mid = 0
    att = 0
    Attackers = []
    Midfielders = []
    Defenders = []
    for i in range(0,team[0]+1):
        de += team[k]
        k += 2
    for i in range(0,team[1]):
        mid += team[k]

        k += 2
    for i in range(0,team[2]):
        att += team[k]
        k += 2
    l=5
    for j in range(0,10):
        if j < team[0]:
            Defenders.append(team[l])
            l+=2
        elif j >=team[0] and j<team[1]+team[0]:
            Midfielders.append(team[l])
            l+=2
        else:
            Attackers.append(team[l])
            l+=2
    return att/team[2], mid/team[1], de/(team[0]+1),Defenders,Midfielders,Attackers

att_Bilbao,mid_Bilbao,def_Bilbao,d,m,a  = overall(Bilbao)
Bilbao.extend((def_Bilbao,mid_Bilbao,att_Bilbao,d,m,a))
att_Atletico,mid_Atletico,def_Atletico ,d,m,a = overall(Atletico)
Atletico.extend((def_Atletico,mid_Atletico,att_Atletico,d,m,a))
att_Osasuna,mid_Osasuna,def_Osasuna,d,m,a  = overall(Osasuna)
Osasuna.extend((def_Osasuna,mid_Osasuna,att_Osasuna,d,m,a))
att_Leganes,mid_Leganes,def_Leganes,d,m,a  = overall(Leganes)
Leganes.extend((def_Leganes,mid_Leganes,att_Leganes,d,m,a))
att_Alaves,mid_Alaves,def_Alaves ,d,m,a = overall(Alaves)
Alaves.extend((def_Alaves,mid_Alaves,att_Alaves,d,m,a))
att_Barcelona,mid_Barcelona,def_Barcelona,d,m,a  = overall(Barcelona)
Barcelona.extend((def_Barcelona,mid_Barcelona,att_Barcelona,d,m,a))
att_Getafe,mid_Getafe,def_Getafe ,d,m,a = overall(Getafe)
Getafe.extend((def_Getafe,mid_Getafe,att_Getafe,d,m,a))
att_Granada,mid_Granada,def_Granada,d,m,a  = overall(Granada)
Granada.extend((def_Granada,mid_Granada,att_Granada,d,m,a))
att_Levante,mid_Levante,def_Levante ,d,m,a = overall(Levante)
Levante.extend((def_Levante,mid_Levante,att_Levante,d,m,a))
att_RealValladolid,mid_RealValladolid,def_RealValladolid ,d,m,a = overall(RealValladolid)
RealValladolid.extend((def_RealValladolid,mid_RealValladolid,att_RealValladolid,d,m,a))
att_Celta,mid_Celta,def_Celta,d,m,a  = overall(Celta)
Celta.extend((def_Celta,mid_Celta,att_Celta,d,m,a))
att_Espanyol,mid_Espanyol,def_Espanyol,d,m,a  = overall(Espanyol)
Espanyol.extend((def_Espanyol,mid_Espanyol,att_Espanyol,d,m,a))
att_Mallorca,mid_Mallorca,def_Mallorca,d,m,a  = overall(Mallorca)
Mallorca.extend((def_Mallorca,mid_Mallorca,att_Mallorca,d,m,a))
att_Betis,mid_Betis,def_Betis ,d,m,a = overall(Betis)
Betis.extend((def_Betis,mid_Betis,att_Betis,d,m,a))
att_RealMadrid,mid_RealMadrid,def_RealMadrid,d,m,a  = overall(RealMadrid)
RealMadrid.extend((def_RealMadrid,mid_RealMadrid,att_RealMadrid,d,m,a))
att_RealSociedad,mid_RealSociedad,def_RealSociedad ,d,m,a = overall(RealSociedad)
RealSociedad.extend((def_RealSociedad,mid_RealSociedad,att_RealSociedad,d,m,a))
att_Eibar,mid_Eibar,def_Eibar ,d,m,a = overall(Eibar)
Eibar.extend((def_Eibar,mid_Eibar,att_Eibar,d,m,a))
att_Sevilla,mid_Sevilla,def_Sevilla,d,m,a  = overall(Sevilla)
Sevilla.extend((def_Sevilla,mid_Sevilla,att_Sevilla,d,m,a))
att_Valencia,mid_Valencia,def_Valencia,d,m,a  = overall(Valencia)
Valencia.extend((def_Valencia,mid_Valencia,att_Valencia,d,m,a))
att_Villareal,mid_Villareal,def_Villareal,d,m,a  = overall(Villareal)
Villareal.extend((def_Villareal,mid_Villareal,att_Villareal,d,m,a))


pts_Atletico = 0
Atletico = Atletico + [pts_Atletico]
pts_Barca = 0
Barcelona = Barcelona + [pts_Barca]
pts_RealMadrid = 0
RealMadrid = RealMadrid + [pts_RealMadrid]
pts_RealSociedad = 0
RealSociedad = RealSociedad + [pts_RealSociedad]
pts_Valencia = 0
Valencia = Valencia + [pts_Valencia]
pts_Villareal = 0
Villareal = Villareal + [pts_Villareal]
pts_Betis = 0
Betis = Betis + [pts_Betis]
pts_Mallorca = 0
Mallorca = Mallorca + [pts_Mallorca]
pts_Eibar = 0
Eibar = Eibar + [pts_Eibar]
pts_Sevilla = 0
Sevilla = Sevilla + [pts_Sevilla]
pts_Espanyol = 0
Espanyol = Espanyol + [pts_Espanyol]
pts_Celta = 0
Celta = Celta + [pts_Celta]
pts_RealValladolid = 0
RealValladolid = RealValladolid + [pts_RealValladolid]
pts_Bilbao = 0
Bilbao = Bilbao + [pts_Bilbao]
pts_Granada = 0
Granada = Granada + [pts_Granada]
pts_Getafe = 0
Getafe = Getafe + [pts_Getafe]
pts_Alaves = 0
Alaves = Alaves + [pts_Alaves]
pts_Levante = 0
Levante = Levante + [pts_Levante]
pts_Osasuna = 0
Osasuna = Osasuna + [pts_Osasuna]
pts_Leganes = 0
Leganes = Leganes + [pts_Leganes]


teams =  [Bilbao,Atletico,Osasuna,Leganes,Alaves,Barcelona,Getafe,Granada,Levante,RealValladolid,Celta,Espanyol,Mallorca,Betis,RealMadrid,RealSociedad,Eibar,Sevilla,Valencia,Villareal]

att_avg = 0
mid_avg = 0
def_avg = 0

for x in teams:
    att_avg += x[25]
    mid_avg += x[26]
    def_avg += x[27]

att_avg = att_avg/20
mid_avg = mid_avg/20
def_avg = def_avg/20


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj][0]

def match (team1,team2):
    def1 = team1[25] + 0.5
    mid1 = team1[26] + 0.5
    att1 = team1[27] + 0.5
    def2 = team2[25]
    mid2 = team2[26]
    att2 = team2[27]
    ovr1 = (def1 + mid1 + att1)/3
    ovr2 = (def2 + mid2 + att2)/3
    att_team1 = att1 - def2
    att_team2 = att2 - def1


    if att_team1 > 10:
        goluri1 = random.poisson(lam = 3)
    elif att_team1 > 5:
        goluri1 = random.poisson(lam= 2)
    elif att_team1 > 0 :
        goluri1 = random.poisson(lam=1)
    else:
        goluri1 = random.poisson(lam=0)

    if att_team2 > 10:
        goluri2 = random.poisson(lam=3)
    elif att_team2 > 5:
        goluri2 = random.poisson(lam=2)
    elif att_team2 > 0:
        goluri2 = random.poisson(lam=1)
    else:
        goluri2 = random.poisson(lam=0)




    print(namestr(team1, globals())), print(ovr1)
    print(namestr(team2, globals())), print(ovr2)

    print(goluri1,goluri2)
    
    if goluri1 > goluri2:
        team1[31] += 3
    elif goluri1 == goluri2:
        team1[31] += 1
        team2[31] == 2
    else:
        team2[31] += 3

n = input('nr iteratii:\n')
n = int(n)

for k in range(0,n):
    for i in range(0, 19):
        for j in range(i + 1, 20):
            match(teams[i], teams[j])
            match(teams[j], teams[i])


for i in range(20):
    for j in range(0,20-i-1):
        if teams[j][31] < teams[j+1][31]:
            teams[j],teams[j+1] = teams[j+1],teams[j]

i=1

n = float(n)
print("Clasament  %d  iterații   " % (n) )
for x in teams:
    print(namestr(x, globals()))
    if i < 10:
        print(" %d %f" % (i,x[31]/n))
    else:
        print("%d %f" % (i, x[31]/n))
    i+=1







