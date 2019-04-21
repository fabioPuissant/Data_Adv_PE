import os 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import xlrd

path='/Users/Work/Documents/TIN2/Data Advanced/PE/voetbal'
os.chdir(path)
cwd = os.getcwd()
data = pd.read_excel("voetbal.xlsx", sheetname="gegevens")
naam = data["naam"]
positie = data["positie"].unique()
col = {'staart':'red', 'linkervleugel':'blue', 'rechtervleugel':'green','piloot':'black', 'keeper':'yellow'}
colors = data['positie'].apply(lambda x: col[x])
goals = data["aantal gemaakte goalen"]
geboortedatum = data["geboortedatum"]
inzet = data['inzet']
gewicht = data['gewicht']
lengte = data["lengte"]
aantalSpelers = len(naam)

plt.scatter(gewicht, lengte, s=(goals*200)+100, alpha=0.4, c=colors)
##plt.legend(('staart','linkervleugel', 'rechtervleugel', 'piloot', 'keeper'), ('red', 'blue', 'green', 'black', 'yellow'), loc='upper left')
##s=goals voor punten groter te maken naargelang aantal goals
##c=positie geeft iederen positie een kleur

##plt.bar(goals, positie, width=0.8)
## voor staafdiagrammen
for i in range(aantalSpelers):
    if goals[i] >= 3:
        plt.text(gewicht[i],lengte[i]+0.1,naam[i][6:]).set_fontsize(10)
 ##label iedere dot met zijn positie, +0.1 om iets boven dot uit te komen
 ##fontsize aanpassen aan goals
plt.xlabel("Gewicht")
plt.ylabel("Lengte")

l1 = plt.scatter(20, 135, alpha=0.6, c = 'red')
l2 = plt.scatter(20, 135, alpha=0.6, c = 'blue')
l3 = plt.scatter(20, 135, alpha=0.6, c = 'green')
l4 = plt.scatter(20, 135, alpha=0.6, c = 'black')
l5 = plt.scatter(20, 135, alpha=0.6, c = 'yellow')
plt.legend((l1, l2, l3, l4, l5), ('Staart', 'Linkervleugel', 'Rechtervleugel', 'Piloot', 'Keeper'), loc='upper left')

plt.show()