import numpy as np
import pandas as pd
import datetime 
from matplotlib import pyplot as plt
from statistics import mode

data = pd.read_excel('voetbal.xlsx')
data.head()

start = pd.to_datetime('2011-01-01')
end = pd.to_datetime('2011-12-31')
start_u = start.value//10**9
end_u = end.value//10**9
cat1_date = pd.to_datetime('2011-04-01')
cat2_date = pd.to_datetime('2011-10-01')

for x, row in data.iterrows():
    y= (pd.to_datetime(np.random.randint(start_u, end_u), unit='s'))
    data.at[x, 'geboortedatum'] = datetime.date(y.year, y.month, y.day)
    inzet_text='matig'
    if y < cat1_date:
        inzet_text = 'zeer goed'
    elif y < cat2_date:
            inzet_text = 'goed'
    data.at[x,'inzet'] = str(inzet_text)
data.head()

gewicht_gesorteerd = sorted(set(data.gewicht))
for x in gewicht_gesorteerd:
    y=data[data.gewicht == x]
    plt.scatter(y.gewicht, y.lengte)
plt.xlim(19,31)
plt.ylim(110,140)
plt.xlabel('gewicht')
plt.ylabel('lengte')
plt.show()

sum_array = {}
per_categorie ={}
player_per_position={}
for position in data['positie']:
    sum_array[position]=0
    player_per_position[position]=0
for x, row in data.iterrows():
    position=data.at[x, 'positie']
    sum_array[position]=sum_array[position]+ data.at[x, 'aantal gemaakte goalen']
    player_per_position[position]=player_per_position[position] + 1
x = list(sum_array.keys())
y = list(sum_array.values())
plt.bar(x,y)
plt.xlabel("Posities")
plt.ylabel("Aantal goals gescoord")
plt.title("Goals per positie")
plt.xticks(list(sum_array.keys()),list(sum_array.keys()), rotation='vertical')
plt.show()
#Opdracht 6
modus_array={}
average_goals_position={}
for position in sum_array.keys():   
    average_goals_position[position]=sum_array[position] / player_per_position[position]
    modus_array[position] = []
    print(average_goals_position[position])
    
for x, row in data.iterrows():
    position = data.at[x, 'positie']
    modus_array[position].append(data.at[x,'aantal gemaakte goalen'])
    
for key in modus_array.keys():
    print ('Mode for ' + key + ': ' + str((mode(modus_array[key]))))
