SELECT 
    a.name AS award_name,
    a.awarding_agency AS awarding_body
FROM 
    awards a
WHERE 
    a.type = 'EXTENSION_OUTREACH'
    AND a.year BETWEEN '2023-07-01' AND '2024-06-30';

-- Variables to be passed: None
