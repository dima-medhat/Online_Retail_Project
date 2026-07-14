
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Online Retail Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

# Load the cleaned retail dataset
df = pd.read_csv("Online_Retail_Cleaned.csv")

# ---------------- SIDEBAR ----------------

st.logo("clipart2179733.png")
st.sidebar.title("🎛️ Filter Options")

selected_year = st.sidebar.selectbox(label="📅 Select Year", options=df["InvoiceYear"].unique())

selected_quarter = st.sidebar.selectbox(label="📊 Select Quarter",options=df["InvoiceQuarter"].unique())

selected_country = st.sidebar.selectbox(label="🌍 Select Country",options=df["Country"].unique())

# Apply filters
filtered_df = df[(df["InvoiceYear"] == selected_year)
    & (df["InvoiceQuarter"] == selected_quarter)
    & (df["Country"] == selected_country)]

# ---------------- CHARTS ----------------

# Chart 1: Revenue by year and quarter
revenue_year_quarter = filtered_df.groupby(["InvoiceYear", "InvoiceQuarter"])["Revenue"].sum().reset_index()

fig1 = px.bar(
    revenue_year_quarter,
    x="InvoiceQuarter",
    y="Revenue",
    color="InvoiceYear",
    barmode="group",
    title="Revenue by Year and Quarter")

# Chart 2: Revenue by month
revenue_month = filtered_df.groupby("InvoiceMonth")["Revenue"].sum().reset_index()


fig2 = px.bar(
    revenue_month,
    x="InvoiceMonth",
    y="Revenue",
    title="Revenue by Month")

# Chart 3: Revenue by weekday and hour
revenue_day_hour = pd.pivot_table(
    filtered_df,
    index="InvoiceWeekday",
    columns="InvoiceHour",
    values="Revenue",
    aggfunc="sum")

weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday"]

revenue_day_hour = revenue_day_hour.reindex(weekday_order)

fig3 = px.imshow(
    revenue_day_hour,
    labels={"x": "Hour","y": "Weekday","color": "Revenue"},
    title="Revenue by Weekday and Hour",
    aspect="auto")

# Chart 4: Product revenue by country
product_revenue_country = filtered_df.groupby(["Country", "Description"])["Revenue"].sum().reset_index()

fig4 = px.treemap(
    product_revenue_country,
    path=["Country", "Description"],
    values="Revenue",
    title="Product Revenue by Country")

# Chart 5: Customer purchase frequency
customer_frequency = filtered_df.groupby("CustomerID")["InvoiceNo"].nunique().reset_index(name="Orders")

purchase_frequency = (
    customer_frequency.groupby("Orders")["CustomerID"]
    .count()
    .reset_index(name="Customers"))

fig5 = px.bar(
    purchase_frequency,
    x="Orders",
    y="Customers",
    title="Customer Purchase Frequency")

# Chart 6: Top products by revenue
top_products = filtered_df.groupby("Description")["Revenue"].sum().reset_index().sort_values("Revenue", ascending=False).head(10)

fig6 = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    title="Top 10 Products by Revenue")

# ---------------- TITLE ----------------

st.title("🛍️ Retail Sales Dashboard")
st.caption("Interactive Overview of Retail Sales Performance")

# ---------------- KPIs ----------------

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric(
        label="💰 Total Revenue",
        value=f"${filtered_df['Revenue'].sum():,.2f}",
        border=True)

with info2:
    st.metric(
        label="📦 Products Sold",
        value=f"{filtered_df['Quantity'].sum():,}",
        border=True)

with info3:
    st.metric(
        label="🛒 Total Orders",
        value=f"{filtered_df['InvoiceNo'].nunique():,}",
        border=True)

with info4:
    st.metric(
        label="🏷️ Total Products",
        value=f"{filtered_df['Description'].nunique():,}",
        border=True)

st.divider()


# charts

chart1, chart2 = st.columns(2)

with chart1:
    st.plotly_chart(fig3, width="stretch")

with chart2:
    st.plotly_chart(fig4, width="stretch")

st.divider()


chart3, chart4, chart5, chart6 = st.columns(4)

with chart3:
    st.plotly_chart(fig1, width="stretch")

with chart4:
    st.plotly_chart(fig2, width="stretch")

with chart5:
    st.plotly_chart(fig5, width="stretch")

with chart6:
    st.plotly_chart(fig6, width="stretch")
