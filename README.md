# 📊 Análisis de Ventas Ficticias con Pandas + Seaborn

Este proyecto muestra un ejemplo práctico de cómo analizar y visualizar datos con **Python**, utilizando las librerías **Pandas**, **Seaborn** y **Matplotlib**.  
El dataset es **ficticio** y representa ventas de distintos vendedores y productos.

---

## 🚀 Tecnologías utilizadas
- [Python 3.x](https://www.python.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Seaborn](https://seaborn.pydata.org/)  
- [Matplotlib](https://matplotlib.org/)  

---

## 📂 Archivos incluidos
- `ventas_ficticias.xlsx` → Dataset ficticio de ventas.  
- `analisis_ventas.py` → Script completo con análisis y visualización.  
- `ventas.png` → Gráfico final exportado.  
- `requirements.txt` → Dependencias del proyecto.  

---

## ⚡ Ejemplo rápido (LinkedIn version)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar Excel ficticio
df = pd.read_excel("ventas_ficticias.xlsx")

# Resumen: ventas totales por vendedor
ventas = df.groupby("Vendedor")["Ventas"].sum().reset_index()

# Visualización
sns.barplot(data=ventas, x="Vendedor", y="Ventas", palette="crest")
plt.title("Ventas Totales por Vendedor")
plt.show()
