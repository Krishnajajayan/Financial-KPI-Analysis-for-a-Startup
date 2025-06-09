#  Startup Financial KPI Dashboard

**Project Title:** Financial KPI Analysis for a Startup  
**Tools Used:** Power BI, Python (Pandas), Excel  
**Domain:** Finance, Startups, Business Analytics

---

##  Objective

To analyze key financial performance metrics of early-stage startups using an interactive dashboard.  
The main KPIs evaluated are:
- Burn Rate
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- LTV:CAC Ratio
- Monthly Run Rate
- Profitability

---

##  Dataset

The project uses the `50_Startups.csv` dataset, which includes:
- R&D Spend
- Administration Cost
- Marketing Spend
- State
- Profit

Additional fields were engineered:
- Burn_Rate
- Run_Rate
- CAC
- LTV
- LTV_CAC_Ratio
- Cohort

---

##  Steps Involved

1. **Data Preprocessing (Python):**
   - Loaded and cleaned the dataset
   - Engineered financial KPIs using assumptions for customer base and customer lifetime
   - Exported processed data as `financial_kpi_output.csv`

2. **Dashboard Development (Power BI):**
   - Imported KPI dataset into Power BI
   - Created summary cards and visualizations:
     - Burn Rate by State
     - Run Rate by Startup Cohort
     - LTV:CAC Ratio by Cohort
     - Customer Acquisition Efficiency (LTV vs CAC Scatter)
     - Top 5 Startups by Profit
   - Added slicers for interactive filtering by `State` and `Cohort`

---

##  Key Insights

-  **Cohort 3** outperformed all other groups with the **highest average LTV:CAC ratio**, indicating highly efficient customer acquisition and long-term profitability.
-  **Florida** consistently had the **highest average Burn Rate**, yet some of its startups also achieved top profits — suggesting high spending pays off when paired with strong revenue.
-  **New York startups** had relatively **balanced CAC and LTV**, showing a more conservative but stable growth strategy compared to California and Florida.
-  Some startups showed **LTV:CAC ratios above 15**, while others fell below 5 — highlighting major differences in marketing efficiency across cohorts and regions.
-  A few rows displayed **infinite or NaN values for LTV:CAC**, due to extremely low or zero CAC values — these are outliers and should be flagged for further investigation.
-  **Cohorts 3, 4, and 7** showed the most promising **Run Rate and LTV combinations**, making them likely candidates for funding or scaling decisions.
-  Despite higher burn rates, startups with **consistent profits and high LTV (like in Cohorts 3 & 5)** demonstrate a good balance of spending and revenue generation.

---

##  Conclusion

This project demonstrates how financial KPIs like LTV, CAC, and Burn Rate can be used to evaluate the performance and sustainability of startups. The interactive dashboard built using Power BI helps stakeholders make data-driven decisions quickly.

---
