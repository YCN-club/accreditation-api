SELECT 
    ag.year,
    STRING_AGG(u.first_name || ' ' || u.last_name, ', ') AS student_names,
    COUNT(ag.student_id) AS total_students,
    c.name AS employer_name,
    c.contact_no AS employer_contact_no,
    c.contact_email AS employer_contact_email,
    p.name AS program_graduated_from
FROM 
    after_graduation ag
JOIN 
    students s ON ag.student_id = s.id
JOIN 
    users u ON s.id = u.id
JOIN 
    after_graduation_placements agp ON ag.id = agp.after_graduation_id
JOIN 
    companies c ON agp.employer_id = c.id
JOIN 
    branches b ON s.branch_id = b.id
JOIN 
    departments d ON b.department_id = d.id
JOIN 
    programs p ON d.program_id = p.id
WHERE 
    ag.year = $year
GROUP BY 
    ag.year, c.name, c.contact_no, c.contact_email, p.name;

-- Variables to be passed: $year
