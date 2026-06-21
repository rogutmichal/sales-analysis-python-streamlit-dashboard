import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.aggregation import group_revenue



@st.cache_data
def load_and_prepare_data():
    df = load_data("data/sales.csv")
    df = preprocess(df)
    return df

df = load_and_prepare_data()

st.subheader(" Key Performance Indicators")


total_revenue = df["Revenue"].sum()
orders = len(df)
avg_order_value = df["Revenue"].mean()
unique_products = df["Product"].nunique()

col1, col2, col3, col4 = st.columns(4)


col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Orders", orders)
col3.metric("Avg Order Value", f"{avg_order_value:,.2f}")
col4.metric("Products", unique_products)




st.subheader(" Revenue by City")

city_sales = group_revenue(df, "City")

fig = px.bar(
    city_sales,
    x="City",
    y="Revenue",
    text="Revenue",
    title="Revenue Distribution by City"
    
)

fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')

fig.update_layout(
    xaxis_title="City",
    yaxis_title="Revenue",
    title_x=0.5,
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

st.plotly_chart(fig, use_container_width=True)