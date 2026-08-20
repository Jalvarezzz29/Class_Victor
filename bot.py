import pandas as pd

df_consolidado = pd.read_excel("data/ventas.xlsx")

total_por_categoria = df_consolidado.groupby('categoria')['precio_unitario'].sum()
print("Total de ventas por categoria:")
print(total_por_categoria)

precio_promedio_categoria = df_consolidado.groupby('categoria')['precio_unitario'].mean()
print("Precio promedio por categoria:")
print(precio_promedio_categoria)

transacciones_por_vendedor = df_consolidado.groupby('vendedor')['precio_unitario'].count()
print("Cantidad de transacciones por vendedor:")
print(transacciones_por_vendedor)

resumen_extra = pd.DataFrame({
    'precio_promedio': precio_promedio_categoria
})
resumen_extra.to_excel("analisis_extra.xlsx")
