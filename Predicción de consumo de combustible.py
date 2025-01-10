

#Importar bibliotecas y leer conjuntos de datos
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
plt.style.use('dark_background')
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, r2_score
from sklearn.ensemble import RandomForestRegressor
import warnings


fc = pd.read_csv("FuelConsumption (1).csv")
print(fc)

#Análisis exploratorio de datos
print(fc.head(10))  

print(fc.describe())  

print(fc.columns)   

cfc = fc[['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION','COEMISSIONS ']]
print(cfc.head())

#Visualización de datos
visualizacion = cfc[['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION','COEMISSIONS ']]
print(visualizacion.hist())
plt.show()

#Visualización de los datos en histograma
for i in cfc[['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION','COEMISSIONS ']]:
    plt.scatter(cfc[i],cfc['COEMISSIONS '],color = 'green')
    plt.xlabel(i)
    plt.ylabel("Emisión\n")
    plt.show()

#Entrenamiento de modelos
mascara = np.random.rand(len(cfc))<0.80
train = cfc[mascara]
test = cfc[~mascara]

#Aplicamos regresión lineal en datos de entrenamiento y calculamos coeficiente e intersección
coeficiente=[]
interceptor=[]
modelo_regresión = {}
for i in ['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION']:
    reg = linear_model.LinearRegression()
    train_x = np.asanyarray(train[[i]])
    train_y = np.asanyarray(train[['COEMISSIONS ']])
    reg.fit(train_x, train_y)
    modelo_regresión[i] = reg
    print("Relación entre {} y {}".format(i, "'coemisión'"))
    print("Coeficiente :", reg.coef_)
    print("interceptor :", reg.intercept_)
    coeficiente.append(reg.coef_)
    interceptor.append(reg.intercept_)
    print('\n')
    
#Utilizamos el parámetro de regresión para modelar una ecuación lineal
j=0
for i in train[['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION']]:
    plt.scatter(train[i], train['COEMISSIONS '],  color='blue')
    x=train[i].values
    print(x.shape)
    y=coeficiente[j][0]*x + interceptor[j]
    print(y.shape)
    l=len(y)
    y=np.reshape(y,(l,))
    plt.plot(x, y, '-r')
    plt.xlabel(i)
    plt.ylabel("Emisión\n")
    plt.show()
    j=j+1
    
#Rendimiento del modelo
#Calculamos Error absoluto medio, suma residual de cuadrados, puntuación R2
for i in train[['ENGINE SIZE','CYLINDERS','FUEL CONSUMPTION']]:
    test_x = np.asanyarray(test[[i]])
    test_y = np.asanyarray(test[['COEMISSIONS ']])
    test_y_ = modelo_regresión[i].predict(test_x)
    print("Error de ajuste entre {} y {}".format(i,"'CO2EMISSIONS'"))
    print("Error absoluto medio: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
    print("Suma residual de cuadrados (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
    print("Puntuación R2: %.2f" % r2_score(test_y_ , test_y) )
    print('\n')
    

fc.dropna(inplace=True)
fc

Lbl=LabelEncoder()
fc.MAKE=Lbl.fit_transform(fc.MAKE)
fc.MODEL=Lbl.fit_transform(fc.MODEL)

fc.TRANSMISSION=Lbl.fit_transform(fc.TRANSMISSION)
fc.FUEL=Lbl.fit_transform(fc.FUEL)
fc["VEHICLE CLASS"]=Lbl.fit_transform(fc["VEHICLE CLASS"])
fc

sns.histplot(data=fc)
plt.show()

sns.pairplot(fc[["Year","MAKE","MODEL","VEHICLE CLASS","ENGINE SIZE","CYLINDERS","TRANSMISSION","FUEL","FUEL CONSUMPTION"]], hue='FUEL CONSUMPTION', palette='husl')
plt.show()

fc.hist(figsize=(20,10),bins = 50)

plt.figure(figsize=(20,10))
sns.heatmap(fc.corr(),annot=True,cmap="cool")
plt.show()

sns.jointplot(data=fc, x="FUEL CONSUMPTION", y="Year", height=5, ratio=2, marginal_ticks=True)
plt.show()

sns.stripplot(data=fc, x="FUEL CONSUMPTION", y="MODEL")
plt.show()

X=fc.drop(["FUEL CONSUMPTION"],axis=1)
print(X)

y=fc["FUEL CONSUMPTION"]
y=pd.DataFrame(y)
print(y)

#Escalador estándar para datos
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
X= scaler.fit_transform(X)
print(X)

scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
y= scaler.fit_transform(y)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=33, shuffle =True)

reg_moduel=RandomForestRegressor(n_estimators=150,random_state=33)
reg_moduel.fit(X_train,y_train)

#Calcular detalles
print('La puntuación del tren de regresor forestal aleatorio es: ' ,  reg_moduel.score(X_train, y_train))
print('La puntuación de la prueba del regresor forestal aleatorio es: ' , reg_moduel.score(X_test, y_test))

#Seleccionar solo columnas numéricas
numeric_data = fc.select_dtypes(include=[np.number])

#Matriz de correlación
corr = numeric_data.corr()

#Trazar el mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='cool', fmt=".2f", linewidths=0.5)
plt.show()

#Distribución del consumo de combustible
plt.figure(figsize=(10, 6))
sns.histplot(fc['FUEL CONSUMPTION'], bins=20, kde=True, color='skyblue', edgecolor = "white")
plt.title('Distribución del consumo de combustible\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('El consumo de combustible\n')
plt.ylabel('Frecuencia\n')
plt.show()

#Diagrama de caja del consumo de combustible por clase de vehículo
plt.figure(figsize=(12, 8))
sns.boxplot(x='VEHICLE CLASS', y='FUEL CONSUMPTION', data=fc, palette='Set2')
plt.title('Consumo de combustible por clase de vehículo\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Clase de vehículo\n')
plt.ylabel('El consumo de combustible\n')
plt.xticks(rotation=45)
plt.show()

#Contar gráfico de clase de vehículo
plt.figure(figsize=(10, 6))
sns.countplot(y='VEHICLE CLASS', data=fc, order=fc['VEHICLE CLASS'].value_counts().index, palette='pastel')
plt.title('Conteo de vehículos por clase de vehículo\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Conteo\n')
plt.ylabel('Clase de vehículo\n')
plt.show()

#Gráfico de barras del consumo medio de combustible por marca
plt.figure(figsize=(12, 8))
Consumo_medio_de_combustible_por_marca = fc.groupby('MAKE')['FUEL CONSUMPTION'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=Consumo_medio_de_combustible_por_marca.values, y=Consumo_medio_de_combustible_por_marca.index, palette='muted')
plt.title('Consumo medio de combustible por marca (Top 10)\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Consumo medio de combustible\n')
plt.ylabel('\n')
plt.show()

#Diagrama de caja del tamaño del motor por tipo de transmisión
plt.figure(figsize=(12, 6))
sns.boxplot(x='TRANSMISSION', y='ENGINE SIZE', data=fc, palette='spring')
plt.title('Tamaño del motor por tipo de transmisión\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Transmisión\n')
plt.ylabel('Tamaño de la maquina\n')
plt.show()

#Gráfico de dispersión del consumo de combustible frente al tamaño del motor coloreado por tipo de transmisión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ENGINE SIZE', y='FUEL CONSUMPTION', hue='TRANSMISSION', data=fc, palette='Set2')
plt.title('Consumo de combustible versus tamaño del motor por tipo de transmisión\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Tamaño de la maquina\n')
plt.ylabel('El consumo de combustible\n')
plt.show()

#Distribución del tamaño del motor por clase de vehículo
plt.figure(figsize=(12, 8))
sns.boxplot(x='VEHICLE CLASS', y='ENGINE SIZE', data=fc, palette='Set2')
plt.title('Distribución del tamaño del motor por clase de vehículo\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Clase de vehículo\n')
plt.ylabel('Tamaño de la maquina\n')
plt.xticks(rotation=45)
plt.show()

#Gráfico de barras del consumo medio de combustible por tipo de transmisión
consumo_medio_de_combustible_por_transmisión = fc.groupby('TRANSMISSION')['FUEL CONSUMPTION'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=consumo_medio_de_combustible_por_transmisión.index, y=consumo_medio_de_combustible_por_transmisión.values, palette='cool')
plt.title('Consumo medio de combustible por tipo de transmisión\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Tipo de transmisión\n')
plt.ylabel('Consumo medio de combustible\n')
plt.xticks(rotation=45)
plt.show()

#Diagrama de caja del tamaño del motor por tipo de combustible
plt.figure(figsize=(10, 6))
sns.boxplot(x='FUEL', y='ENGINE SIZE', data=fc, palette='Set3')
plt.title('Tamaño del motor por tipo de combustible\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Tipo de combustible\n')
plt.ylabel('Tamaño de la maquina\n')
plt.show()

#Gráfico de enjambre de consumo de combustible por recuento de cilindros
plt.figure(figsize=(10, 6))
sns.swarmplot(x='CYLINDERS', y='FUEL CONSUMPTION', data=fc, palette='muted')
plt.title('Consumo de combustible por cantidad de cilindros\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Recuento de cilindros\n')
plt.ylabel('El consumo de combustible\n')
plt.show()