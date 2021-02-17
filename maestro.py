import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

C = pd.read_csv("Data_C.csv", delimiter=';', decimal=',')
C['Year'] = 2020
C['Date'] = pd.to_datetime(C[['Day', 'Month', 'Year']])
C = C.drop(columns=['Day', 'Month', 'Year'])

dates = C['Date'].value_counts().index # get the unique dates
dates = dates.sort_values()
                    
player_5 = C[C['Player']==4]
x = player_5.loc[player_5['Date']=='2020-10-07']['headz'].plot()
y = player_5.loc[player_5['Date']=='2020-10-07']['camz'].plot()

#plt.plot(x,y)
plt.show()

sns.pairplot(player_5[['camx', 'camy', 'camz']], height=2.5)
g=sns.pairplot(player_5[['headx', 'heady', 'headz']], height=2.5)
#g.axes.set_ylim((-2,2))
g.add_legend()

# compute polar plot
# Compute areas and colors
def polar_view(data):
    norm = np.sqrt(data[:,0]**2 + data[:,1]**2) 
    r = norm
    theta = np.arccos((data[:,0] * data[:,1]) / norm)
    area = 2 * r**2
    colors = theta
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='polar')
    # ax.scatter(theta, r, c=colors, s=area, cmap='twilight_shifted', alpha=0.75)
    # ax.set_thetamin(-10)
    # ax.set_thetamax(190)
    

fig, ax = plt.subplots(12,2, figsize=(15,40), subplot_kw=dict(polar=True))

for i, date in enumerate(dates):
    data = C[C['Date'] == date]
    data = data[['camx','camy', 'camz']].values
    norm = np.sqrt(data[:,0]**2 + data[:,1]**2) #polar conversion
    y = [0,1]
    # norm = np.sqrt(data[:,0]**2 + data[:,1]**2) * np.sqrt(y[0]**2 + y[1]**2)
    r = norm
    theta = np.arctan2(data[:,0], data[:,1]) #polar conversion
    # theta = np.arccos((data[:,0:2] * y)[:,1] / norm)
    area = 2 * r**2
    colors = theta + data[:,2]
    ax[i,0].scatter(theta, r, c=colors, s=area, cmap='PuOr', alpha=0.75)
    # ax[i,0].set_thetamin(-10)
    # ax[i,0].set_thetamax(190)
    ax[i,0].set_title(str(date) + ': Cam')

for i, date in enumerate(dates):
    data = C[C['Date'] == date]
    data = data[['headx','heady', 'headz']].values
    norm = np.sqrt(data[:,0]**2 + data[:,1]**2) 
    r = norm
    theta = np.arccos((data[:,0] * data[:,1]) / norm)
    area = 2 * r**2
    colors = theta + data[:,2]
    ax[i,1].scatter(theta, r, c=colors, s=area, cmap='PuOr', alpha=0.75)
    ax[i,1].set_thetamin(-10)
    ax[i,1].set_thetamax(190)
    ax[i,1].set_title(str(date) + ': Head')
    
plt.suptitle('Cummulative Movement of Head and Cam in x-y-Plane')
plt.tight_layout()
plt.savefig("plots/" + 'cummulative_polar_new.jpg', dpi=300, format = 'jpeg')

'''
# schwierig einen Trainingseffekt zu kalkuliere
# man könnte einen gemittelten ROM über alle Missionen machen, um Aussagen über die 
Wirksamkeit des Spiels zu treffen; dafür müsste man die Daten filtern, so dass die Zuordnung
Spieler -- Mission -- Tag als MW genommen wird
# Die Daten von VP1 sollte nicht verwendet werden, da Abbruch 
# Pattern Kopf sieht sehr nach Suche aus
# Pattern CAM sieht sehr nach zielgerichteter Bewegung aus (hier könnte man nach zeitlicher
Abfolge Suche --> Zielen schauen)
# checking for correlations
# Ausmaß statischer Haltung und Bewegung für Kopf und Hand
# Polar Häufungs Plot für Beweguns (ginge auch für 3D-Bewegungsvektor)
würde ich aber eher in 2D-Ebene machen als Kummulation / radial heatmap
# welche Einheit haben die Koordinatenangaben
# PLOT: alle MWs pro Datum, gemittelt; links Kopf, rechts cam
# Calibration globales Koordinatensystem
# Missionsbeschreibung
# Gamestates
'''