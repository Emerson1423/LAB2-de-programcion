import pandas as pd
import matplotlib.pyplot as plt
    
df = pd.read_csv('imdb_top_1000.csv')

# Contar cuántas películas hay por género
# Como algunos registros pueden tener múltiples géneros separados por comas, necesitamos desglosar eso
generos = df['Genre'].str.split(', ', expand=True).stack().value_counts()

colors = ['skyblue', 'lightgreen', 'orange', 'pink', 'yellow', 'lightcoral', 
          'lightgrey', 'mediumpurple', 'lightgoldenrodyellow', 'plum', 'limegreen',
          'cornflowerblue', 'khaki', 'salmon', 'palevioletred', 'mediumseagreen',
          'gold', 'deepskyblue', 'tomato', 'slateblue', 'powderblue']

# Crear el gráfico de barras
plt.bar(generos.index,generos.values, color=colors)

# Añadir títulos y etiquetas
plt.title('cantidas de peliculas por generos')
plt.xlabel('Género')
plt.ylabel('cantida de películas')
# Ajustar el gráfico
plt.xticks(rotation=45, ha='right')
# Mostrar el gráfico

plt.tight_layout()
plt.show()

"""
El gráfico de barras muestra el desglose de películas por género. El género más dominante es el drama con más de 700 películas, 
lo que demuestra su popularidad y frecuencia en la industria cinematográfica. Le siguen las comedias, los dramas policiales y las películas de aventuras,
cada una con unas 200 películas, lo que también demuestra su alto reconocimiento en la sociedad.

al contrario de , los géneros menos representados incluyen Musical, Sport, y Film-Noir, 
que tienen una cantidad muy reducida de películas, posiblemente debido a su nicho más específico y menor demanda.
"""
