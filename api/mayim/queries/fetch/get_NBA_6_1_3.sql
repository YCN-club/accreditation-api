SELECT 
    u.first_name || ' ' || u.last_name AS faculty_name,
    fc.name_of_course AS course_name
FROM 
    faculty_courses fc
JOIN 
    faculty f ON fc.faculty_id = f.id
JOIN 
    users u ON f.id = u.id
WHERE 
    fc.developed = true
    AND f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
