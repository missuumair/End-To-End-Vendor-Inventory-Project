🧾 Vendor Performance Analysis – Retail Inventory & Sales
Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI.

📌 Table of Contents
Overview
Business Problem
Dataset
Tools & Technologies
Project Structure
Data Cleaning & Preparation
Exploratory Data Analysis (EDA)
Research Questions & Key Findings
Dashboard
How to Run This Project
Final Recommendations
Author & Contact
Overview
This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL, Python for analysis and hypothesis testing, and Power BI for visualization.

Business Problem
Effective inventory and sales management are critical in the retail sector. This project aims to:

Identify underperforming brands needing pricing or promotional adjustments
Determine vendor contributions to sales and profits
Analyze the cost-benefit of bulk purchasing
Investigate inventory turnover inefficiencies
Statistically validate differences in vendor profitability
Dataset
Multiple CSV files located in /data/ folder (sales, vendors, inventory)
Summary table created from ingested data and used for analysis
Tools & Technologies
SQL (Common Table Expressions, Joins, Filtering)
Python (Pandas, Matplotlib, Seaborn, SciPy)
Power BI (Interactive Visualizations)
GitHub
Data Cleaning & Preparation
Removed transactions with:
Gross Profit ≤ 0
Profit Margin ≤ 0
Sales Quantity = 0
Created summary tables with vendor-level metrics
Converted data types, handled outliers, merged lookup tables
Exploratory Data Analysis (EDA)
Negative or Zero Values Detected:

Gross Profit: Min -52,002.78 (loss-making sales)
Profit Margin: Min -∞ (sales at zero or below cost)
Unsold Inventory: Indicating slow-moving stock
Outliers Identified:

High Freight Costs (up to 257K)
Large Purchase/Actual Prices
Correlation Analysis:

Weak between Purchase Price & Profit
Strong between Purchase Qty & Sales Qty (0.999)
Negative between Profit Margin & Sales Price (-0.179)
Research Questions & Key Findings
Brands for Promotions: 198 brands with low sales but high profit margins
Top Vendors: Top 10 vendors = 65.69% of purchases → risk of over-reliance
Bulk Purchasing Impact: 72% cost savings per unit in large orders
Inventory Turnover: $2.71M worth of unsold inventory
Vendor Profitability:
High Vendors: Mean Margin = 31.17%
Low Vendors: Mean Margin = 41.55%
Hypothesis Testing: Statistically significant difference in profit margins → distinct vendor strategies
