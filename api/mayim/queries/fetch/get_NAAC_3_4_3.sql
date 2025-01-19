SELECT 
    u.first_name || ' ' || u.last_name AS awardee_name,
    i.uuid AS patent_copyright_number,
    i.title AS patent_copyright_title,
    i.year AS year_awarded
FROM 
    ipr i
JOIN 
    users u ON i.awardee_id = u.id
WHERE 
    i.type IN ('PATENT', 'COPYRIGHT')
    AND i.year = $year;

-- Variables to be passed: $year