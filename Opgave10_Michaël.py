import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import xlrd

data = pd.read_excel("voetbal.xlsx", sheetname="gegevens")

#lees de data voor posities en goals in
posities = data['positie']
goals = data['aantal gemaakte goalen']

#selecteer de goals voor de gewenste posities
goalsPerPositie = [[],[],[]]
for x in range(0, len(posities)):
    if posities[x] == "linkervleugel":
        goalsPerPositie[0].append(goals[x])
    if posities[x] == "rechtervleugel":
        goalsPerPositie[1].append(goals[x])
    if posities[x] == "piloot":
        goalsPerPositie[2].append(goals[x])
#print(goalsPerPositie)

boxplotdata = [goalsPerPositie[0], goalsPerPositie[1], goalsPerPositie[2]]
fig1, ax1 = plt.subplots()
ax1.set_title('Boxplot')
plt.boxplot(boxplotdata)

# Blijkbaar gaat het zo simpel ook voor alle data (dus wel keeper en staart erbij)
# data.boxplot(column='aantal gemaakte goalen', by='positie')

plt.show()

## Kutcode, niet naar kijken aub
#
#
#
#
"""spreadLinker = max(goalsPerPositie[0] - min(goalsPerPositie[0]))
spreadRechter = max(goalsPerPositie[1] - min(goalsPerPositie[1]))
spreadPiloot = max(goalsPerPositie[2] - min(goalsPerPositie[2]))
spread = [spreadLinker, spreadRechter, spreadPiloot]
print(spread)
centerPiloot = np.median(goalsPerPositie[2])
centerLinker = np.median(goalsPerPositie[0])
centerRechter = np.median(goalsPerPositie[1])
center = [centerLinker, centerRechter, centerPiloot]
print(center)
flier_highLinker = max(goalsPerPositie[0])
flier_highRechter = max(goalsPerPositie[1])
flier_highPiloot = max(goalsPerPositie[2])
flier_high = [flier_highLinker, flier_highRechter, flier_highPiloot]

flier_lowLinker = min(goalsPerPositie[0])
flier_lowRechter = min(goalsPerPositie[1])
flier_lowPiloot = min(goalsPerPositie[2])
flier_low = [flier_lowLinker, flier_lowRechter, flier_lowPiloot]

allData = np.concatenate((spread, center, flier_high, flier_low))
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(allData)"""