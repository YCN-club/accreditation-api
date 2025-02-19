SELECT
    (SELECT COUNT(*)
     FROM students s
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = $program_id
       AND s.year_of_join = $year
       AND s.type_of_join IN ('LATERAL_ENTRY', 'OTHER')) AS N4,
    (SELECT COUNT(*)
     FROM students s
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = $program_id
       AND s.year_of_exit = $year
       AND s.type_of_exit IN ('LEFT', 'OTHER')) AS N5,
    ((SELECT COUNT(*)
      FROM students s
      JOIN branches b ON s.branch_id = b.id
      JOIN departments d ON b.department_id = d.id
      WHERE d.program_id = $program_id
        AND s.year_of_join = $year
        AND s.type_of_join IN ('LATERAL_ENTRY', 'OTHER'))
     - (SELECT COUNT(*)
        FROM students s
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = $program_id
          AND s.year_of_exit = $year
          AND s.type_of_exit IN ('LEFT', 'OTHER'))) AS total_admitted
FROM
    programs p
WHERE
    p.id = $program_id;

-- Variables to be passed: $program_id, $year
