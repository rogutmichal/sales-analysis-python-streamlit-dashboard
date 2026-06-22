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

st.sidebar.header("Filters")
cities = sorted(df["City"].unique())


selected_cities = st.sidebar.multiselect(
    "Select Cities",
    cities,
    default=cities
)

products = sorted(df["Product"].unique())

selected_products = st.sidebar.multiselect(
    "Select Products",
    products,
    default=products
)


managers = sorted(df["Manager"].unique())

selected_managers = st.sidebar.multiselect(
    "Select Managers",
    managers,
    default=managers
)


filtered_df = df[
    df["City"].isin(selected_cities) & df["Product"].isin(selected_products) & df["Manager"].isin(selected_managers)
]

st.subheader(" Key Performance Indicators")


total_revenue = filtered_df["Revenue"].sum()
orders = len(filtered_df)
avg_order_value = filtered_df["Revenue"].mean()
unique_products = filtered_df["Product"].nunique()

col1, col2, col3, col4 = st.columns(4)


col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Orders", orders)
col3.metric("Avg Order Value", f"{avg_order_value:,.2f}")
col4.metric("Products", unique_products)




st.subheader(" Revenue by City")

city_sales = group_revenue(filtered_df, "City")

fig = px.bar(
    city_sales,
    x="City",
    y="Revenue",
    text="Revenue",
    title="Revenue Distribution by City"
    
    
    
)

fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')

fig.update_layout(
    title_x=0.5,
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    barcornerradius=15,
    
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Revenue by Product")

product_sales = group_revenue(filtered_df, "Product")
product_sales = (
    group_revenue(filtered_df, "Product")
    .head(5)
    .iloc[::-1]
)
fig = px.bar(
    product_sales,
    x="Revenue",
    y="Product",
    orientation="h",
    text="Revenue",
    title="Top Products by Revenue"
)

fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')

fig.update_layout(
    title_x=0.5,
    yaxis_title="",
    xaxis_title="Revenue",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

fig.update_yaxes(categoryorder="total ascending")

st.subheader("Revenue Trend Over Time")

daily_revenue = (
    filtered_df.groupby("Date")["Revenue"]
    .sum()
    .reset_index()
)


fig = px.line(
    daily_revenue,
    x="Date",
    y="Revenue",
    title="Daily Revenue Trend",
    markers=True
)


fig.update_layout(
    title_x=0.5,
    height=500
)


st.plotly_chart(fig, use_container_width=True)

best_day = daily_revenue.loc[
    daily_revenue["Revenue"].idxmax()
]

st.info(
    f"Best sales day: {best_day['Date'].date()} "
    f"with revenue {best_day['Revenue']:,.0f}"
)

st.subheader("Manager Performance")

manager_sales = group_revenue(filtered_df, "Manager")

top_manager = manager_sales.iloc[0]

st.success(
    f"🏆 Top Manager: {top_manager['Manager']} | "
    f"Revenue: {top_manager['Revenue']:,.0f}"
)

fig = px.bar(
    manager_sales,
    x="Manager",
    y="Revenue",
    text="Revenue",
    title="Revenue by Manager"
)

fig.update_traces(
    texttemplate='%{text:,.0f}',
    textposition='outside'
)

fig.update_layout(
    title_x=0.5,
    xaxis_title="Manager",
    yaxis_title="Revenue",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("Revenue by Payment Method")

    payment_sales = group_revenue(
        filtered_df,
        "Payment Method"
    )


    fig = px.pie(
        payment_sales,
        names="Payment Method",
        values="Revenue",
        title="Payments Method",
        hole=0.4,
    )

    fig.update_layout(
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    with col2:
        st.subheader("Revenue by Purchase Type")

        purchase_sales = group_revenue(
            filtered_df,
            "Purchase Type"
        )

        fig = px.pie(
            purchase_sales,
            names="Purchase Type",
            values="Revenue",
            hole=0.4,
            title="Purchase Types"
        )

        fig.update_layout(
            title_x=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )