import pandas as pd
import glob

print("=================================== DATAFRAME MEDELLIN =====================================")

df_medellin = pd.read_csv("TrabajosJxxx/Trabajos/Victor/sucursal_medellin.csv")
print(df_medellin.head(3))

print("\n")
print("=================================== DATAFRAME BOGOTA =======================================")
print("\n")

df_bogota = pd.read_excel("TrabajosJxxx/Trabajos/Victor/sucursal_bogota.xlsx")
print(df_bogota.head(3))


print("\n")
print("================================== DATAFRAME BARRANQUILLA ===================================")
print("\n")

df_barranquilla = pd.read_excel("TrabajosJxxx/Trabajos/Victor/sucursal_barranquilla.xlsx")
print(df_barranquilla.head(3))


print("\n")
print("====================================== DATAFRAME CALI ========================================")
print("\n")

df_cali = pd.read_csv("TrabajosJxxx/Trabajos/Victor/sucursal_cali.csv")
print(df_cali.head(3))

print("\n")
print("====================================== COLUMNAS BOGOTA =======================================")
print("\n")

print(df_bogota.columns)

print("\n")
print("====================================== COLUMNAS MEDELLIN =======================================")
print("\n")


print(df_medellin.columns)

print("\n")
print("==================================== COLUMNAS BARRANQUILLA =====================================")
print("\n")

print(df_barranquilla.columns)

print("\n")
print("======================================== COLUMNAS CALI =========================================")

print(df_cali.columns)

print("\n")
print("======================================== ARCHIVOS CSV ===========================================")
print("\n")

archivos_csv = glob.glob("*.csv")

print(archivos_csv)

print("\n")
print("======================================== ARCHIVOS XLSX ==========================================")

archivos_xlsx = glob.glob("*.xlsx")

print(archivos_xlsx)

lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)

    print(f"Leidos: {archivo} - {len(df)} filas")

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_informes.append(df)
    
    print(f"Leidos: {archivo} - {len(df)} filas")
    
    
for i, df in enumerate(lista_informes):
    if "Fecha_Venta" in df.columns:
        lista_informes[i] = df.rename(columns={
            "Fecha_Venta": "fecha", "Producto": "producto", 
            "Cant": "cantidad", "Valor_Unitario": "precio_unitario", 
            "Categoria": "categoria", "Vendedor": "vendedor", "Pago": "metodo_pago"
        })
                                    
df_consolidado = pd.concat(lista_informes, ignore_index=True):
print(df_consolidado):