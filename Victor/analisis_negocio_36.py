import pandas as pd
import glob
import matplotlib.pyplot as plt

# ============================== LECTURA INDIVIDUAL ==============================
print("=================================== DATAFRAME MEDELLIN =====================================")
df_medellin = pd.read_csv("TrabajosJxxx/Trabajos/Victor/sucursal_medellin.csv")
print(df_medellin.head(3))

print("\n=================================== DATAFRAME BOGOTA =======================================\n")
df_bogota = pd.read_excel("TrabajosJxxx/Trabajos/Victor/sucursal_bogota.xlsx")
print(df_bogota.head(3))

print("\n================================== DATAFRAME BARRANQUILLA ===================================\n")
df_barranquilla = pd.read_excel("TrabajosJxxx/Trabajos/Victor/sucursal_barranquilla.xlsx")
print(df_barranquilla.head(3))

print("\n====================================== DATAFRAME CALI ========================================\n")
df_cali = pd.read_csv("TrabajosJxxx/Trabajos/Victor/sucursal_cali.csv")
print(df_cali.head(3))

# ============================== COLUMNAS ==============================
print("\n====================================== COLUMNAS BOGOTA =======================================\n")
print(df_bogota.columns)

print("\n====================================== COLUMNAS MEDELLIN =======================================\n")
print(df_medellin.columns)

print("\n==================================== COLUMNAS BARRANQUILLA =====================================\n")
print(df_barranquilla.columns)

print("\n======================================== COLUMNAS CALI =========================================")
print(df_cali.columns)

# ============================== BUSCAR ARCHIVOS ==============================
print("\n======================================== ARCHIVOS CSV =====================================\n")
archivos_csv = glob.glob("TrabajosJxxx/Trabajos/Victor/*.csv")
print(archivos_csv)

print("\n======================================== ARCHIVOS XLSX ====================================\n")
archivos_xlsx = glob.glob("TrabajosJxxx/Trabajos/Victor/*.xlsx")
print(archivos_xlsx)

# ============================== LEER TODOS LOS ARCHIVOS ==============================
print("\n======================================== LEER ARCHIVOS ====================================\n")
lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)
    print(f"Leídos: {archivo} - {len(df)} filas")

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_informes.append(df)
    print(f"Leídos: {archivo} - {len(df)} filas")

# ============================== RENOMBRAR COLUMNAS ==============================
for i, df in enumerate(lista_informes):
    if "Fecha_Venta" in df.columns:
        lista_informes[i] = df.rename(columns={
            "Fecha_Venta": "fecha",
            "Producto": "producto",
            "Cant": "cantidad",
            "Valor_Unitario": "precio_unitario",
            "Categoria": "categoria",
            "Vendedor": "vendedor",
            "Pago": "metodo_pago"
        })

# ============================== CONSOLIDAR ==============================
print("\n======================================== CONSOLIDAR ====================================\n")
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(df_consolidado)

# ============================== LIMPIEZA DE DATOS ==============================
# 1. Eliminar filas duplicadas
filas_antes = len(df_consolidado)
df_consolidado = df_consolidado.drop_duplicates()
print(f"\nFilas antes: {filas_antes} - después: {len(df_consolidado)}")

# 2. Ver valores nulos
print(f"\nValores nulos ANTES de rellenar:\n{df_consolidado.isnull().sum()}")

# 3. Rellenar valores nulos
df_consolidado["producto"] = df_consolidado["producto"].fillna("Desconocido")
df_consolidado["categoria"] = df_consolidado["categoria"].fillna("Desconocido")
df_consolidado["vendedor"] = df_consolidado["vendedor"].fillna("Desconocido")
df_consolidado["metodo_pago"] = df_consolidado["metodo_pago"].fillna("Desconocido")

df_consolidado["cantidad"] = df_consolidado["cantidad"].fillna(0)
df_consolidado["precio_unitario"] = df_consolidado["precio_unitario"].fillna(0)

df_consolidado["fecha"] = df_consolidado["fecha"].fillna("2024-01-01")

# 4. Verificar que ya no hay nulos
print(f"\nValores nulos DESPUÉS de rellenar:\n{df_consolidado.isnull().sum()}")

# ============================== GUARDAR RESULTADO ==============================
df_consolidado.to_excel("consolidado_limpio.xlsx", index=False)
print("\nArchivo guardado correctamente: consolidado_limpio.xlsx")


# ============================= ANÁLISIS DE NEGOCIO =============================

# Creamos la columna de venta total (precio * cantidad)
df_consolidado["venta_total"] = df_consolidado["precio_unitario"] * df_consolidado["cantidad"]

# ============= PREGUNTA 1: ¿Cuánto vendió cada categoría en total? ==============

print("PREGUNTA 1: Ventas por Categoría")

ventas_categoria = df_consolidado.groupby("categoria")["venta_total"].sum().sort_values(ascending=False)
print(ventas_categoria)

plt.figure(figsize=(8, 5))
ventas_categoria.plot(kind="bar", title="Ventas por Categoría", color="steelblue")
plt.ticklabel_format(style="plain", axis="y")
plt.ylabel("Ventas totales ($)")
plt.xlabel("Categoría")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_categoria.png", dpi=150)
plt.show()

# ======= PREGUNTA 2: ¿Qué porcentaje de las ventas representa cada vendedor? ========
 
print("PREGUNTA 2: Porcentaje de Ventas por Vendedor")

ventas_vendedor = df_consolidado.groupby("vendedor")["venta_total"].sum().sort_values(ascending=False)
print(ventas_vendedor)

plt.figure(figsize=(8, 6))
ventas_vendedor.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    title="Porcentaje de Ventas por Vendedor"
)
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafico_vendedor.png", dpi=150)
plt.show()

# =============== PREGUNTA 3: ¿Cuál es el producto que más se vende? ===============

print("PREGUNTA 3: Producto más vendido")

producto_mas_vendido = df_consolidado["producto"].value_counts()
print(producto_mas_vendido)

print(f"\n→ El producto que MÁS se vende es: {producto_mas_vendido.idxmax()} con {producto_mas_vendido.max()} transacciones")


 
# ======= PREGUNTA 4: ¿Cómo se distribuyen las ventas según el método de pago? ========

print("PREGUNTA 4: Ventas por Método de Pago")

ventas_metodo = df_consolidado.groupby("metodo_pago")["venta_total"].sum().sort_values(ascending=False)
print(ventas_metodo)

plt.figure(figsize=(8, 5))
ventas_metodo.plot(kind="bar", title="Ventas por Método de Pago", color="teal")
plt.ticklabel_format(style="plain", axis="y")
plt.ylabel("Ventas totales ($)")
plt.xlabel("Método de Pago")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_metodo_pago.png", dpi=150)
plt.show()

# ===== RETO OPCIONAL - PREGUNTA 5: ¿Cuál es el día de la semana con más ventas? =======
 
print("PREGUNTA 5 (OPCIONAL): Día de la semana con más ventas")

# CORRECCIÓN: las fechas vienen como día/mes/año
df_consolidado["fecha"] = pd.to_datetime(df_consolidado["fecha"], dayfirst=True, errors="coerce")

df_consolidado["dia_semana"] = df_consolidado["fecha"].dt.day_name()

# Traducir días al español
mapa_dias = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
df_consolidado["dia_semana_es"] = df_consolidado["dia_semana"].map(mapa_dias)

orden_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas_dia = df_consolidado.groupby("dia_semana_es")["venta_total"].sum().reindex(orden_dias)
print(ventas_dia)

print(f"\n→ El día con MÁS ventas es: {ventas_dia.idxmax()} con ${ventas_dia.max():,.0f}")

plt.figure(figsize=(9, 5))
ventas_dia.plot(kind="bar", title="Ventas por Día de la Semana", color="coral")
plt.ticklabel_format(style="plain", axis="y")
plt.ylabel("Ventas totales ($)")
plt.xlabel("Día de la Semana")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_dia_semana.png", dpi=150)
plt.show()

print("ANÁLISIS COMPLETADO")

print("Archivos generados:")
print("  - consolidado_limpio.xlsx")
print("  - grafico_categoria.png")
print("  - grafico_vendedor.png")
print("  - grafico_metodo_pago.png")
print("  - grafico_dia_semana.png")