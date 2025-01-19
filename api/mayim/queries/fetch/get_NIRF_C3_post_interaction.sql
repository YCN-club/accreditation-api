-- Post Interaction
SELECT 
    i.year,
    COUNT(CASE WHEN i.type = 'PATENT' AND i.status = 'FILED' THEN 1 END) AS patents_filed,
    COUNT(CASE WHEN i.type = 'PATENT' AND i.status = 'GRANTED' THEN 1 END) AS patents_granted,
    COUNT(CASE WHEN i.type = 'PATENT' AND i.status = 'LICENSED' THEN 1 END) AS patents_licensed,
    COUNT(CASE WHEN i.type = 'PATENT' AND i.status = 'COLLABORATIVE' THEN 1 END) AS collaborative_patents,
    COUNT(CASE WHEN i.type = 'DESIGN' AND i.status = 'FILED' THEN 1 END) AS designs_filed,
    COUNT(CASE WHEN i.type = 'DESIGN' AND i.status = 'GRANTED' THEN 1 END) AS designs_granted
FROM 
    ipr i
WHERE 
    i.year IN ($year - 2, $year - 3, $year - 4)
GROUP BY 
    i.year;

SELECT 
    ie.financial_year AS year,
    SUM(ie.amount_inr) / 100000 AS amount_in_lakh_inr
FROM 
    ipr_earnings ie
WHERE 
    ie.financial_year IN ($year - 2, $year - 3, $year - 4)
GROUP BY 
    ie.financial_year;

-- Variables to be passed: $year