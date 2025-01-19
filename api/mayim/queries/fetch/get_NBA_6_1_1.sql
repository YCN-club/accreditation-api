SELECT 
    u.first_name || ' ' || u.last_name AS faculty_name,
    pc.name_of_society AS professional_society,
    pc.position AS grade_level_position
FROM 
    professional_communities pc
JOIN 
    faculty f ON pc.faculty_id = f.id
JOIN 
    users u ON f.id = u.id
WHERE 
    f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
