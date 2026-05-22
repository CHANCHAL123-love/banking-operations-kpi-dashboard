# banking-operations-kpi-dashboard
Loan Processing TAT &amp; Bottleneck Analysis | Power BI Dashboard for Small Finance Bank Operations
# 🏦 Banking Operations KPI Dashboard
### Loan Processing TAT & Bottleneck Analysis | AU Small Finance Bank (Simulated)

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)

---

## 📌 Project Overview

This project simulates a real-world banking operations analytics use case for a Small Finance Bank.
The goal was to identify loan processing bottlenecks, measure SLA compliance, and recommend 
data-driven process improvements — directly mapped to the KPIs a Business Solutions & Strategy 
team would track.

**Dataset:** 5,000 simulated loan applications across 5 product types, 3 branch tiers, 
and 10 states | Jan 2024 – Jun 2025

---

## 🎯 Business Problem

Small Finance Banks serving semi-urban and rural customers face significantly higher loan 
processing times than urban branches. This directly impacts:
- Customer experience and retention
- Disbursement rates and revenue
- Operational costs and staff efficiency

**Key Question:** Where exactly in the loan lifecycle are delays occurring, 
and what interventions would have the highest impact?

---

## 📊 Dashboard Pages

### Page 1 — Operations Overview
Executive snapshot of overall performance
- Total applications, avg TAT, SLA breach rate, disbursement rate
- Monthly volume and TAT trend
- Status breakdown and branch tier comparison

### Page 2 — Bottleneck Deep Dive
Stage-by-stage processing analysis
- TAT per stage with data bars (Application → Document → Credit → Approval → Disbursal)
- SLA breach % per stage
- TAT heatmap: Branch Tier × Product Type
- MSME and Rural flagged as highest-risk combination

### Page 3 — Executive Summary
Board-ready insight page
- Key findings panel
- Recommendations panel with estimated impact
- TAT trend over time by branch tier
- Disbursed loan value by product type

---

## 🔍 Key Findings

| Finding | Data Point |
|---------|-----------|
| Rural branches are 2.4x slower than Urban | 158.9 hrs vs 66.0 hrs avg TAT |
| Document Verification & Credit Assessment = biggest bottleneck | 68% of total TAT |
| Overall SLA breach rate | 62% of all applications |
| MSME + Rural = highest risk combination | Darkest red in heatmap |
| Pending Documents stage trapping applications | 8% of total volume stuck |

---

## 💡 Recommendations

1. **Automate document verification** in Rural branches using OCR
   → Estimated TAT reduction: 35%
2. **Digitize MSME credit assessment** workflow
   → Reduce avg from 48hrs to 20hrs
3. **Deploy SLA alert system** — notify branch managers at 80% threshold
4. **WhatsApp/SMS nudges** for Pending Documents applications
   → Convert stuck 8% applications
5. **Dedicated processing teams** in Semi-Urban branches during Q1 and Q3 peak periods

---

## 🛠️ Technical Stack

| Tool | Usage |
|------|-------|
| Power BI Desktop | Dashboard development, DAX measures |
| Power Query | Data cleaning, column transformations |
| DAX | KPI measures, SLA breach calculations, time intelligence |
| Excel/CSV | Raw dataset preparation |
| Python (Pandas, NumPy) | Synthetic dataset generation |

---

## 📁 Repository Structure

├── data/
│   └── AU_Bank_Loan_Operations_Data.csv
├── dataset_generator/
│   └── generate_dataset.py
├── dashboard/
│   └── Banking Operations Dashboard.pbix
├── screenshots/
│   ├── page1_operations_overview.png
│   ├── page2_bottleneck_deepdive.png
│   └── page3_executive_summary.png
└── README.md

---

## 📸 Dashboard Preview

![Operations Overview](screenshots/page1_operations_overview.png)
![Bottleneck Deep Dive](screenshots/page2_bottleneck_deepdive.png)
![Executive Summary](screenshots/page3_executive_summary.png)

---

## ⚠️ Disclaimer

This project uses a synthetically generated dataset created for portfolio purposes.
It does not represent actual AU Small Finance Bank data.
All figures are simulated to reflect realistic banking operational patterns.
