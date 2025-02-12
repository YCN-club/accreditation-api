SELECT
    u.first_name || ' ' || u.last_name AS teacher_name,
    a.name AS award_fellowship,
    a.year AS year_of_award,
    a.awarding_agency
FROM
    awards a
JOIN
    users u ON a.user_id = u.id
WHERE
    a.type = 'FELLOWSHIP'
    AND a.year = $year;

-- Variables to be passed: $year
