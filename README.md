# Sales Data Analysis & Interactive Dashboard (Python + Pandas + Streamlit)

## Project Overview

This project presents a complete sales data analysis workflow implemented in Python in two different versions:

* **Version 1 – Classical Data Analysis (`analysis.py`)** – uses Pandas for data processing and Matplotlib for static data visualization.
* **Version 2 – Interactive Dashboard (`app.py`)** – a web application built with Streamlit and Plotly Express that enables interactive data exploration through filters and dynamic visualizations.

Both versions share the same data preparation pipeline and reusable modules responsible for data loading, preprocessing, aggregation, and KPI calculations.

The project uses the **Restaurant Sales Data** dataset created by Data Science Lovers:
https://www.kaggle.com/datasets/rohitgrewal/restaurant-sales-data/data

The goal of the project is to demonstrate a complete data analysis workflow, starting from data cleaning and preprocessing, through exploratory data analysis (EDA), and ending with an interactive business dashboard.

---

# Technologies

* Python 3
* Pandas – data analysis and manipulation
* Matplotlib – static data visualization
* Streamlit – interactive web dashboard
* Plotly Express – interactive charts

---

# Data Analysis Workflow

## 1. Data Loading

* Load data from a CSV file
* Validate required columns
* Clean text values (remove unnecessary whitespace)

## 2. Data Preprocessing

* Convert dates to `datetime`
* Convert numeric values (`Price`, `Quantity`)
* Remove invalid and missing records
* Remove duplicate rows
* Create additional features:

  * `Revenue`
  * `Month`
  * `DayOfWeek`
  * `Year`

## 3. KPI Calculation

The project calculates several key business metrics:

* Total number of orders
* Total revenue
* Average order value
* Number of unique products
* Number of cities

## 4. Data Aggregation

The data is aggregated by:

* City
* Product
* Manager
* Purchase Type
* Payment Method

---

# Version 1 – Classical Data Analysis (`analysis.py`)

This version focuses on traditional exploratory data analysis using **Pandas** and **Matplotlib**. After preprocessing, the project generates static charts and business insights based on aggregated sales data.

### Visualizations

### Revenue by City

<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/266549a0-6374-412a-a5d7-de9e87175ec2" />

### Revenue by Product

<img width="1000" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/93d2e350-0acc-498f-b5c0-b6793ff936c5" />

### Revenue Trend Over Time

<img width="1200" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/6775a9dd-5937-47c6-a307-205ff7845ce1" />

### Revenue by Purchase Type

<img width="800" height="500" alt="Figure_4" src="https://github.com/user-attachments/assets/d5109b31-b79f-4a48-9efe-09bff8237a8f" />

### Revenue by Payment Method

<img width="700" height="700" alt="Figure_5" src="https://github.com/user-attachments/assets/2d28a723-12c0-438b-88f7-799f0e47741d" />

---

# Version 2 – Interactive Dashboard (`app.py`)

The second version presents the same analysis as an interactive web dashboard built with **Streamlit** and **Plotly Express**. It allows users to explore the data dynamically using filters and automatically updated KPIs and charts.

## Features

### Interactive Filters

Users can filter the data by:

* City
* Product
* Manager

All KPIs and visualizations are updated automatically based on the selected filters.

### KPI Dashboard

The dashboard displays key business metrics, including:

* Total Revenue
* Number of Orders
* Average Order Value
* Number of Unique Products

### Interactive Visualizations

The dashboard includes:

* Revenue trend over time
* Revenue by city
* Manager performance
* Top 5 best-selling products
* Revenue by payment method
* Revenue by purchase type

### Performance Optimization

The application uses the `@st.cache_data` decorator to cache loaded and preprocessed data, reducing unnecessary computations and improving performance.

## Dashboard Preview

<img width="1891" height="440" alt="image" src="https://github.com/user-attachments/assets/79f42c1c-95de-4304-813c-080afc3a657a" />

<img width="1447" height="557" alt="image" src="https://github.com/user-attachments/assets/81a840a7-9dbe-4662-8fa8-9dfefff259a0" />

<img width="1447" height="625" alt="image" src="https://github.com/user-attachments/assets/6bbd011f-9cd8-4e37-9491-0ff4faf014db" />

<img width="1457" height="561" alt="image" src="https://github.com/user-attachments/assets/1d48422a-15a9-44e4-b45d-9885a7d8739f" />

