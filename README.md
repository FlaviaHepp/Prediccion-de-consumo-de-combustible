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

**Resultados clave:**
Se midieron errores de predicción y precisión para evaluar la eficacia de los modelos.
Se proporcionaron representaciones gráficas detalladas de los patrones en los datos.
