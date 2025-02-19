SELECT
    s.year_of_join AS year_of_entry,
    COUNT(*) AS total_students,
    SUM(CASE WHEN s.year_of_exit IS NOT NULL AND s.year_of_exit - s.year_of_join <= p.duration_year THEN 1 ELSE 0 END) AS graduated_within_stipulated_period,
    SUM(CASE WHEN s.year_of_exit IS NOT NULL AND s.year_of_exit - s.year_of_join <= p.duration_year AND s.backlogs = 0 THEN 1 ELSE 0 END) AS graduated_without_backlogs,
    SUM(CASE WHEN s.year_of_exit IS NOT NULL AND s.year_of_join <= p.duration_year AND s.backlogs > 0 THEN 1 ELSE 0 END) AS graduated_with_backlogs
FROM
    students s
JOIN
    branches b ON s.branch_id = b.id
JOIN
    departments d ON b.department_id = d.id
JOIN
    programs p ON d.program_id = p.id
WHERE
    p.id = $program_id
GROUP BY
    s.year_of_join
ORDER BY
    s.year_of_join;

-- Variables to be passed: $program_id
