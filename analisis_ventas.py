import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Cargar Excel ficticio
df = pd.read_excel("ventas_ficticias.xlsx")

# Resumen: Ventas totales por vendedor (orden natural)
ventas_por_vendedor = df.groupby("Vendedor")["Ventas"].sum().reset_index()

# Configuración de estilo
sns.set_theme(style="whitegrid")
plt.figure(figsize=(9, 5))

# Gráfico con paleta
ax = sns.barplot(
    data=ventas_por_vendedor,
    x="Vendedor",
    y="Ventas",
    palette="crest"
)

# Título
plt.title("Ventas Totales por Vendedor\n(Datos ficticios)", fontsize=18, fontweight="bold")

# Ejes
ax.set(xlabel=None, ylabel=None)
plt.ylabel("Ventas Totales (CLP)", fontsize=12)

# Formato en miles (ejemplo: $200K en vez de $200,000)
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${int(x/1000)}K"))

# Línea de promedio
promedio = ventas_por_vendedor["Ventas"].mean()
plt.axhline(promedio, color="red", linestyle="--", linewidth=1.2, label=f"Promedio: ${promedio:,.0f}")
plt.legend()

# Etiquetas sobre las barras con fondo blanco
for index, row in ventas_por_vendedor.iterrows():
    ax.text(
        index,
        row["Ventas"] + (row["Ventas"] * 0.02),
        f"${row['Ventas']:,.0f}",
        ha='center', va='bottom',
        fontsize=10, color="black",
        bbox=dict(facecolor="white", alpha=0.7, edgecolor="none")
    )

# Limpiar bordes
sns.despine()

# Guardar imagen
plt.tight_layout()
plt.savefig("ventas.png", dpi=300)
plt.show()
