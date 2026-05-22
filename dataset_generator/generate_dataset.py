import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

n = 5000

product_types = ['Personal Loan', 'Business Loan', 'Vehicle Finance', 'Home Loan', 'MSME Loan']
product_weights = [0.25, 0.20, 0.20, 0.15, 0.20]

branch_tiers = ['Urban', 'Semi-Urban', 'Rural']
branch_tier_weights = [0.40, 0.35, 0.25]

statuses = ['Disbursed', 'Rejected', 'Under Review', 'Pending Documents']
status_weights = [0.65, 0.15, 0.12, 0.08]

states = ['Rajasthan', 'Gujarat', 'Maharashtra', 'Madhya Pradesh', 'Uttar Pradesh',
          'Punjab', 'Haryana', 'Tamil Nadu', 'Karnataka', 'Odisha']

def get_stage_tat(product, branch_tier, stage):
    base = {
        'Application Submission': {'Urban': (2,6), 'Semi-Urban': (4,10), 'Rural': (8,18)},
        'Document Verification':  {'Urban': (8,24), 'Semi-Urban': (12,36), 'Rural': (24,60)},
        'Credit Assessment':      {'Urban': (12,36), 'Semi-Urban': (18,48), 'Rural': (24,72)},
        'Approval/Rejection':     {'Urban': (4,12), 'Semi-Urban': (8,20), 'Rural': (12,30)},
        'Loan Disbursal':         {'Urban': (6,18), 'Semi-Urban': (10,28), 'Rural': (18,48)},
    }
    lo, hi = base[stage][branch_tier]
    if product in ['MSME Loan', 'Business Loan'] and stage == 'Credit Assessment':
        lo, hi = int(lo*1.4), int(hi*1.6)
    if product == 'Home Loan' and stage == 'Document Verification':
        lo, hi = int(lo*1.3), int(hi*1.5)
    return round(np.random.uniform(lo, hi), 1)

stages = ['Application Submission', 'Document Verification', 'Credit Assessment', 'Approval/Rejection', 'Loan Disbursal']
sla_hours = {'Application Submission': 8, 'Document Verification': 24, 'Credit Assessment': 48, 'Approval/Rejection': 16, 'Loan Disbursal': 24}

records = []
start_date = datetime(2024, 1, 1)

for i in range(n):
    product = np.random.choice(product_types, p=product_weights)
    branch_tier = np.random.choice(branch_tiers, p=branch_tier_weights)
    state = random.choice(states)
    status = np.random.choice(statuses, p=status_weights)
    loan_amount = round(np.random.lognormal(mean=12.5, sigma=1.1), -3)
    loan_amount = max(50000, min(loan_amount, 5000000))

    app_date = start_date + timedelta(days=random.randint(0, 500))
    month = app_date.strftime('%Y-%m')

    row = {
        'Application_ID': f'AU{2024000+i:06d}',
        'Application_Date': app_date.strftime('%Y-%m-%d'),
        'Month': month,
        'Product_Type': product,
        'Branch_Tier': branch_tier,
        'State': state,
        'Status': status,
        'Loan_Amount': loan_amount,
        'Customer_Segment': np.random.choice(['Salaried', 'Self-Employed', 'MSME Owner', 'Farmer'],
                                              p=[0.35, 0.30, 0.20, 0.15]),
    }

    total_tat = 0
    for stage in stages:
        tat = get_stage_tat(product, branch_tier, stage)
        if status == 'Rejected' and stage == 'Loan Disbursal':
            tat = 0
        if status == 'Under Review' and stage in ['Approval/Rejection', 'Loan Disbursal']:
            tat = 0
        row[f'TAT_{stage.replace("/","_").replace(" ","_")}_hrs'] = tat
        row[f'SLA_Breach_{stage.replace("/","_").replace(" ","_")}'] = 1 if tat > sla_hours[stage] and tat > 0 else 0
        total_tat += tat

    row['Total_TAT_hrs'] = round(total_tat, 1)
    row['Total_TAT_days'] = round(total_tat / 24, 1)
    row['SLA_Breached'] = 1 if any(row[f'SLA_Breach_{s.replace("/","_").replace(" ","_")}'] for s in stages) else 0
    records.append(row)

df = pd.DataFrame(records)
df.to_csv('AU_Bank_Loan_Operations_Data.csv', index=False)
print(f"Dataset generated: {len(df)} rows, {len(df.columns)} columns")
