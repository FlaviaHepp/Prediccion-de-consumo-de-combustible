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
