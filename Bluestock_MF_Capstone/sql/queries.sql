-- =====================================================
-- 1. Top 5 Funds by AUM
-- =====================================================

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- =====================================================
-- 2. Average NAV per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- =====================================================
-- 3. SIP Year-wise Growth
-- =====================================================

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_amount
FROM investor_transactions
WHERE transaction_type='SIP'
GROUP BY year
ORDER BY year;

-- =====================================================
-- 4. Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- =====================================================
-- 5. Funds with Expense Ratio < 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- =====================================================
-- 6. Highest NAV
-- =====================================================

SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC;

-- =====================================================
-- 7. Lowest NAV
-- =====================================================

SELECT
    amfi_code,
    MIN(nav) AS lowest_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY lowest_nav;

-- =====================================================
-- 8. Average Expense Ratio
-- =====================================================

SELECT
    ROUND(AVG(expense_ratio_pct),2) AS average_expense_ratio
FROM scheme_performance;

-- =====================================================
-- 9. KYC Status Count
-- =====================================================

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;

-- =====================================================
-- 10. Total Investment by Fund
-- =====================================================

SELECT
    amfi_code,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY amfi_code
ORDER BY total_investment DESC;