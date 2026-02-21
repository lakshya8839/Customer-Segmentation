import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="Customer Insights Dashboard", layout="wide")

st.title("Customer Insights & Segmentation Dashboard")

st.markdown("""
### 📌 Project Overview
This project analyzes transactional e-commerce data to understand customer behavior and revenue patterns.  
It combines time-based revenue analysis with RFM-based customer segmentation.

### 🎯 Objective
- Analyze revenue trends year-wise, month-wise, and weekday-wise  
- Segment customers using Recency, Frequency, and Monetary value  
- Identify high-value and at-risk customer groups  

### 🛠 Tools Used
- Python  
- Pandas & NumPy  
- Scikit-learn (KMeans Clustering)  
- Streamlit for dashboard visualization  

---
""")

st.write("Revenue trends and customer behavior analysis using RFM segmentation.")

# -------------------------------
# Load & Clean Data
# -------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv", encoding="ISO-8859-1")
    df = df.dropna(subset=["CustomerID"])
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df

df = load_data()

# -------------------------------
# Time Features
# -------------------------------

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["MonthName"] = df["InvoiceDate"].dt.month_name()
df["Weekday"] = df["InvoiceDate"].dt.day_name()

# -------------------------------
# KPI Section
# -------------------------------

total_revenue = df["TotalPrice"].sum()
total_customers = df["CustomerID"].nunique()
total_orders = df["InvoiceNo"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Customers", total_customers)
col3.metric("Total Orders", total_orders)

st.divider()

# -------------------------------
# Year-wise Revenue
# -------------------------------

st.subheader("Year-wise Revenue")

year_revenue = df.groupby("Year")["TotalPrice"].sum()

fig1, ax1 = plt.subplots()
year_revenue.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Revenue")
st.pyplot(fig1)

# -------------------------------
# Month-wise Revenue
# -------------------------------

st.subheader("Month-wise Revenue")

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

month_revenue = df.groupby("MonthName")["TotalPrice"].sum().reindex(month_order)

fig2, ax2 = plt.subplots()
month_revenue.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Revenue")
st.pyplot(fig2)

# -------------------------------
# Weekday-wise Revenue
# -------------------------------

st.subheader("Weekday Revenue Pattern")

weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

weekday_revenue = df.groupby("Weekday")["TotalPrice"].sum().reindex(weekday_order)

fig3, ax3 = plt.subplots()
weekday_revenue.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Revenue")
st.pyplot(fig3)

st.divider()

# -------------------------------
# RFM Segmentation
# -------------------------------

st.subheader("Customer Segmentation")

latest_date = df["InvoiceDate"].max()

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (latest_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

# Log transform for clustering
rfm_log = np.log1p(rfm)

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

# -------------------------------
# Segment Summary
# -------------------------------

cluster_summary = rfm.groupby("Cluster").mean()

st.write("Average Behavior by Cluster")
st.dataframe(cluster_summary)

# -------------------------------
# Revenue Contribution by Cluster
# -------------------------------

st.subheader("Revenue Contribution by Segment")

cluster_revenue = rfm.groupby("Cluster")["Monetary"].sum()
revenue_share = cluster_revenue / cluster_revenue.sum() * 100

fig4, ax4 = plt.subplots()
revenue_share.plot(kind="bar", ax=ax4)
ax4.set_ylabel("Revenue %")
st.pyplot(fig4)

# -------------------------------
# Customer Distribution
# -------------------------------

st.subheader("Customer Distribution by Segment")

cluster_counts = rfm["Cluster"].value_counts()

fig5, ax5 = plt.subplots()
cluster_counts.plot(kind="bar", ax=ax5)
ax5.set_ylabel("Number of Customers")
st.pyplot(fig5)

st.divider()

st.write("This dashboard combines time-based revenue analysis with RFM-based customer segmentation to provide actionable business insights.")