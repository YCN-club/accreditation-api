SELECT 
    jp.title AS publication_name,
    u.first_name || ' ' || u.last_name AS editor_name,
    s.first_name || ' ' || s.last_name AS student_name,
    g.semester,
    jp.journal_volume_number AS number_of_issues,
    jp.type AS publication_type
FROM 
    journal_publications jp
JOIN 
    journal_publication_authors jpa ON jp.id = jpa.publication_id
JOIN 
    users u ON jp.journal_id = u.id
JOIN 
    students s ON jpa.author_id = s.id
JOIN 
    gpa g ON s.id = g.student_id
WHERE 
    jp.year = $year
ORDER BY 
    jp.title, s.first_name, s.last_name;

-- Variables to be passed: $year
