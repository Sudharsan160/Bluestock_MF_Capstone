# Data Dictionary

## 1. 02_nav_history.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Unique Mutual Fund AMFI Code |
| date | Date | NAV Date |
| nav | Decimal | Net Asset Value |

---

## 2. 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| investor_id | String | Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Mutual Fund AMFI Code |
| transaction_type | String | SIP / Lumpsum / Redemption |
| amount_inr | Decimal | Investment Amount |
| state | String | Investor State |
| city | String | Investor City |
| city_tier | String | Tier of City |
| age_group | String | Investor Age Group |
| gender | String | Gender |
| annual_income_lakh | Decimal | Annual Income (Lakhs) |
| payment_mode | String | Payment Method |
| kyc_status | String | KYC Status |

---

## 3. 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|-----------|-------------|
| amfi_code | Integer | Mutual Fund AMFI Code |
| scheme_name | String | Mutual Fund Scheme |
| fund_house | String | AMC Name |
| category | String | Fund Category |
| plan | String | Direct / Regular |
| return_1yr_pct | Decimal | 1-Year Return (%) |
| return_3yr_pct | Decimal | 3-Year Return (%) |
| return_5yr_pct | Decimal | 5-Year Return (%) |
| benchmark_3yr_pct | Decimal | Benchmark Return |
| alpha | Decimal | Alpha |
| beta | Decimal | Beta |
| sharpe_ratio | Decimal | Sharpe Ratio |
| sortino_ratio | Decimal | Sortino Ratio |
| std_dev_ann_pct | Decimal | Standard Deviation |
| max_drawdown_pct | Decimal | Maximum Drawdown |
| aum_crore | Decimal | Assets Under Management |
| expense_ratio_pct | Decimal | Expense Ratio |
| morningstar_rating | Integer | Morningstar Rating |
| risk_grade | String | Risk Category |

---

## Source

All datasets were provided as part of the Bluestock Mutual Fund Capstone Project.