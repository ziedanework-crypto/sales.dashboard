import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Regional Sales Dashboard", layout="wide")
st.title("📍 Regional Sales Performance Dashboard")
st.markdown("A comprehensive analysis of sales and customer performance across regions.")

# Data
data = {
    "Area": ["01-SH", "02-KH", "03-QL", "04-QA", "05-BE", "06-TKH", "07-MAH", "08-AN", "09-ST"],
    "Sales Target": [2850000, 3200000, 2800000, 3600000, 2800000, 1900000, 3000000, 1000000, 1500000],
    "Sales": [1136113, 1005132, 960941, 1664922, 1119000, 634196, 644196, 314155, 297140],
    "Sales %": [40, 31, 34, 46, 40, 33, 22, 31, 20],
    "Customer Target": [220, 220, 170, 180, 140, 100, 20, 5, 5],
    "Customers": [133, 155, 99, 104, 72, 56, 11, 3, 2],
    "Customer %": [60, 70, 58, 58, 51, 56, 55, 60, 40]
}

df = pd.DataFrame(data)

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("📈 Avg. Sales Achievement", f"{df['Sales %'].mean():.1f}%")
col2.metric("👥 Avg. Customer Achievement", f"{df['Customer %'].mean():.1f}%")
col3.metric("🏅 Top Performing Area", df.loc[df['Sales %'].idxmax(), 'Area'])

# Bar Chart: Sales %
st.subheader("📊 Sales Achievement by Area")
fig1 = px.bar(df, x="Area", y="Sales %", color="Sales %",
              text="Sales %", color_continuous_scale="Viridis",
              title="Sales Achievement (%)")
st.plotly_chart(fig1, use_container_width=True)

# Bar Chart: Customer %
st.subheader("👥 Customer Achievement by Area")
fig2 = px.bar(df, x="Area", y="Customer %", color="Customer %",
              text="Customer %", color_continuous_scale="Blues",
              title="Customer Achievement (%)")
st.plotly_chart(fig2, use_container_width=True)

# Pie Chart: Sales Distribution
st.subheader("🍩 Sales Distribution by Area")
fig3 = px.pie(df, names="Area", values="Sales", title="Share of Total Sales")
st.plotly_chart(fig3, use_container_width=True)

# Pie Chart: Customer Distribution
st.subheader("🍩 Customer Distribution by Area")
fig4 = px.pie(df, names="Area", values="Customers", title="Share of Total Customers")
st.plotly_chart(fig4, use_container_width=True)

# Full Data Table
st.subheader("📋 Full Performance Table")
st.dataframe(df)

# Area Filter
selected_area = st.selectbox("🔍 Select an Area to View Details", df["Area"])
filtered = df[df["Area"] == selected_area]
st.write("📌 Selected Area Details:")
st.dataframe(filtered)
