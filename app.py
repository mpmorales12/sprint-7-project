#Import libraries
import pandas as pd
import streamlit as st
from src.data_processing import clean_data
import src.visualization as vis

#Load data
df = pd.read_csv('vehicles_us.csv')

#Clean data
df = clean_data(df)

#Title and app description
st.title('Descriptive Analysis of Vehicles for Sale')
st.write(
    'This application allows you to explore a dataset of vehicles, '
    'providing statistics and interactive visualisations.'
)

#Show statistic summary
st.write('## Summary of Data')

#Generate and show graphs
fig1 = vis.plot_price_distribution(df)
st.plotly_chart(fig1)

fig2 = vis.plot_price_odometer_distribution(df)
st.plotly_chart(fig2)

st.write('## Data by Brand')

#Input to create a Brand analysis
check = st.checkbox('Analyse Data by Brand')

if check:
    #Input to select a Brand vehicle
    selected_brand = st.selectbox('Select a vehicle brand to filter the data:',
                                df['brand'].unique())
    df_filtered = df[df['brand'] == selected_brand]

    # --- Create a slider to selecet the price range ---
    min_price, max_price = st.slider(
        "Select a price range:",
        min_value=int(df_filtered['price'].min()),
        max_value=int(df_filtered['price'].max()),
        value=(int(df_filtered['price'].min()), int(df_filtered['price'].max())) 
    )

    df_filtered = df_filtered[(df_filtered['price'] >= min_price) & (df_filtered['price'] <= max_price)]

    # --- Creat a checkbox to select the type of transmission ---
    select_transm = st.radio('Select Type of Transmission', (list(df_filtered['transmission'].unique()) + ['Any']))

    if select_transm == 'Any':
        df_filtered = df_filtered
    else:
        df_filtered = df_filtered[df_filtered['transmission'] == select_transm]

    fig3 = vis.plot_brand_type_count_price(df_filtered)
    st.plotly_chart(fig3)

    fig4 = vis.plot_price_odometer_distribution(df_filtered)
    st.plotly_chart(fig4)
