SELECT
    COUNT(CASE WHEN f.highest_degree = 'DOCTORAL' THEN 1 END) AS X,
    COUNT(CASE WHEN f.highest_degree = 'MASTERS' THEN 1 END) AS Y,
    COUNT(*) AS F,
    2.5 * ((10 * COUNT(CASE WHEN f.highest_degree = 'DOCTORAL' THEN 1 END) +
            4 * COUNT(CASE WHEN f.highest_degree = 'MASTERS' THEN 1 END)) /
            COUNT(*)) AS FQI
FROM
    faculty f
JOIN
    departments d ON f.department_id = d.id
JOIN
    programs p ON d.program_id = p.id
WHERE
    p.id = $program_id;

-- Variables to be passed: $program_id
