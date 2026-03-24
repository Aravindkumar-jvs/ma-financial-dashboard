import csv
import random
from datetime import date, timedelta

random.seed(42)

industries = ["Technology", "Healthcare", "Financial Services", "Energy", "Consumer Goods", "Manufacturing", "Telecom", "Real Estate"]
deal_types = ["Acquisition", "Merger", "Divestiture", "Joint Venture", "Leveraged Buyout"]
deal_stages = ["Announced", "Due Diligence", "Completed", "Terminated"]
regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East"]
advisors = ["Goldman Sachs", "Morgan Stanley", "JP Morgan", "EY", "Deloitte", "KPMG", "PwC", "Lazard"]

companies = [
    "AlphaTech", "BetaCorp", "GammaSolutions", "DeltaIndustries", "EpsilonGroup",
    "ZetaVentures", "EtaHoldings", "ThetaCo", "IotaSystems", "KappaEnterprises",
    "LambdaWorks", "MuMedia", "NuNetworks", "XiXchange", "OmicronOil",
    "PiPharma", "RhoRetail", "SigmaSoft", "TauTelecom", "UpsilonUtilities"
]

def random_date(start_year=2020, end_year=2024):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

rows = []
for i in range(1, 101):
    acquirer = random.choice(companies)
    target = random.choice([c for c in companies if c != acquirer])
    industry = random.choice(industries)
    deal_type = random.choice(deal_types)
    stage = random.choice(deal_stages)
    region = random.choice(regions)
    advisor = random.choice(advisors)
    ann_date = random_date()
    deal_value = round(random.uniform(50, 5000), 1)  # in $M
    ebitda = round(deal_value / random.uniform(6, 18), 1)
    revenue = round(ebitda * random.uniform(2, 6), 1)
    ev_ebitda = round(deal_value / ebitda, 1)
    ev_revenue = round(deal_value / revenue, 2)
    synergies = round(deal_value * random.uniform(0.05, 0.20), 1)
    premium = round(random.uniform(10, 55), 1)
    completion_days = random.randint(60, 540) if stage == "Completed" else None

    rows.append({
        "Deal_ID": f"MA-{1000+i}",
        "Acquirer": acquirer,
        "Target": target,
        "Industry": industry,
        "Deal_Type": deal_type,
        "Stage": stage,
        "Region": region,
        "Financial_Advisor": advisor,
        "Announcement_Date": ann_date.strftime("%Y-%m-%d"),
        "Year": ann_date.year,
        "Quarter": f"Q{(ann_date.month-1)//3+1}",
        "Deal_Value_USD_M": deal_value,
        "Target_Revenue_USD_M": revenue,
        "Target_EBITDA_USD_M": ebitda,
        "EV_EBITDA_Multiple": ev_ebitda,
        "EV_Revenue_Multiple": ev_revenue,
        "Synergies_USD_M": synergies,
        "Acquisition_Premium_Pct": premium,
        "Days_to_Completion": completion_days if completion_days else ""
    })

with open("/home/claude/ma_deals_dataset.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Dataset generated: ma_deals_dataset.csv")
print(f"Total deals: {len(rows)}")
