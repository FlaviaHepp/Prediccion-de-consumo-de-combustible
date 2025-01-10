# Prediccion-de-consumo-de-combustible
Análisis, visualización y predicción de consumo de combustible.

Se hizo un análisis detallado y un modelo predictivo para estimar el consumo de combustible utilizando Python. 

**Desarrollo:**
Importación de bibliotecas y carga de datos.
*Herramientas utilizadas:* Python, pandas, numpy, seaborn, matplotlib, scikit-learn, StandardScaler, LabelEncoder y RandomForestRegressor.
**Análisis exploratorio de datos (EDA):**
Se imprimieron las primeras filas y estadísticas descriptivas del conjunto de datos.
Se seleccionaron columnas relevantes: ENGINE SIZE, CCYLINDERS,FUEL CONSUMPTION, y `COECOEMISSIONS.
**Entrenamiento y prueba de modelos:**
*División de datos:* Los datos se dividieron en conjuntos de entrenamiento (80%)
*Regresión lineal:* Se aplicó un modelo de regresión lineal para relacionar variables como ENGINE SIZE y CYLINDERS con las COECOEMISSIONS. Se calcularon coeficientes, interceptos y se graficaron líneas de ajuste.
*Regresión de bosque aleatorio:* Se entrenó un modelo de bosque aleatorio para predecir el consumo de combustible.
Se evaluaron las métricas del modelo con 𝑅2 y otros indicadores.
**Transformación de datos:**
Se aplicó LabelEncoder para convertir columnas categóricas como MAKE, MODEL, y TRANSMISSION a valores numéricos.
Se utilizó StandardScaler para escalar los datos.
**Visualizaciones avanzadas:**
Se generaron gráficos como mapas de calor, diagramas de caja, gráficos de barras y gráficos de dispersión para analizar relaciones entre variables como:
- Consumo de combustible vs. clase del vehículo.
- Consumo medio de combustible por marca.
- Relación entre tipo de transmisión y tamaño del motor.

***Resultados clave:***
Existe una relación positiva clara entre el tamaño del motor y las emisiones de CO2: a mayor tamaño del motor, mayores emisiones.
Los vehículos con más cilindros tienden a consumir más combustible y emitir más CO2.
En los Modelos predictivos la Regresión lineal mostró coeficientes significativos que indican cómo las variables predictoras influyen en las emisiones de CO2. En tanto que, en el modelo Random Forest Regressor la puntuación de la prueba fue razonablemente alta, mostrando que el modelo generaliza bien.
La mayoría de los vehículos tienen un consumo promedio de combustible en un rango definido, pero se observaron valores atípicos que podrían corresponder a vehículos de alto rendimiento o ineficientes.
Las clases de vehículos más grandes (como SUV y camiones) tienen mayores consumos de combustible y emisiones de CO2.
El tipo de transmisión influye en el tamaño del motor y, en consecuencia, en el consumo y las emisiones.
*Mapas de calor mostraron correlaciones significativas entre variables numéricas, destacando:*
- Alta correlación entre FUEL CONSUMPTION y COEMISSIONS.
- Los diagramas de caja y gráficos de dispersión evidenciaron:
- Vehículos con motores más grandes tienen mayores consumos y emisiones.
- Variabilidad en el consumo de combustible dentro de clases de vehículos similares.
