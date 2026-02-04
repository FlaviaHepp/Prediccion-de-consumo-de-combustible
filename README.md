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

# Predicción de consumo de combustible y emisiones de CO₂

Este proyecto analiza y modela el **consumo de combustible de vehículos** y su relación con variables técnicas como el tamaño del motor, número de cilindros y tipo de transmisión, utilizando técnicas de **análisis exploratorio de datos (EDA)** y **modelos de regresión**.

El objetivo es **predecir el consumo de combustible** y estudiar su impacto en las **emisiones de CO₂**, aportando información relevante para eficiencia energética y sostenibilidad.

---

## 🚗 Contexto del problema

El consumo de combustible y las emisiones vehiculares son factores clave en:
- costos operativos
- regulaciones ambientales
- diseño de vehículos más eficientes

A partir de datos técnicos de vehículos, este proyecto busca identificar **qué características influyen más en el consumo** y construir modelos predictivos.

---

## 🎯 Objetivo de Machine Learning

- **Tipo de problema:** Regresión
- **Variable objetivo:** `FUEL CONSUMPTION`
- **Métrica de evaluación:** R², MAE y MSE
- **Enfoque:** comparación entre modelos lineales simples y modelos no lineales

---

## 📊 Dataset

El conjunto de datos incluye información técnica de vehículos:

### Variables principales
- `ENGINE SIZE`
- `CYLINDERS`
- `FUEL CONSUMPTION`
- `COEMISSIONS`
- `MAKE`, `MODEL`
- `VEHICLE CLASS`
- `TRANSMISSION`
- `FUEL`
- `Year`

Variables categóricas fueron codificadas mediante **Label Encoding**.

---

## 🧪 Metodología

### 1. Análisis exploratorio de datos (EDA)
- Estadísticas descriptivas
- Distribuciones e histogramas
- Análisis de correlación
- Visualizaciones multivariadas (pairplot, heatmap)
- Relación entre consumo, emisiones y características del vehículo

### 2. Modelado

#### Regresión lineal simple
Se entrenaron modelos independientes para evaluar la relación entre:
- tamaño del motor → emisiones
- número de cilindros → emisiones
- consumo de combustible → emisiones

#### Regresión no lineal
- **Random Forest Regressor**
- Entrenamiento y evaluación en conjuntos de train/test
- Comparación de desempeño con modelos lineales

---

## 📈 Resultados principales

- Existe una **fuerte correlación positiva** entre:
  - tamaño del motor y consumo
  - consumo de combustible y emisiones de CO₂
- Los modelos no lineales capturan mejor relaciones complejas
- El Random Forest mostró mayor capacidad predictiva que la regresión lineal simple

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **pandas, numpy**
- **matplotlib, seaborn**
- **scikit-learn**
- **RandomForestRegressor**

---

## 📂 Estructura del repositorio

├── FuelConsumption.csv
├── Predicción de consumo de combustible.py
├── README.md


---

## 🚀 Próximos pasos

- Ajuste de hiperparámetros del Random Forest
- Inclusión de técnicas de regularización (Ridge / Lasso)
- Feature importance y explainability
- Incorporación de variables externas (peso del vehículo, potencia)
- Construcción de un pipeline de ML reproducible

---

## 👤 Autor

**Flavia Hepp**  
Data Analyst / Data Scientist en formación  
