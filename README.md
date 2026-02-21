# 📊 Customer Insights & Segmentation Dashboard

## Overview

This project analyzes e-commerce transactional data to understand revenue trends and customer behavior.  
It combines time-based revenue analysis with RFM (Recency, Frequency, Monetary) segmentation using KMeans clustering to identify meaningful customer groups.

The final output is an interactive Streamlit dashboard that presents business-ready insights.

---

## 🎯 Project Objectives

- Analyze revenue trends year-wise, month-wise, and weekday-wise  
- Perform RFM-based customer profiling  
- Segment customers using KMeans clustering  
- Identify high-value, regular, and at-risk customer segments  
- Visualize revenue contribution across segments  

---

## 📂 Dataset

The dataset contains transactional e-commerce records including:

- Invoice Date  
- Customer ID  
- Invoice Number  
- Quantity  
- Unit Price  

From this data, total revenue and behavioral metrics were derived.

---

## 🧠 Segmentation Methodology

Customer behavior was summarized using:

- **Recency** – Days since last purchase  
- **Frequency** – Number of transactions  
- **Monetary** – Total spending  

Before clustering:
- Log transformation was applied to reduce skewness  
- StandardScaler was used for feature normalization  

KMeans clustering was used to divide customers into 4 behavioral segments.

---

## 📈 Insights Generated

- Identified a high-value segment contributing the majority of revenue  
- Observed revenue concentration patterns (Pareto-like behavior)  
- Detected inactive customer segments indicating churn risk  
- Analyzed seasonal revenue patterns across months and weekdays  

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## 🚀 How to Run the Project

```bash
git clone https://github.com/lakshya8839/Customer-Segmentation.git
cd Customer-Segmentation
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure

```bash
app.py              # Main dashboard application  
data.csv            # Dataset  
requirements.txt    # Python dependencies  
.env                # Environment configuration (not pushed to GitHub)  
.gitignore          # Ignored files  
README.md           # Project documentation  
```
---
## 👨‍💻 Author
Lakshya Chalana
B.Tech CSE
Focused on Data Analytics, Machine Learning & Applied AI