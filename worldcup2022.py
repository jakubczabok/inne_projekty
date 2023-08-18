import random
import sys
import os
import pprint
import operator
import time

os.system("cls")
qat={'name': 'Qatar         ', 'rating': 9.6, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
ecu={'name': 'Ecuador       ', 'rating': 9.59, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
sen={'name': 'Senegal       ', 'rating': 9.72, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
ned={'name': 'Netherlands   ', 'rating': 9.7, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
a=[qat, ecu, sen, ned]
eng={'name': 'England       ', 'rating': 9.85, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
ira={'name': 'Iran          ', 'rating': 9.68, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
usa={'name': 'United States ', 'rating': 9.76, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
wls={'name': 'Wales         ', 'rating': 9.65, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
b=[eng, ira, usa, wls]
arg={'name': 'Argentina     ', 'rating': 9.98, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
sau={'name': 'Saudi Arabia  ', 'rating': 9.45, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
mex={'name': 'Mexico        ', 'rating': 9.84, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
pol={'name': 'Poland        ', 'rating': 9.64, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
c=[arg, sau, mex, pol]
fra={'name': 'France        ', 'rating': 9.93, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
aus={'name': 'Australia     ', 'rating': 9.63, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
den={'name': 'Denmark       ', 'rating': 9.74, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
tun={'name': 'Tunisia       ', 'rating': 9.55, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
d=[fra,aus,den,tun]
spa={'name': 'Spain         ', 'rating': 9.82, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
cos={'name': 'Costa Rica    ', 'rating': 9.74, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
ger={'name': 'Germany       ', 'rating': 9.87, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
jpn={'name': 'Japan         ', 'rating': 9.71, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
e=[spa, cos, ger, jpn]
bel={'name': 'Belgium       ', 'rating': 9.94, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
can={'name': 'Canada        ', 'rating': 9.56, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
mor={'name': 'Morocco       ', 'rating': 9.56, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
cro={'name': 'Croatia       ', 'rating': 9.83, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
f=[bel,can,mor,cro]
bra={'name': 'Brazil        ', 'rating': 10.0, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
srb={'name': 'Serbia        ', 'rating': 9.48, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
sui={'name': 'Switzerland   ', 'rating': 9.8, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
cmr={'name': 'Cameroon      ', 'rating': 9.55, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
g=[bra,srb,sui,cmr]
por={'name': 'Portugal      ', 'rating': 9.82, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
gha={'name': 'Ghana         ', 'rating': 9.4, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
urg={'name': 'Uruguay       ', 'rating': 9.83, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
kor={'name': 'South Korea   ', 'rating': 9.71, 'score': 0, 'goals+': 0, 'goals-': 0, '+-': 0}
h=[por,gha,urg,kor]

top8=[]

def match(SP, CP):
    
    goals=0
    x1=random.randint(1,6)
    if x1==3:
        goals+=1
    if x1==4:
        goals+=2
    if x1==5:
        goals+=3
    if x1==6:
        goals+=4
    x2=random.randint(1,6)
    if x2==3:
        goals+=1
    if x2==4:
        goals+=2
    if x2==5:
        goals+=3
    if x2==6:
        goals+=4
    team1score=0
    team2score=0
    while goals>0:
        x3=random.randint(1,6)
        x4=random.randint(1,6)
        if x3==1:
            SP['new_rating']=SP['rating']+0.3
        if x3==2:
            SP['new_rating']=SP['rating']+0.15
        if x3==3:
            SP['new_rating']=SP['rating']+0.05
        if x3==4:
            SP['new_rating']=SP['rating']-0.05
        if x3==5:
            SP['new_rating']=SP['rating']-0.15
        if x3==6:
            SP['new_rating']=SP['rating']-0.3
        if x4==1:
            CP['new_rating']=CP['rating']+0.3
        if x4==2:
            CP['new_rating']=CP['rating']+0.15
        if x4==3:
            CP['new_rating']=CP['rating']+0.05
        if x4==4:
            CP['new_rating']=CP['rating']-0.05
        if x4==5:
            CP['new_rating']=CP['rating']-0.15
        if x4==6:
            CP['new_rating']=CP['rating']-0.3
        if SP['new_rating']>CP['new_rating']:
            team1score+=1
        if CP['new_rating']>SP['new_rating']:
            team2score+=1
        goals-=1
    

    SP['goals+']+=team1score
    SP['goals-']+=team2score
    SP['+-']=SP['goals+']-SP['goals-']
    CP['goals+']+=team2score
    CP['goals-']+=team1score
    CP['+-']=CP['goals+']-CP['goals-']

    print(SP['name'] + str(team1score))
    print(CP['name'] + str(team2score))
    if team1score>team2score:
        SP['score']+=3
    if team2score>team1score:
        CP['score']+=3
    if team1score==team2score:
        SP['score']+=1
        CP['score']+=1


def playoff(SP, CP):
    global top8
    goals=0
    x1=random.randint(1,6)
    if x1==3:
        goals+=1
    if x1==4:
        goals+=2
    if x1==5:
        goals+=3
    if x1==6:
        goals+=4
    x2=random.randint(1,6)
    if x2==3:
        goals+=1
    if x2==4:
        goals+=2
    if x2==5:
        goals+=3
    if x2==6:
        goals+=4
    team1score=0
    team2score=0
    while goals>0:
        x3=random.randint(1,6)
        x4=random.randint(1,6)
        if x3==1:
            SP['new_rating']=SP['rating']+0.3
        if x3==2:
            SP['new_rating']=SP['rating']+0.15
        if x3==3:
            SP['new_rating']=SP['rating']+0.05
        if x3==4:
            SP['new_rating']=SP['rating']-0.05
        if x3==5:
            SP['new_rating']=SP['rating']-0.15
        if x3==6:
            SP['new_rating']=SP['rating']-0.3
        if x4==1:
            CP['new_rating']=CP['rating']+0.3
        if x4==2:
            CP['new_rating']=CP['rating']+0.15
        if x4==3:
            CP['new_rating']=CP['rating']+0.05
        if x4==4:
            CP['new_rating']=CP['rating']-0.05
        if x4==5:
            CP['new_rating']=CP['rating']-0.15
        if x4==6:
            CP['new_rating']=CP['rating']-0.3
        if SP['new_rating']>CP['new_rating']:
            team1score+=1
        if CP['new_rating']>SP['new_rating']:
            team2score+=1
        goals-=1
    if team1score!=team2score:
        
        print(SP['name'] + str(team1score))
        print(CP['name'] + str(team2score))
        if team1score>team2score:
            top8.append(SP)
        else:
            top8.append(CP)
    
    
        
    else:
        
        team3score=team1score
        team4score=team2score
        goals=0
        x5=random.randint(1,6)
        if x5==3:
            goals+=1
        if x5==4:
            goals+=2
        if x5==5:
            goals+=3
        if x5==6:
            goals+=4
        
        while goals>0:
            x3=random.randint(1,6)
            x4=random.randint(1,6)
            if x3==1:
                SP['new_rating']=SP['rating']+0.3
            if x3==2:
                SP['new_rating']=SP['rating']+0.15
            if x3==3:
                SP['new_rating']=SP['rating']+0.05
            if x3==4:
                SP['new_rating']=SP['rating']-0.05
            if x3==5:
                SP['new_rating']=SP['rating']-0.15
            if x3==6:
                SP['new_rating']=SP['rating']-0.3
            if x4==1:
                CP['new_rating']=CP['rating']+0.3
            if x4==2:
                CP['new_rating']=CP['rating']+0.15
            if x4==3:
                CP['new_rating']=CP['rating']+0.05
            if x4==4:
                CP['new_rating']=CP['rating']-0.05
            if x4==5:
                CP['new_rating']=CP['rating']-0.15
            if x4==6:
                CP['new_rating']=CP['rating']-0.3
            if SP['new_rating']>CP['new_rating']:
                team3score+=1
            if CP['new_rating']>SP['new_rating']:
                team4score+=1
            goals-=1
        if team3score!=team4score:
            print(SP['name'] + str(team1score)+" "+str(team3score))
            print(CP['name'] + str(team2score)+" "+str(team4score))
            if team3score>team4score:
                top8.append(SP)
            else:
                top8.append(CP)
        else:
            pen1=0
            pen2=0
            y1=random.randint(1,3)
            if y1>1:
                pen1+=1
            z1=random.randint(1,3)
            if z1>1:
                pen2+=1
            y1=random.randint(1,3)
            if y1>1:
                pen1+=1
            z1=random.randint(1,3)
            if z1>1:
                pen2+=1
            y1=random.randint(1,3)
            if y1>1:
                pen1+=1
            z1=random.randint(1,3)
            if z1>1:
                pen2+=1
            if pen1-pen2==3 or pen2-pen1==3:
                print(SP['name'] + str(team1score)+" "+str(team3score)+" "+str(pen1)+"p")
                print(CP['name'] + str(team2score)+" "+str(team4score)+" "+str(pen2)+"p")
                if pen1>pen2:
                    top8.append(SP)
                else:
                    top8.append(CP)
            else:
                y1=random.randint(1,3)
                if y1>1:
                    pen1+=1
                z1=random.randint(1,3)
                if z1>1:
                    pen2+=1
                if pen1-pen2==2 or pen2-pen1==2:
                    print(SP['name'] + str(team1score)+" "+str(team3score)+" "+str(pen1)+"p")
                    print(CP['name'] + str(team2score)+" "+str(team4score)+" "+str(pen2)+"p")
                    if pen1>pen2:
                        top8.append(SP)
                    else:
                        top8.append(CP)
                else:
                    y1=random.randint(1,3)
                    if y1>1:
                        pen1+=1
                    z1=random.randint(1,3)
                    if z1>1:
                        pen2+=1
                    if pen1!=pen2:
                        print(SP['name'] + str(team1score)+" "+str(team3score)+" "+str(pen1)+"p")
                        print(CP['name'] + str(team2score)+" "+str(team4score)+" "+str(pen2)+"p")
                        if pen1>pen2:
                            top8.append(SP)
                        else:
                            top8.append(CP)
                    else:
                        while pen1==pen2:
                            y1=random.randint(1,3)
                            if y1>1:
                                pen1+=1
                            z1=random.randint(1,3)
                            if z1>1:
                                pen2+=1
                        print(SP['name'] + str(team1score)+" "+str(team3score)+" "+str(pen1)+"p")
                        print(CP['name'] + str(team2score)+" "+str(team4score)+" "+str(pen2)+"p")
                        if pen1>pen2:
                            top8.append(SP)
                        else:
                            top8.append(CP)
        



                

        
        




def table(D):
    teams_standings=sorted(D, key= lambda z: z["goals+"], reverse=True)
    teams_standings=sorted(teams_standings, key= lambda z: z["+-"], reverse=True)
    teams_standings=sorted(teams_standings, key= lambda z: z["score"], reverse=True)
    D=teams_standings

    
    print("1. ",teams_standings[0]["name"]," ",teams_standings[0]["score"],"p   ",teams_standings[0]["goals+"],"",teams_standings[0]["goals-"])
    print("2. ",teams_standings[1]["name"], " ",teams_standings[1]["score"],"p   ",teams_standings[1]["goals+"],"",teams_standings[1]["goals-"])
    print("3. ",teams_standings[2]["name"], " ",teams_standings[2]["score"], "p   ",teams_standings[2]["goals+"],"",teams_standings[2]["goals-"])
    print("4. ",teams_standings[3]["name"], " ",teams_standings[3]["score"], "p   ",teams_standings[3]["goals+"],"",teams_standings[3]["goals-"])


input("Group stage: round 1 ") 
print()                           
match(a[0], a[1])
input("")
match(a[2], a[3])
print()
input("Group A table ")
print()
table(a)
print()
input("")
match(b[0], b[1])
input("")
match(b[2], b[3])
print()
input("Group B table ")
print()
table(b)
print()
input("")
match(c[0], c[1])
input("")
match(c[2], c[3])
print()
input("Group C table ")
print()
table(c)
print()
input("")
match(d[0], d[1])
input("")
match(d[2], d[3])
print()
input("Group D table ")
print()
table(d)
print()
input("")
match(e[0], e[1])
input("")
match(e[2], e[3])
print()
input("Group E table ")
print()
table(e)
print()
input("")
match(f[0], f[1])
input("")
match(f[2], f[3])
print()
input("Group F table ")
print()
table(f)
print()
input("")
match(g[0], g[1])
input("")
match(g[2], g[3])
print()
input("Group G table ")
print()
table(g)
print()
input("")
match(h[0], h[1])
input("")
match(h[2], h[3])
print()
input("Group H table ")
print()
table(h)
print()

input("Group stage: round 2 ") 
print()                           
match(a[0], a[2])
input("")
match(a[1], a[3])
print()
input("Group A table ")
print()
table(a)
print()
input("")
match(b[0], b[2])
input("")
match(b[1], b[3])
print()
input("Group B table ")
print()
table(b)
print()
input("")
match(c[0], c[2])
input("")
match(c[1], c[3])
print()
input("Group C table ")
print()
table(c)
print()
input("")
match(d[0], d[2])
input("")
match(d[1], d[3])
print()
input("Group D table ")
print()
table(d)
print()
input("")
match(e[0], e[2])
input("")
match(e[1], e[3])
print()
input("Group E table ")
print()
table(e)
print()
input("")
match(f[0], f[2])
input("")
match(f[1], f[3])
print()
input("Group F table ")
print()
table(f)
print()
input("")
match(g[0], g[2])
input("")
match(g[1], g[3])
print()
input("Group G table ")
print()
table(g)
print()
input("")
match(h[0], h[2])
input("")
match(h[1], h[3])
print()
input("Group H table ")
print()
table(h)
print()

input("Group stage: round 3 ") 
print()                           
match(a[0], a[3])
input("")
match(a[1], a[2])
print()
input("Group A table ")
print()
table(a)
print()
input("")
match(b[0], b[3])
input("")
match(b[1], b[2])
print()
input("Group B table ")
print()
table(b)
print()
input("")
match(c[0], c[3])
input("")
match(c[1], c[2])
print()
input("Group C table ")
print()
table(c)
print()
input("")
match(d[0], d[3])
input("")
match(d[1], d[2])
print()
input("Group D table ")
print()
table(d)
print()
input("")
match(e[0], e[3])
input("")
match(e[1], e[2])
print()
input("Group E table ")
print()
table(e)
print()
input("")
match(f[0], f[3])
input("")
match(f[1], f[2])
print()
input("Group F table ")
print()
table(f)
print()
input("")
match(g[0], g[3])
input("")
match(g[1], g[2])
print()
input("Group G table ")
print()
table(g)
print()
input("")
match(h[0], h[3])
input("")
match(h[1], h[2])
print()
input("Group H table ")
print()
table(h)
print()

a=sorted(a, key= lambda z: z["goals+"], reverse=True)
a=sorted(a, key= lambda z: z["+-"], reverse=True)
a=sorted(a, key= lambda z: z["score"], reverse=True)
b=sorted(b, key= lambda z: z["goals+"], reverse=True)
b=sorted(b, key= lambda z: z["+-"], reverse=True)
b=sorted(b, key= lambda z: z["score"], reverse=True)
c=sorted(c, key= lambda z: z["goals+"], reverse=True)
c=sorted(c, key= lambda z: z["+-"], reverse=True)
c=sorted(c, key= lambda z: z["score"], reverse=True)
d=sorted(d, key= lambda z: z["goals+"], reverse=True)
d=sorted(d, key= lambda z: z["+-"], reverse=True)
d=sorted(d, key= lambda z: z["score"], reverse=True)
e=sorted(e, key= lambda z: z["goals+"], reverse=True)
e=sorted(e, key= lambda z: z["+-"], reverse=True)
e=sorted(e, key= lambda z: z["score"], reverse=True)
f=sorted(f, key= lambda z: z["goals+"], reverse=True)
f=sorted(f, key= lambda z: z["+-"], reverse=True)
f=sorted(f, key= lambda z: z["score"], reverse=True)
g=sorted(g, key= lambda z: z["goals+"], reverse=True)
g=sorted(g, key= lambda z: z["+-"], reverse=True)
g=sorted(g, key= lambda z: z["score"], reverse=True)
h=sorted(h, key= lambda z: z["goals+"], reverse=True)
h=sorted(h, key= lambda z: z["+-"], reverse=True)
h=sorted(h, key= lambda z: z["score"], reverse=True)








input("Round of 16 ") 
print() 
playoff(a[0], b[1])
input("")
playoff(c[0], d[1])
input("")
playoff(e[0], f[1])
input("")
playoff(g[0], h[1])
input("")
playoff(b[0], a[1])
input("")
playoff(d[0], c[1])
input("")
playoff(f[0], e[1])
input("")
playoff(h[0], g[1])
print()

input("Quarter-finals ") 
print() 
playoff(top8[0], top8[1])
input("")
playoff(top8[2], top8[3])
input("")
playoff(top8[4], top8[5])
input("")
playoff(top8[6], top8[7])
print()

input("Semi-finals ") 
print() 
playoff(top8[8], top8[9])
input("")
playoff(top8[10], top8[11])
print()

input("Third place play-off ") 
print()
thirdpoff=[]
if top8[12]==top8[8]:
    thirdpoff.append(top8[9])
else:
    thirdpoff.append(top8[8])
if top8[13]==top8[10]:
    thirdpoff.append(top8[11])
else:
    thirdpoff.append(top8[10])
playoff(thirdpoff[0], thirdpoff[1])
print()
input("Final ") 
print()
playoff(top8[12], top8[13])
print()








