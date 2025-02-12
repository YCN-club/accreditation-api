SELECT
    bp.year,
    bp.type AS scheme_name,
    COUNT(bp.student_id) AS number_of_students_benefited
FROM
    benefit_programs bp
WHERE
    bp.year = $year
    AND bp.type = 'COMPETITIVE_EXAM_GUIDANCE'
GROUP BY
    bp.year, bp.type;

-- Variables to be passed: $year
