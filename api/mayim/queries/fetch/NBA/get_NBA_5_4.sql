SELECT
    u.first_name || ' ' || u.last_name AS person_name,
    fc.name_of_course AS course_name,
    f.designation || ', ' || f.university AS designation_organization,
    af.hours_handled
FROM
    adjunct_faculty af
JOIN
    faculty f ON af.faculty_id = f.id
JOIN
    users u ON f.id = u.id
JOIN
    faculty_courses fc ON f.id = fc.faculty_id
WHERE
    f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
