SELECT
    a.name AS award_name,
    u.first_name || ' ' || u.last_name AS recipient_name,
    CASE
        WHEN a.user_type = 'FACULTY' THEN 'Faculty'
        WHEN a.user_type = 'STUDENT' THEN 'Student'
        ELSE 'Research Scholar'
    END AS designation,
    a.awarding_agency,
    a.year AS year_of_award
FROM
    awards a
JOIN
    users u ON a.user_id = u.id
WHERE
    a.type = 'INNOVATION_DISCOVERY'
    AND a.year = $year;

-- Variables to be passed: $year
