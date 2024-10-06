"""
https://www.kaggle.com/datasets/saurabhshahane/road-traffic-accidents

"""

import pandas as pd
import matplotlib.pyplot as plt
    
df = pd.read_csv('RTA Dataset.csv')

# Eliminar valores 'Unknown' o similares
df = df[df['Age_band_of_driver'] != 'Unknown']

# Contar cuántos registros hay en cada banda de edad
edad = df['Age_band_of_driver'].value_counts()

plt.pie(edad.values, labels=edad.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink', 'purple'])

# Añadir título
plt.title('Distribución de conductores por rango de edad')

# Asegurar que el gráfico sea circular


plt.show()

"""
Analizis del dataset
El objetivo del dataset es recopilar información sobre la edad de los conductores involucrados en accidentes.
 El gráfico de pastel muestra que el grupo con mayor frecuencia de accidentes es el de 18-30 años, representando un 39.7%. 
 Esto puede deberse a la inexperiencia o mayor uso de vehículos.

a diferencia en , el grupo con menor frecuencia de accidentes son los menores de 18 años, con un 7.7%.
Esto podría explicarse por la menor cantidad de conductores en ese grupo de edad. Los demás grupos muestran una distribución más equilibrada,
destacando que los conductores de 31-50 años también tienen una participación significativa, con un 38%.


"""