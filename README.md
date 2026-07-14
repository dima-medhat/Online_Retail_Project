# 🛍️ Online Retail Interactive Dashboard

## 📖 Project Overview

This project analyzes an online retail dataset and presents the results through an interactive dashboard built with Python, Pandas, Plotly, and Streamlit. The project follows a complete data analysis workflow, starting from raw data cleaning and feature engineering to interactive visualization and deployment.

## 🎯 Objectives

- Clean and preprocess the retail dataset.
- Perform feature engineering to create meaningful features.
- Explore the dataset using interactive visualizations.
- Build an interactive dashboard using Streamlit.
- Deploy the dashboard using Ngrok.

## 🛠️ Technologies Used

- Python
- Pandas
- Plotly Express
- Streamlit
- Ngrok
- Google Colab

## 📂 Project Structure

- `Online_Retail_Project.ipynb` – Complete data analysis notebook.
- `app.py` – Streamlit dashboard application.
- `README.md` – Project documentation.

## 🧹 Data Preparation

The dataset was prepared through several preprocessing steps, including:

- Removing duplicate records.
- Handling missing values.
- Correcting data types.
- Creating a Revenue column.
- Feature engineering for Year, Quarter, Month, Weekday, and Hour.

## 📊 Dashboard Features

### Filters

- Year
- Quarter
- Country

### KPI Cards

- 💰 Total Revenue
- 📦 Products Sold
- 🛒 Total Orders
- 🏷️ Total Products

### Interactive Visualizations

- Revenue by Weekday and Hour (Heatmap)
- Product Revenue by Country (Treemap)
- Revenue by Year and Quarter
- Revenue by Month
- Customer Purchase Frequency
- Top 10 Products by Revenue

All KPIs and charts update automatically based on the selected filters.

## 🚀 Running the Project

1. Install the required libraries.


pip install pandas plotly streamlit pyngrok


2. Run the Streamlit application.


streamlit run app.py


3.  Use Ngrok to generate a public URL for sharing the dashboard.

## 📸 Demo

This repository includes screenshots and a short demonstration video showing the dashboard and its interactive features.

## 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning with Pandas.
- Feature engineering.
- Interactive visualization using Plotly.
- Building dashboards with Streamlit.
- Deploying applications using Ngrok.
- Developing an end-to-end data analytics workflow.

## 📌 Conclusion

This project demonstrates how raw transactional data can be transformed into meaningful business insights through data preprocessing, visualization, and interactive dashboard development. It reflects the complete workflow of a real-world data analytics project using Python.
