import streamlit
import pandas
import numpy
import datetime
import matplotlib.pyplot
from datetime import time

streamlit.title('**Proyecto Final - Programación Avanzada**')

df = pandas.read_csv('datos_horarios_contaminacion_lima.csv', sep = ',')

streamlit.subheader('**Integrantes:**')

streamlit.write('- Ames Anapán José Manuel')
streamlit.write('- Casimiro Beteta Arnorld Uriel')
streamlit.write('- Carpio Peralta Joaquín Felipe')
streamlit.write('- Salazar Leon Sergio Leoncio')
streamlit.write('- Torres Linares Maricielo Jazmin')

streamlit.write('La contaminación del aire es uno de los mayores riesgos ambientales que existen para la salud.',
				'Los grupos de población y localidades geográficas influyen en la contaminación al aire.',
				'Según la OMS más de 150 millones de personas en América Latina viven en ciudades que exceden',
				'las Guías de Calidad del Aire (OMS, 2016), es por ello que los datos horarios de contaminantes',
				'del aire son fundamentales porque ofrecen información detallada sobre las concentraciones de',
				'contaminantes en una ubicación específica durante el día, lo que permite una evaluación más',
				'precisa de la calidad del aire y de la exposición de las personas a los contaminantes.')

streamlit.write('Los contaminantes que se consideran en los datos de horario de contaminantes son los siguientes:')

streamlit.write(' - Partículas de menos de 10 micrómetros de diámetro (PM10)')
streamlit.write(' - Partículas de menos de 2.5 micrómetros de diámetro (PM2.5)')
streamlit.write(' - Ozono troposférico (O3)')
streamlit.write(' - Dióxido de nitrógeno (NO2)')
streamlit.write(' - Dióxido de azufre (SO2)')
streamlit.write(' - Monóxido de carbono (CO)')

streamlit.write('A continuación tendremos los datos de cada uno de las estaciones en las que se tomaron los datos')

streamlit.subheader('Seleccione la estación y año que desea revisar:')

Estaciones_opciones = df['ESTACION'].unique().tolist()

Estación = streamlit.multiselect('Seleccione la estación y año que desea revisar:',['ATE', 'SAN BORJA ', 
'CAMPO DE MARTE', 'SANTA ANITA', 'VILLA MARIA DEL TRIUNFO', 'HUACHIPA', 'SAN JUAN DE LURIGANCHO',
'SAN MARTIN DE PORRES', 'CARABAYLLO', 'PUENTE PIEDRA'])

Año_Inicial, Año_Final = streamlit.select_slider('Ahora, Seleccione la fecha que quiere revisar:', options = ['2010',
'2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], value = ('2010', '2020'))

streamlit.write('Usted selecciono como estacion(es):', [Estación], 'y seleccionó como el periodo de tiempo entre:',
Año_Inicial, 'y', Año_Final)

streamlit.subheader('Tabla de datos')

Año_Inicial_1 = str(Año_Inicial)

Año_Final_1 = str(Año_Final)

Año_I_df = int(Año_Inicial_1)

Año_F_df =int(Año_Final_1)

Estaciones = str(Estación)

df_1 = df[  df["ANO"] >= Año_I_df]

df_2 = df_1[  df_1["ANO"] <= Año_F_df]

df_USO = df_2[  df_2["ESTACION"].isin(Estación)]

streamlit.write(df_USO)

streamlit.subheader('Graficos')

streamlit.write('Grafico de concenatración de PM 10')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'PM 10')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'PM 10')

streamlit.write('Grafico de concenatración de PM 2.5')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'PM 2.5')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'PM 2.5')

streamlit.write('Grafico de concenatración de SO2')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'SO2')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'SO2')

streamlit.write('Grafico de concenatración de NO2')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'NO2')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'NO2')

streamlit.write('Grafico de concenatración de O3')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'O3')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'O3')

streamlit.write('Grafico de concenatración de CO')

if len(df_USO) > 50000:
	streamlit.bar_chart(df_USO.sample(frac = 0.2), x = 'ESTACION', y = 'CO')
else:
	streamlit.bar_chart(df_USO, x = 'ESTACION', y = 'CO')