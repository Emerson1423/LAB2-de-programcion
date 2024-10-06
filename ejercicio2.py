"""
https://www.kaggle.com/datasets/gregorut/videogamesales

"""


import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
# Asegúrate de cambiar la ruta a donde tengas tu archivo CSV
df = pd.read_csv('vgsales.csv')

# Contar cuántos juegos hay por plataforma
juegosp = df['Platform'].value_counts()

# Crear el gráfico de líneas
plt.plot(juegosp.index, juegosp.values)
juegosp.plot(marker='o',color='green')


plt.title('Número de juegos por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Número de juegos')

# activa la visualización de una cuadrícula en el gráfico. Esto significa 
# que se mostrarán líneas de guía horizontales y verticales a lo largo del gráfico, 
# lo que facilita la lectura de los valores en los ejes.
plt.grid(color='black', linestyle='--', linewidth=0.5)
#ajustar los graficos
plt.xticks(rotation=45, ha='right')

# Mostrar el gráfico
plt.show()

"""
El gráfico de línea muestra el número de juegos por plataforma. Se observa que la Nintendo DS es la plataforma con mayor cantidad de juegos, 
superando los 2000 títulos. Le siguen la PlayStation 2 y la PlayStation 3, 
ambas con un número considerable de juegos, lo que refleja su popularidad y amplio catálogo.

Por otro lado, plataformas más antiguas o menos populares como PC-FX, GG, y TG16 tienen una cantidad muy baja de juegos, 
lo que podría deberse a su menor duración en el mercado o su limitada adopción por parte de los usuarios.
"""
