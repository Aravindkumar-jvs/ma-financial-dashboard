# 📊 M&A Financial Dashboard — Power BI

An interactive Power BI dashboard analyzing **100 M&A transactions** across industries, regions, and deal types. Built to simulate the kind of financial analytics used in real-world transaction advisory (Restructuring, Diligence, and Valuations).

---

## 🔍 Project Overview

This project replicates a simplified version of M&A deal tracking and financial analysis — the type of work done by transaction advisory teams at firms like EY, Deloitte, and Goldman Sachs.

The dashboard enables stakeholders to:
- Monitor deal pipeline by stage and region
- Analyze valuation multiples (EV/EBITDA, EV/Revenue) across industries
- Track synergy estimates and acquisition premiums
- Identify trends by year, quarter, and deal type

---

## 📁 Repository Structure

```
ma-financial-dashboard/
│
├── data/
│   └── ma_deals_dataset.csv        # 100 simulated M&A transactions
│
├── scripts/
│   └── generate_ma_data.py         # Python script to regenerate dataset
│
├── dashboard/
│   └── MA_Dashboard.pbix           # Power BI dashboard file
│
├── screenshots/
│   └── overview.png                # Dashboard preview
│
└── README.md
```

---

## 📊 Dashboard Pages

| Page | Description |
|------|-------------|
| **Deal Overview** | Total deal value, count, avg premium, stage breakdown |
| **Industry Analysis** | EV/EBITDA multiples and deal volume by sector |
| **Regional View** | Geographic distribution and regional deal value |
| **Valuation Metrics** | Scatter plots of deal value vs. multiples |
| **Timeline Trends** | Quarterly and yearly deal activity trends |

---

## 🧰 Tools & Technologies

- **Power BI Desktop** — Dashboard design and DAX measures
- **Python (pandas)** — Data generation and preprocessing
- **CSV / Excel** — Data source format
- **DAX** — Custom calculated columns and KPIs

---

## 📐 Key DAX Measures Used

```dax
-- Average EV/EBITDA Multiple
Avg EV/EBITDA = AVERAGE(ma_deals_dataset[EV_EBITDA_Multiple])

-- Total Deal Value
Total Deal Value ($M) = SUM(ma_deals_dataset[Deal_Value_USD_M])

-- Deal Completion Rate
Completion Rate = 
DIVIDE(
    COUNTROWS(FILTER(ma_deals_dataset, ma_deals_dataset[Stage] = "Completed")),
    COUNTROWS(ma_deals_dataset)
) * 100

-- Average Acquisition Premium
Avg Premium = AVERAGE(ma_deals_dataset[Acquisition_Premium_Pct])
```

---

## 📈 Dataset Fields

| Column | Description |
|--------|-------------|
| Deal_ID | Unique deal identifier |
| Acquirer / Target | Company names |
| Industry | Sector classification |
| Deal_Type | Acquisition, Merger, Divestiture, etc. |
| Stage | Announced, Due Diligence, Completed, Terminated |
| Region | Geographic region |
| Deal_Value_USD_M | Transaction value in USD millions |
| EV_EBITDA_Multiple | Enterprise value to EBITDA ratio |
| EV_Revenue_Multiple | Enterprise value to revenue ratio |
| Synergies_USD_M | Estimated cost/revenue synergies |
| Acquisition_Premium_Pct | Premium paid over market price |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ma-financial-dashboard.git
   ```

2. (Optional) Regenerate the dataset:
   ```bash
   pip install pandas
   python scripts/generate_ma_data.py
   ```

3. Open `dashboard/MA_Dashboard.pbix` in **Power BI Desktop**

4. If prompted, update the data source path to your local `data/ma_deals_dataset.csv`

---

## 💡 Key Insights from the Data

- **Technology** sector commands the highest EV/EBITDA multiples on average
- **North America** accounts for the largest share of deal volume by value
- **Leveraged Buyouts** show the highest acquisition premiums (~35–50%)
- Deal activity peaks in **Q3** across all years in the dataset

---

## 🎯 Relevance to Industry

This project mirrors the analytical work done in:
- **Transaction Advisory Services** (EY SaT, Deloitte M&A)
- **Investment Banking** (deal screening and valuation)
- **Private Equity** (portfolio and pipeline tracking)

---

## 👤 Author

**[Your Name]**  
Final Year B.Tech — Computer Science  
[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

---

## 📄 License

MIT License — free to use and modify for learning purposes.
