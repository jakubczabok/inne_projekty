import random
import math
import sys
import os
import pprint
import operator
import time

os.system("cls")

ver={"name": "Max Verstappen    ", "team": "Red Bull", "rating": 10.0, "score": 0, "positions":[], "wins":0}
per={"name": "Sergio Perez      ", "team": "Red Bull", "rating": 9.76, "score": 0, "positions":[], "wins":0}
lec={"name": "Charles Leclerc   ", "team": "Ferrari", "rating": 9.81, "score": 0, "positions":[], "wins":0}
sai={"name": "Carlos Sainz      ", "team": "Ferrari", "rating": 9.71, "score": 0, "positions":[], "wins":0}
rus={"name": "George Russell    ", "team": "Mercedes", "rating": 9.68, "score": 0, "positions":[], "wins":0}
ham={"name": "Lewis Hamilton    ", "team": "Mercedes", "rating": 9.65, "score": 0, "positions":[], "wins":0}
nor={"name": "Lando Norris      ", "team": "McLaren", "rating": 9.48, "score": 0, "positions":[], "wins":0}
alo={"name": "Fernando Alonso   ", "team": "Alpine", "rating": 9.42, "score": 0, "positions":[], "wins":0}
oco={"name": "Esteban Ocon      ", "team": "Alpine", "rating": 9.41, "score": 0, "positions":[], "wins":0}
bot={"name": "Valtteri Bottas   ", "team": "Alfa Romeo", "rating": 9.29, "score": 0, "positions":[], "wins":0}
ric={"name": "Daniel Ricciardo  ", "team": "McLaren", "rating": 9.26, "score": 0, "positions":[], "wins":0}
gas={"name": "Pierre Gasly      ", "team": "AlphaTauri", "rating": 9.25, "score": 0, "positions":[], "wins":0}
mag={"name": "Kevin Magnussen   ", "team": "Haas", "rating": 9.22, "score": 0, "positions":[], "wins":0}
msc={"name": "Mick Schumacher   ", "team": "Haas", "rating": 9.16, "score": 0, "positions":[], "wins":0}
vet={"name": "Sebastian Vettel  ", "team": "Aston Martin", "rating": 9.22, "score": 0, "positions":[], "wins":0}
tsu={"name": "Yuki Tsunoda      ", "team": "AlphaTauri", "rating": 9.17, "score": 0, "positions":[], "wins":0}
zho={"name": "Zhou Guanyu       ", "team": "Alfa Romeo", "rating": 9.15, "score": 0, "positions":[], "wins":0}
str={"name": "Lance Stroll      ", "team": "Aston Martin", "rating": 9.18, "score": 0, "positions":[], "wins":0}
alb={"name": "Alexander Albon   ", "team": "Williams", "rating": 9.13, "score": 0, "positions":[], "wins":0}
lat={"name": "Nicholas Latifi   ", "team": "Williams", "rating": 9.04, "score": 0, "positions":[], "wins":0}

winners=[]
grid=[ver, per, lec, sai, rus, ham, nor, ric, alo, oco, bot, zho, gas, tsu, mag, msc, vet, str, alb, lat]
def grand_prix():
    for x in grid:
        standings=[]
        y=random.randint(1,20)
        if y==1:
            x["race"]=((x["rating"]) + 0.305)
        if y==2:
            x["race"]=((x["rating"]) +0.204)
        if y==3:
            x["race"]=((x["rating"]) +0.153)
        if y==4:
            x["race"]=((x["rating"]) +0.102)
        if y==5:
            x["race"]=((x["rating"]) +0.051)
        if y>5 and y<13:
            x["race"]=((x["rating"]) +0.0)
        if y==13:
            x["race"]=((x["rating"]) -0.101)
        if y==14:
            x["race"]=((x["rating"]) -0.202)
        if y==15:
            x["race"]=((x["rating"]) -0.303)
        if y==16:
            x["race"]=((x["rating"]) -0.404)
        if y==17:
            x["race"]=((x["rating"]) -0.605)
        if y>=18:
            x["race"]=((x["rating"]) -10.0)
      
    standings=sorted(grid, key= lambda z: z["race"], reverse=True)
    (standings[0]["score"]) += 25
    (standings[1]["score"]) += 18
    (standings[2]["score"]) += 15
    (standings[3]["score"]) += 12
    (standings[4]["score"]) += 10
    (standings[5]["score"]) += 8
    (standings[6]["score"]) += 6
    (standings[7]["score"]) += 4
    (standings[8]["score"]) += 2
    (standings[9]["score"]) += 1
    print("race results:")
    print()
    print("1. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["wins"]+=1
    standings[0]["positions"].append(1)
    winners.append(standings[0]['name'])
    del standings[0]
    print("2. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(2)
    del standings[0]
    print("3. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(3)
    del standings[0]
    print("4. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(4)
    del standings[0]
    print("5. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(5)
    del standings[0]
    print("6. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(6)
    del standings[0]
    print("7. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(7)
    del standings[0]
    print("8. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(8)
    del standings[0]
    print("9. ",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(9)
    del standings[0]
    print("10.",(max(standings, key=lambda z: z["race"])["name"]))
    standings[0]["positions"].append(10)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("11.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(11)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("12.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(12)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("13.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(13)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("14.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(14)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("15.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(15)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("16.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(16)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("17.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(17)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("18.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(18)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("19.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(19)
    del standings[0]
    if (max(standings, key=lambda z: z["race"])["race"]) <= 0:
        print("DNF",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append("DNF")
    else:
        print("20.",(max(standings, key=lambda z: z["race"])["name"]))
        standings[0]["positions"].append(20)
    print()
    print()
    input(("drivers standings:"))
    print()
    standings = sorted(grid, key= lambda z: z["score"], reverse=True)
    print("1. ",standings[0]["name"],standings[0]["score"])
    print("2. ",standings[1]["name"],standings[1]["score"])
    print("3. ",standings[2]["name"],standings[2]["score"])
    print("4. ",standings[3]["name"],standings[3]["score"])
    print("5. ",standings[4]["name"],standings[4]["score"])
    print("6. ",standings[5]["name"],standings[5]["score"])
    print("7. ",standings[6]["name"],standings[6]["score"])
    print("8. ",standings[7]["name"],standings[7]["score"])
    print("9. ",standings[8]["name"],standings[8]["score"])
    print("10.",standings[9]["name"],standings[9]["score"])
    print("11.",standings[10]["name"],standings[10]["score"])
    print("12.",standings[11]["name"],standings[11]["score"])
    print("13.",standings[12]["name"],standings[12]["score"])
    print("14.",standings[13]["name"],standings[13]["score"])
    print("15.",standings[14]["name"],standings[14]["score"])
    print("16.",standings[15]["name"],standings[15]["score"])
    print("17.",standings[16]["name"],standings[16]["score"])
    print("18.",standings[17]["name"],standings[17]["score"])
    print("19.",standings[18]["name"],standings[18]["score"])
    print("20.",standings[19]["name"],standings[19]["score"])
    print()
    print()
    input(("constructors standings:"))
    rb_score= ver["score"] + per["score"]
    ferrari_score= lec["score"] + sai["score"]
    merc_score= ham["score"] + rus["score"]
    alpine_score= alo["score"] + oco["score"]
    mclaren_score= nor["score"] + ric["score"]
    alfa_score= bot["score"] + zho["score"]
    at_score= gas["score"] + tsu["score"]
    haas_score= msc["score"] + mag["score"]
    aston_score= str["score"] + vet["score"]
    williams_score= lat["score"] + alb["score"]
    print()
    rb=      {"name": "Red Bull          ", "score": rb_score}
    ferrari ={"name": "Ferrari           ", "score": ferrari_score}
    merc    ={"name": "Mercedes          ", "score": merc_score}
    alpine  ={"name": "Alpine            ", "score": alpine_score}
    mclaren ={"name": "McLaren           ", "score": mclaren_score}
    alfa    ={"name": "Alfa Romeo        ", "score": alfa_score}
    at      ={"name": "AlphaTauri        ", "score": at_score}
    haas    ={"name": "Haas              ", "score": haas_score}
    aston   ={"name": "Aston Martin      ", "score": aston_score}
    williams={"name": "Williams          ", "score": williams_score}
    teams=[rb, ferrari, merc, alpine, mclaren, alfa, at, haas, aston, williams]
    teams_standings=sorted(teams, key= lambda z: z["score"], reverse=True)
    print("1. ",teams_standings[0]["name"],teams_standings[0]["score"])
    print("2. ",teams_standings[1]["name"],teams_standings[1]["score"])
    print("3. ",teams_standings[2]["name"],teams_standings[2]["score"])
    print("4. ",teams_standings[3]["name"],teams_standings[3]["score"])
    print("5. ",teams_standings[4]["name"],teams_standings[4]["score"])
    print("6. ",teams_standings[5]["name"],teams_standings[5]["score"])
    print("7. ",teams_standings[6]["name"],teams_standings[6]["score"])
    print("8. ",teams_standings[7]["name"],teams_standings[7]["score"])
    print("9. ",teams_standings[8]["name"],teams_standings[8]["score"])
    print("10.",teams_standings[9]["name"],teams_standings[9]["score"])
    print()
    print()
input(("Bahrain GP (1/22)"))
print()
grand_prix()
input(("Saudi Arabian GP (2/22)"))
print()
grand_prix()
input(("Australian GP (3/22)"))
print()
grand_prix()
input(("Emilia Romagna GP (4/22)"))
print()
grand_prix()
input(("Miami GP (5/22)"))
print()
grand_prix()
input(("Spanish GP (6/22)"))
print()
grand_prix()
input(("Monaco GP (7/22)"))
print()
grand_prix()
input(("Azerbaijan GP (8/22)"))
print()
grand_prix()
input(("Canadian GP (9/22)"))
print()
grand_prix()
input(("British GP (10/22)"))
print()
grand_prix()
input(("Austrian GP (11/22)"))
print()
grand_prix()
input(("French GP (12/22)"))
print()
grand_prix()
input(("Hungarian GP (13/22)"))
print()
grand_prix()
input(("Belgian GP (14/22)"))
print()
grand_prix()
input(("Dutch GP (15/22)"))
print()
grand_prix()
input(("Italian GP (16/22)"))
print()
grand_prix()
input(("Singapore GP (17/22)"))
print()
grand_prix()
input(("Japanese GP (18/22)"))
print()
grand_prix()
input(("United States GP (19/22)"))
print()
grand_prix()
input(("Mexico City GP (20/22)"))
print()
grand_prix()
input(("Sao Paulo GP (21/22)"))
print()
grand_prix()
input(("Abu Dhabi GP (22/22)"))
print()
grand_prix()

while True:
    print()
    x=input("Stats: ")
    print()
    if x == "win":
            for i in winners:
                print(i)
                print()
    if x == "ver":
        print(ver['name'])
        print(ver['team'])
        print("points:  ", ver["score"])
        print("wins:    ", ver["wins"])
        print("results: ", ver['positions'])
    if x == "per":
        print(per['name'])
        print(per['team'])
        print("points:  ", per["score"])
        print("wins:    ", per["wins"])
        print("results: ", per['positions'])
    if x == "lec":
        print(lec['name'])
        print(lec['team'])
        print("points:  ", lec["score"])
        print("wins:    ", lec["wins"])
        print("results: ", lec['positions'])
    if x == "sai":
        print(sai['name'])
        print(sai['team'])
        print("points:  ", sai["score"])
        print("wins:    ", sai["wins"])
        print("results: ", sai['positions'])
    if x == "rus":
        print(rus['name'])
        print(rus['team'])
        print("points:  ", rus["score"])
        print("wins:    ", rus["wins"])
        print("results: ", rus['positions'])
    if x == "ham":
        print(ham['name'])
        print(ham['team'])
        print("points:  ", ham["score"])
        print("wins:    ", ham["wins"])
        print("results: ", ham['positions'])
    if x == "nor":
        print(nor['name'])
        print(nor['team'])
        print("points:  ", nor["score"])
        print("wins:    ", nor["wins"])
        print("results: ", nor['positions'])
    if x == "lat":
        print(lat['name'])
        print(lat['team'])
        print("points:  ", lat["score"])
        print("wins:    ", lat["wins"])
        print("results: ", lat['positions'])
    if x == "oco":
        print(oco['name'])
        print(oco['team'])
        print("points:  ", oco["score"])
        print("wins:    ", oco["wins"])
        print("results: ", oco['positions'])
    if x == "gas":
        print(gas['name'])
        print(gas['team'])
        print("points:  ", gas["score"])
        print("wins:    ", gas["wins"])
        print("results: ", gas['positions'])
    if x == "alo":
        print(alo['name'])
        print(alo['team'])
        print("points:  ", alo["score"])
        print("wins:    ", alo["wins"])
        print("results: ", alo['positions'])
    if x == "str":
        print(str['name'])
        print(str['team'])
        print("points:  ", str["score"])
        print("wins:    ", str["wins"])
        print("results: ", str['positions'])
    if x == "vet":
        print(vet['name'])
        print(vet['team'])
        print("points:  ", vet["score"])
        print("wins:    ", vet["wins"])
        print("results: ", vet['positions'])
    if x == "tsu":
        print(tsu['name'])
        print(tsu['team'])
        print("points:  ", tsu["score"])
        print("wins:    ", tsu["wins"])
        print("results: ", tsu['positions'])
    if x == "bot":
        print(bot['name'])
        print(bot['team'])
        print("points:  ", bot["score"])
        print("wins:    ", bot["wins"])
        print("results: ", bot['positions'])
    if x == "zho":
        print(zho['name'])
        print(zho['team'])
        print("points:  ", zho["score"])
        print("wins:    ", zho["wins"])
        print("results: ", zho['positions'])
    if x == "msc":
        print(msc['name'])
        print(msc['team'])
        print("points:  ", msc["score"])
        print("wins:    ", msc["wins"])
        print("results: ", msc['positions'])
    if x == "mag":
        print(mag['name'])
        print(mag['team'])
        print("points:  ", mag["score"])
        print("wins:    ", mag["wins"])
        print("results: ", mag['positions'])
    if x == "alb":
        print(alb['name'])
        print(alb['team'])
        print("points:  ", alb["score"])
        print("wins:    ", alb["wins"])
        print("results: ", alb['positions'])
    if x == "ric":
        print(ric['name'])
        print(ric['team'])
        print("points:  ", ric["score"])
        print("wins:    ", ric["wins"])
        print("results: ", ric['positions'])