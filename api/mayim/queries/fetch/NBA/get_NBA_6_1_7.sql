SELECT
    u.first_name || ' ' || u.last_name AS faculty_name,
    fitc.name_of_itc AS internship_training_collaboration,
    fitc.name_of_company AS company_place,
    fitc.outcomes AS outcomes
FROM
    faculty_internship_training_collaboration fitc
JOIN
    faculty f ON fitc.faculty_id = f.id
JOIN
    users u ON f.id = u.id
WHERE
    f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
