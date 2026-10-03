SELECT 
    corridor,
    payment_rail,
    COUNT(transaction_id) AS total_transactions,
    SUM(CASE WHEN status = 'SUCCESS' THEN amount_usd ELSE 0 END) AS successful_volume_usd,
    ROUND(
        (COUNT(CASE WHEN status = 'SUCCESS' THEN 1 END) * 100.0) / COUNT(transaction_id), 
        2
    ) AS success_rate_pct,
    ROUND(AVG(latency_seconds), 1) AS avg_latency_sec
FROM 
    transactions
GROUP BY 
    corridor, payment_rail
ORDER BY 
    successful_volume_usd DESC;