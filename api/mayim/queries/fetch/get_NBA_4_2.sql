SELECT 
    (SELECT COUNT(*)  
     FROM students s 
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = p.id 
       AND s.year_of_join = $year 
       AND s.type_of_join IN ('REGULAR', 'LATERAL_ENTRY', 'OTHER')) AS A,
    (SELECT COUNT(*) 
     FROM students s 
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = p.id 
       AND s.year_of_join = $year 
       AND s.year_of_exit - s.year_of_join <= p.duration_year) AS B,
    ((SELECT COUNT(*) 
      FROM students s 
      JOIN branches b ON s.branch_id = b.id
      JOIN departments d ON b.department_id = d.id
      WHERE d.program_id = p.id 
        AND s.year_of_join = $year 
        AND s.year_of_exit - s.year_of_join <= p.duration_year) 
     / (SELECT COUNT(*) 
        FROM students s 
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id 
          AND s.year_of_join = $year 
          AND s.type_of_join IN ('REGULAR', 'LATERAL_ENTRY', 'OTHER'))) * 100 AS SR_1,
    ((SELECT COUNT(*) 
      FROM students s 
      JOIN branches b ON s.branch_id = b.id
      JOIN departments d ON b.department_id = d.id
      WHERE d.program_id = p.id 
        AND s.year_of_join = $year - 1 
        AND s.year_of_exit - s.year_of_join <= p.duration_year) 
     / (SELECT COUNT(*) 
        FROM students s 
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id 
          AND s.year_of_join = $year - 1 
          AND s.type_of_join IN ('REGULAR', 'LATERAL_ENTRY', 'OTHER'))) * 100 AS SR_2,
    ((SELECT COUNT(*) 
      FROM students s 
      JOIN branches b ON s.branch_id = b.id
      JOIN departments d ON b.department_id = d.id
      WHERE d.program_id = p.id 
        AND s.year_of_join = $year - 2 
        AND s.year_of_exit - s.year_of_join <= p.duration_year) 
     / (SELECT COUNT(*) 
        FROM students s 
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id 
          AND s.year_of_join = $year - 2 
          AND s.type_of_join IN ('REGULAR', 'LATERAL_ENTRY', 'OTHER'))) * 100 AS SR_3,
    ((SR_1 + SR_2 + SR_3) / 3) AS average_SR
FROM 
    programs p
WHERE 
    p.id = $program_id;

# Variables to be passed: $program_id, $year
