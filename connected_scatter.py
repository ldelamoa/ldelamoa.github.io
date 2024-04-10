import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Creem un dataset que ens serveixi d'exemple
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
online_hotel_revenue = np.array([5e9, 10e9, 15e9, 20e9, 25e9, 30e9, 40e9, 35e9, 30e9, 40e9, 50e9, 55e9, 50e9, 60e9, 65e9])
number_of_travel_agents = [119000, 117000, 116000, 114000, 112000, 110000, 108000, 106000, 104000, 102000, 100000, 98000, 96000, 94000, 92000]

# Format dels eixos x i y per la gràfica
online_hotel_revenue_billions = online_hotel_revenue / 1e9

def billions_formatter(x, pos):
    return f'${int(x)}B'

def thousands_formatter(x, pos):
    return f'{int(x/1000)}K'

# Creem el plot
plt.figure(figsize=(12, 6))
plt.plot(online_hotel_revenue_billions, number_of_travel_agents, 'o-', color='darkgreen', markersize=8)

ax = plt.gca()
ax.xaxis.set_major_formatter(FuncFormatter(billions_formatter))
ax.yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

# Eliminem el límit superior i de la dreta, i afegim grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Unim les dades
for (revenue, agents, year) in zip(online_hotel_revenue_billions, number_of_travel_agents, years):
    plt.annotate(year, xy=(revenue, agents), textcoords="offset points", xytext=(5,10), ha='center')

# Afegim títols, guardem el plot i el mostrem
plt.title('Beneficis online hotel vs Número d\'agències de viatges', fontsize=20, pad = '30.0')
plt.xlabel('Beneficis online hotel (€)', fontsize=10)
plt.ylabel('Número d\'agències de viatges', fontsize=10)

plt.savefig('beneficis_hotel.png', bbox_inches='tight', facecolor='white')

plt.show()