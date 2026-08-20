# Manage Your Day (MYD)

Manage Your Day (MYD) es una aplicación para el control de tareas y finanzas
personales. Permite al usuario registrar y organizar sus tareas diarias, así
como llevar un seguimiento de sus ingresos y gastos, con el objetivo de
ayudarlo a administrar mejor su tiempo y su dinero.

Este repositorio documenta el desarrollo del proyecto usando **Git**, con un
flujo de trabajo basado en commits convencionales y ramas.

## Instalación

1. Clona este repositorio:

git clone <url-del-repositorio>
cd manage-your-day

2. Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

3. Instala las dependencias:

pip install pandas openpyxl


## Cómo ejecutar el proyecto

1. Asegúrate de tener los archivos de datos necesarios en la carpeta `data/`.
2. Ejecuta el script principal:

python bot.py

3. El script imprime en consola los resultados del análisis y genera
   `analisis_extra.xlsx` con el resumen correspondiente.

## Resultados y hallazgos

El análisis de los datos permitió identificar patrones de comportamiento en
las categorías analizadas, resumidos en la siguiente tabla:

| Categoría   | Total ventas |
|-------------|--------------|
| Electrónica | $3,361,610   |
| Ropa        | $2,687,020   |

Estos resultados sirven como base para el análisis complementario desarrollado
más adelante en la rama `mejoras`.

## Conclusión final

El desarrollo de este ejercicio permitió aplicar un flujo de trabajo ordenado
con Git, usando commits convencionales para documentar cada etapa del
proyecto y ramas para incorporar nuevas funcionalidades de forma controlada,
sin afectar la rama principal hasta que el trabajo estuvo listo para
fusionarse.
