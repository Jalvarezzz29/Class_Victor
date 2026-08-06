import pandas as pd
import glob

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
print("\n======================================== ARCHIVOS CSV ===========================================\n")
archivos_csv = glob.glob("TrabajosJxxx/Trabajos/Victor/*.csv")
print(archivos_csv)

print("\n======================================== ARCHIVOS XLSX ==========================================")
archivos_xlsx = glob.glob("TrabajosJxxx/Trabajos/Victor/*.xlsx")
print(archivos_xlsx)

# ============================== LEER TODOS LOS ARCHIVOS ==============================
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