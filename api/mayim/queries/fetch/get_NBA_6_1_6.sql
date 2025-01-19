SELECT 
    u.first_name || ' ' || u.last_name AS faculty_name,
    fsip.name_of_event AS event_name,
    fsip.link_of_website AS website_link
FROM 
    faculty_student_innovative_projects fsip
JOIN 
    faculty f ON fsip.faculty_id = f.id
JOIN 
    users u ON f.id = u.id
WHERE 
    f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
