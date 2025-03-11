# sprint-7-project
🚗Practical Project: Descriptive Analysis of a Vehicle Dataset

# Descripción del Proyecto
Este proyecto forma parte del Sprint 7 - Herramientas de Desarrollo de Software y tiene como objetivo construir y desplegar una aplicación web para el análisis de un conjunto de datos de vehículos. La aplicación permite realizar un análisis exploratorio interactivo mediante gráficos generados con Plotly Express, se ha desarrollado con la librería Streamlit y está alojada en Render.

***Render**: 
**Repositorio GitHub**: https://github.com/mpmorales12/sprint-7-project.git

# Funcionalidades
- Carga y visualización de datos de vehículos
- Filtros interactivos por marca, precio y tipo de transmisión
- Gráfico de histograma para distribución de precio 
- Gráfico de dispersión de relación entre precio y kilometraje
- Casillas de verificación para seleccionar gráficos

# Estructura del proyecto
sprint-7-project
|── README.md                   # Documentación del proyecto
|── app.py                      # Código principal de la aplicación Streamlit
|── vehicles_us.csv             # Dataset utilizado en el análisis
|── requirements.txt            # Librerías del proyecto
|── src                         # Módulos propios para hacer más limpio el código principal
|   |── data_processing.py      # Módulo propio para hacer el preprocesamiento de datos
|   |── visualization.py        # Módulo propio para la creación de visualizaciones
|── notebooks                   # Análisis exploratiorio con Jupyter
|   |── Data_wrangling.ipynb    # Análisis exploratiorio inicial
|── EDA.ipynb                   # Análisis exploratorio del proyecto         

