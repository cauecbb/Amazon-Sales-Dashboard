import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/ecommerce.csv')

st.title("Dashboard - E-commerce")

# Counts orders per status
status_count = df['order_status'].value_counts().reset_index()
status_count.columns = ['Status', 'Quantity']

# Shows the tabel with Status Count
st.write("Count of Orders per Status")
st.write(status_count)

# Creates a grafic for visualization the order per status
fig = px.bar(status_count, x='Status', y='Quantity', title='Orders per Status')
st.plotly_chart(fig)