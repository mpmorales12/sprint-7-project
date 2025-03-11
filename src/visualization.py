import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_fuel_type_count(df: pd.DataFrame):
    '''
    Genera un gráfico de barras que muestra la cantidad de vehículos por tipo
    de combustible

    :param df: DataFrame con los datos de los vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    '''
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(x=df['fuel'],palette='colorblind',ax=ax)
    ax.set_xlabel('Fuel Type')
    ax.set_ylabel('Number of Vehicles')
    ax.set_title("Number of Vehicles per Fuel Type")
    ax.grid()
    return fig

def plot_price_odometer_distribution(df: pd.DataFrame):
    '''
    Genera un gráfico de dispersión que muestra la relación entre kilometraje y precio

    :param df: DataFrame con los datos de los vehículos.
    :return: Figura de Plotly con el gráfico generado.
    '''
    fig = px.scatter(df,
                     x= df['odometer'],
                     y= df['price'],
                     color= df['model'])
    
    fig.update_layout(title="Price vs Odometer",
                      xaxis_title="Odometer",
                      yaxis_title="Price")
    return fig

def plot_brand_type_count_price(df: pd.DataFrame):
    '''
    Genera un gráfico de barras que muestra la cantidad de vehículos por marca
    filtrado según el precio

    :param df: DataFrame con los datos de los vehículos.
    :return: Figura de Plotly con el gráfico generado.
    '''
    fig = px.histogram(df,
                        x= df['price'],
                        color= df['model'])
    
    fig.update_layout(title="Number of Vehicles per model",
                      xaxis_title="Price",
                      yaxis_title="Number of Vehicles")
    return fig

def plot_year_distribution(df: pd.DataFrame):
    '''
    Genera un histograma de frecuencia que muestra la distribución de los años
    de modelos de los vehículos.

    :param df: DataFrame con los datos de los vehículos.
    :return: Figura de Plotly con el gráfico generado.
    '''
    fig = px.histogram(df,
                        x= df['model_year'])
    
    fig.update_layout(title="Model Year Distribution",
                      xaxis_title="Model Year",
                      yaxis_title="Frequency")

    return fig

def plot_price_distribution(df: pd.DataFrame):
    '''
    Genera un histograma de frecuencia que muestra la distribución de precios
    los vehículos.

    :param df: DataFrame con los datos de los vehículos.
    :return: Figura de Plotly con el gráfico generado.
    '''
    fig = px.histogram(df,
                        x= df['price'])
    
    fig.update_layout(title="Price Distribution",
                      xaxis_title="Price",
                      yaxis_title="Frequency")

    return fig
