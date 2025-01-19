SELECT 
    (SELECT COUNT(*) 
     FROM journal_publications jp
     JOIN journals j ON jp.journal_id = j.id
     JOIN departments d ON j.department_id = d.id
     WHERE d.id = $department_id) AS peer_reviewed_journal_papers,
    (SELECT COUNT(*) 
     FROM journal_publications jp
     JOIN journals j ON jp.journal_id = j.id
     JOIN departments d ON j.department_id = d.id
     WHERE d.id = $department_id
       AND jp.type = 'CONFERENCE') AS peer_reviewed_conference_papers,
    (SELECT COUNT(*) 
     FROM book_publications bp
     JOIN departments d ON bp.department_id = d.id
     WHERE d.id = $department_id) AS books_book_chapters_published,
    (SELECT SUM(jp.citations) 
     FROM journal_publications jp
     JOIN journals j ON jp.journal_id = j.id
     JOIN departments d ON j.department_id = d.id
     WHERE d.id = $department_id) AS citations,
    (SELECT COUNT(*) 
     FROM students s
     JOIN departments d ON s.department_id = d.id
     WHERE d.id = $department_id
       AND s.program_level = 'PhD') AS phd_students_registered,
    (SELECT COUNT(*) 
     FROM students s
     JOIN departments d ON s.department_id = d.id
     WHERE d.id = $department_id
       AND s.program_level = 'PhD'
       AND s.year_of_exit IS NOT NULL) AS phd_students_produced
FROM 
    departments d
WHERE 
    d.id = $department_id;

-- Variables to be passed: $department_id
