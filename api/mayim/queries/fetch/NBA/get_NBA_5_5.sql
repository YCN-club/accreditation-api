SELECT
    COUNT(CASE WHEN f.date_of_join >= NOW() - INTERVAL '1 year' THEN 1 END) AS A,
    COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '1 year' AND f.date_of_join >= NOW() - INTERVAL '2 years' THEN 1 END) AS B,
    COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '2 years' AND f.date_of_join >= NOW() - INTERVAL '4 years' THEN 1 END) AS C,
    COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '4 years' AND f.date_of_join >= NOW() - INTERVAL '6 years' THEN 1 END) AS D,
    COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '6 years' THEN 1 END) AS E,
    COUNT(*) AS AF,
    CEIL(COUNT(*) / 20.0) AS RF,
    LEAST((((COUNT(CASE WHEN f.date_of_join >= NOW() - INTERVAL '1 year' THEN 1 END) * 0) +
            (COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '1 year' AND f.date_of_join >= NOW() - INTERVAL '2 years' THEN 1 END) * 1) +
            (COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '2 years' AND f.date_of_join >= NOW() - INTERVAL '4 years' THEN 1 END) * 2) +
            (COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '4 years' AND f.date_of_join >= NOW() - INTERVAL '6 years' THEN 1 END) * 3) +
            (COUNT(CASE WHEN f.date_of_join < NOW() - INTERVAL '6 years' THEN 1 END) * 4)) /
            CEIL(COUNT(*) / 20.0)) * 2.5, 10) AS FR
FROM
    faculty f
JOIN
    departments d ON f.department_id = d.id
JOIN
    programs p ON d.program_id = p.id
WHERE
    p.id = $program_id;

-- Variables to be passed: $program_id
