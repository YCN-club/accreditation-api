SELECT
    nge.year,
    nge.exam_type,
    COUNT(nge.student_id) AS total_students,
    STRING_AGG(u.first_name || ' ' || u.last_name, ', ') AS names
FROM
    national_government_exams nge
JOIN
    students s ON nge.student_id = s.id
JOIN
    users u ON s.id = u.id
WHERE
    nge.year = $year
GROUP BY
    nge.year, nge.exam_type
ORDER BY
    nge.exam_type;

-- Variables to be passed: $year
