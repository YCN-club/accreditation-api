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
    (SELECT (N1::float / p.sanctioned_intake) AS ER
     FROM (
         SELECT 
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
                  AND s.type_of_join = 'LATERAL_ENTRY') AS N1
     ) AS subquery) AS ER_1,
    (SELECT (N1::float / p.sanctioned_intake) AS ER
     FROM (
         SELECT 
             (SELECT COUNT(*) 
              FROM students s 
              JOIN branches b ON s.branch_id = b.id
              JOIN departments d ON b.department_id = d.id
              WHERE d.program_id = p.id 
                AND s.year_of_join = $year - 1 
                AND s.type_of_join = 'REGULAR') 
             - (SELECT COUNT(*) 
                FROM students s 
                JOIN branches b ON s.branch_id = b.id
                JOIN departments d ON b.department_id = d.id
                WHERE d.program_id = p.id 
                  AND s.year_of_join = $year - 1 
                  AND s.type_of_exit = 'LEFT') 
             + (SELECT COUNT(*) 
                FROM students s 
                JOIN branches b ON s.branch_id = b.id
                JOIN departments d ON b.department_id = d.id
                WHERE d.program_id = p.id 
                  AND s.year_of_join = $year - 1 
                  AND s.type_of_join = 'LATERAL_ENTRY') AS N1
     ) AS subquery) AS ER_2,
    (SELECT (N1::float / p.sanctioned_intake) AS ER
     FROM (
         SELECT 
             (SELECT COUNT(*) 
              FROM students s 
              JOIN branches b ON s.branch_id = b.id
              JOIN departments d ON b.department_id = d.id
              WHERE d.program_id = p.id 
                AND s.year_of_join = $year - 2 
                AND s.type_of_join = 'REGULAR') 
             - (SELECT COUNT(*) 
                FROM students s 
                JOIN branches b ON s.branch_id = b.id
                JOIN departments d ON b.department_id = d.id
                WHERE d.program_id = p.id 
                  AND s.year_of_join = $year - 2 
                  AND s.type_of_exit = 'LEFT') 
             + (SELECT COUNT(*) 
                FROM students s 
                JOIN branches b ON s.branch_id = b.id
                JOIN departments d ON b.department_id = d.id
                WHERE d.program_id = p.id 
                  AND s.year_of_join = $year - 2 
                  AND s.type_of_join = 'LATERAL_ENTRY') AS N1
     ) AS subquery) AS ER_3,
    ((ER_1 + ER_2 + ER_3) / 3) AS average_ER
FROM 
    programs p
WHERE 
    p.id = $program_id;

-- Variables to be passed: $program_id, $year
