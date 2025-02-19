SELECT
    bp.year,
    bp.type AS scheme_type,
    COUNT(bp.student_id) AS number_of_students_benefited
FROM
    benefit_programs bp
WHERE
    bp.year = $year
GROUP BY
    bp.year, bp.type;

-- Variables to be passed: $year
