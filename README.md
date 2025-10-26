# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using **SQL**, **Python**, and **Power BI**.

---

## 📌 Table of Contents
- [Overview](#overview)  
- [Business Problem](#business-problem)  
- [Dataset](#dataset)  
- [Tools & Technologies](#tools--technologies)  
- [Project Structure](#project-structure)  
- [Data Cleaning & Preparation](#data-cleaning--preparation)  
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
- [Research Questions & Key Findings](#research-questions--key-findings)  
- [Dashboard](#dashboard)  
- [How to Run This Project](#how-to-run-this-project)  
- [Final Recommendations](#final-recommendations)  
- [Author & Contact](#author--contact)  

---

## Overview
This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using **SQL** for ETL, **Python** for analysis and hypothesis testing, and **Power BI** for visualization.

---

## Business Problem
Effective inventory and sales management are critical in the retail sector. This project aims to:

- Identify underperforming brands needing pricing or promotional adjustments  
- Determine vendor contributions to sales and profits  
- Analyze the cost-benefit of bulk purchasing  
- Investigate inventory turnover inefficiencies  
- Statistically validate differences in vendor profitability  

---

## Dataset
- Multiple CSV files located in `/data/` folder: **sales, vendors, inventory**  
- A summary table was created from ingested data and used for analysis  

---

## Tools & Technologies
- **SQL:** Common Table Expressions, Joins, Filtering  
- **Python:** Pandas, Matplotlib, Seaborn, SciPy  
- **Power BI:** Interactive Visualizations  

---

## Project Structure
```
vendor-performance-analysis/
├── scripts/
│   ├── ingestion_db.py
│   └── Vendor_Summary_GET.py
├── notebooks/
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance Analysis.ipynb
├── dashboard/
│   └── Vendor Sales.pbix
└── README.md
```



---

## Data Cleaning & Preparation
- Removed transactions with:  
  - `Gross Profit ≤ 0`  
  - `Profit Margin ≤ 0`  
  - `Sales Quantity = 0`  
- Created summary tables with vendor-level metrics  
- Converted data types, handled outliers, merged lookup tables  

---

## Exploratory Data Analysis (EDA)
- **Negative or Zero Values Detected:**  
  - Gross Profit: Min -52,002.78 (loss-making sales)  
  - Profit Margin: Min -∞ (sales at zero or below cost)  
  - Unsold Inventory: Indicates slow-moving stock  

- **Outliers Identified:**  
  - High Freight Costs (up to 257K)  
  - Large Purchase/Actual Prices  

- **Correlation Analysis:**  
  - Weak between Purchase Price & Profit  
  - Strong between Purchase Qty & Sales Qty (0.999)  
  - Negative between Profit Margin & Sales Price (-0.179)  

---

## Research Questions & Key Findings
- **Brands for Promotions:** 198 brands with low sales but high profit margins  
- **Top Vendors:** Top 10 vendors = 65.69% of purchases → risk of over-reliance  
- **Bulk Purchasing Impact:** 72% cost savings per unit in large orders  
- **Inventory Turnover:** $2.71M worth of unsold inventory  
- **Vendor Profitability:**  
  - High Vendors: Mean Margin = 31.17%  
  - Low Vendors: Mean Margin = 41.55%  
- **Hypothesis Testing:** Statistically significant difference in profit margins → distinct vendor strategies  

---

## Dashboard
Interactive **Power BI** dashboards were created to visualize vendor performance, sales distribution, and inventory turnover.  

---

## How to Run This Project
1. Clone the repository  
# Vendor Performance Analysis

## How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/missuumair/End-To-End-Vendor-Inventory-Project.git
cd End-To-End-Vendor-Inventory-Project
```

### 2. Load CSVs and Ingest into Database
```bash
python scripts/ingestion_db.py
```

### 3. Create Vendor Summary Table
```bash
python scripts/Vendor_Summary_GET.py
```

### 4. Run Analysis Notebooks
Open and run the following Jupyter notebooks in order:
- `notebooks/Exploratory Data Analysis.ipynb`
- `notebooks/vendor_performance_analysis.ipynb`

### 5. Open Power BI Dashboard
Open the dashboard file:
```
dashboard/Vendor Sales.pbix
```

## Prerequisites
- Python 3.x
- Jupyter Notebook
- Power BI Desktop
- Required Python packages (see `requirements.txt`)


## Final Recommendations

### 1. Diversify Vendor Base
- Reduce dependency on single vendors to minimize risk
- Identify and onboard reliable alternative suppliers

### 2. Optimize Bulk Order Strategies
- Analyze order patterns to determine optimal bulk ordering quantities
- Negotiate better terms for high-volume purchases
- Balance inventory holding costs with bulk discounts

### 3. Reprice Slow-Moving, High-Margin Brands
- Identify products with low turnover rates but high profit margins
- Implement dynamic pricing strategies to improve sales velocity
- Consider promotional pricing for aged inventory

### 4. Clear Unsold Inventory Strategically
- Develop clearance strategies for slow-moving stock
- Bundle products to move stagnant inventory
- Implement seasonal sales and discount campaigns

### 5. Improve Marketing for Underperforming Vendors
- Analyze marketing effectiveness by vendor
- Increase visibility for high-quality but underperforming brands
- Create targeted campaigns to boost sales
- Optimize product placement and recommendations


Author & Contact

Mohammed Misabahuddin

Email: missuumair@gmail.com
]

GitHub: https://github.com/missuumair
