SELECT
    p.sanctioned_intake AS N,
    (SELECT COUNT(*)
     FROM students s
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = p.id
       AND s.year_of_join = $year
       AND s.type_of_join = 'REGULAR')
    - (SELECT COUNT(*)
       FROM students s
       JOIN branches b ON s.branch_id = b.id
       JOIN departments d ON b.department_id = d.id
       WHERE d.program_id = p.id
         AND s.year_of_join = $year
         AND s.type_of_exit = 'LEFT')
    + (SELECT COUNT(*)
       FROM students s
       JOIN branches b ON s.branch_id = b.id
       JOIN departments d ON b.department_id = d.id
       WHERE d.program_id = p.id
         AND s.year_of_join = $year
         AND s.type_of_join = 'LATERAL_ENTRY') AS N1,
    (SELECT COUNT(*)
     FROM students s
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = p.id
       AND s.year_of_join = $year
       AND s.type_of_join = 'LATERAL_ENTRY') AS N2,
    (SELECT COUNT(*)
     FROM students s
     JOIN branches b ON s.branch_id = b.id
     JOIN departments d ON b.department_id = d.id
     WHERE d.program_id = p.id
       AND s.year_of_join = $year
       AND s.type_of_join = 'OTHER') AS N3,
    ((SELECT COUNT(*)
      FROM students s
      JOIN branches b ON s.branch_id = b.id
      JOIN departments d ON b.department_id = d.id
      WHERE d.program_id = p.id
        AND s.year_of_join = $year
        AND s.type_of_join = 'REGULAR')
     - (SELECT COUNT(*)
        FROM students s
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id
          AND s.year_of_join = $year
          AND s.type_of_exit = 'LEFT')
     + (SELECT COUNT(*)
        FROM students s
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id
          AND s.year_of_join = $year
          AND s.type_of_join = 'LATERAL_ENTRY')
     + (SELECT COUNT(*)
        FROM students s
        JOIN branches b ON s.branch_id = b.id
        JOIN departments d ON b.department_id = d.id
        WHERE d.program_id = p.id
          AND s.year_of_join = $year
          AND s.type_of_join = 'OTHER')) AS total_admitted
FROM
    programs p
WHERE
    p.id = $program_id;

-- Variables to be passed: $program_id, $year
