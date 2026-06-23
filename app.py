import streamlit as st
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.aggregation import group_revenue


st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)


@st.cache_data
def load_and_prepare_data():
    df = load_data("data/sales.csv")
    df = preprocess(df)
    return df


df = load_and_prepare_data()


# SIDEBAR

st.sidebar.header("Filters")

cities = sorted(df["City"].unique())
products = sorted(df["Product"].unique())
managers = sorted(df["Manager"].unique())

selected_cities = st.sidebar.multiselect(
    "Select Cities",
    cities,
    default=cities
)

selected_products = st.sidebar.multiselect(
    "Select Products",
    products,
    default=products
)

selected_managers = st.sidebar.multiselect(
    "Select Managers",
    managers,
    default=managers
)

filtered_df = df[
    (df["City"].isin(selected_cities))
    &
    (df["Product"].isin(selected_products))
    &
    (df["Manager"].isin(selected_managers))
]


# HEADER


st.title("Sales Analysis Dashboard")





# KPI




total_revenue = filtered_df["Revenue"].sum()
orders = len(filtered_df)
avg_order_value = filtered_df["Revenue"].mean()
unique_products = filtered_df["Product"].nunique()

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.metric(
            "Revenue",
            f"{total_revenue:,.0f} €"
        )

with col2:
    with st.container(border=True):
        st.metric(
            "Orders",
            f"{orders:,}"
        )

with col3:
    with st.container(border=True):
        st.metric(
            "Avg Order",
            f"{avg_order_value:,.0f} €"
        )

with col4:
    with st.container(border=True):
        st.metric(
            "Products",
            unique_products
        )

# ROW 1



col1, col2 = st.columns(2)

with col1:

    st.subheader("Revenue by City")

    city_sales = group_revenue(
        filtered_df,
        "City"
    )

    fig = px.bar(
        city_sales,
        x="City",
        y="Revenue",
        text="Revenue"
    )

    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Top Products")

    product_sales = (
        group_revenue(
            filtered_df,
            "Product"
        )
        .head(5)
        .iloc[::-1]
    )

    fig = px.bar(
        product_sales,
        x="Revenue",
        y="Product",
        orientation="h",
        text="Revenue"
    )

    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        )
    )

    fig.update_yaxes(
        categoryorder="total ascending"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ROW 2


col1, col2 = st.columns(2)

with col1:

    st.subheader("Revenue Trend")

    daily_revenue = (
        filtered_df
        .groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily_revenue,
        x="Date",
        y="Revenue",
        markers=True
    )

    fig.update_layout(
        height=380,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Manager Performance")

    manager_sales = group_revenue(
        filtered_df,
        "Manager"
    )

    top_manager = manager_sales.iloc[0]

    kpi1, kpi2 = st.columns(2)

    kpi1.metric(
        "Top Manager",
        top_manager["Manager"]
    )

    kpi2.metric(
        "Revenue",
        f"{top_manager['Revenue']:,.0f}"
    )

    fig = px.bar(
        manager_sales,
        x="Manager",
        y="Revenue",
        text="Revenue"
    )

    fig.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    fig.update_layout(
        height=300,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ROW 3


col1, col2 = st.columns(2)

with col1:

    st.subheader("Payment Method")

    payment_sales = group_revenue(
        filtered_df,
        "Payment Method"
    )

    fig = px.pie(
        payment_sales,
        names="Payment Method",
        values="Revenue",
        hole=0.4
    )

    fig.update_layout(
        height=380
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Purchase Type")

    purchase_sales = group_revenue(
        filtered_df,
        "Purchase Type"
    )

    fig = px.pie(
        purchase_sales,
        names="Purchase Type",
        values="Revenue",
        hole=0.4
    )

    fig.update_layout(
        height=380
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )