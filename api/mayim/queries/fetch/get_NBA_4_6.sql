WITH P1 AS (
    SELECT 
        COUNT(*) AS F,
        SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) AS X,
        SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) AS Y,
        SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END) AS Z,
        ((SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END)) / COUNT(*)) * 100 AS P1
    FROM 
        students s
    JOIN 
        after_graduation ag ON s.id = ag.student_id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND s.year_of_join = $year - 3
    GROUP BY 
        p.id
),
P2 AS (
    SELECT 
        COUNT(*) AS F,
        SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) AS X,
        SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) AS Y,
        SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END) AS Z,
        ((SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END)) / COUNT(*)) * 100 AS P2
    FROM 
        students s
    JOIN 
        after_graduation ag ON s.id = ag.student_id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND s.year_of_join = $year - 4
    GROUP BY 
        p.id
),
P3 AS (
    SELECT 
        COUNT(*) AS F,
        SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) AS X,
        SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) AS Y,
        SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END) AS Z,
        ((SUM(CASE WHEN ag.type = 'PLACEMENT' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'HIGHER_STUDIES' THEN 1 ELSE 0 END) + 
          SUM(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 ELSE 0 END)) / COUNT(*)) * 100 AS P3
    FROM 
        students s
    JOIN 
        after_graduation ag ON s.id = ag.student_id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND s.year_of_join = $year - 5
    GROUP BY 
        p.id
)
SELECT 
    P1.F AS F1, P1.X AS X1, P1.Y AS Y1, P1.Z AS Z1, P1.P1,
    P2.F AS F2, P2.X AS X2, P2.Y AS Y2, P2.Z AS Z2, P2.P2,
    P3.F AS F3, P3.X AS X3, P3.Y AS Y3, P3.Z AS Z3, P3.P3,
    ((P1.P1 + P2.P2 + P3.P3) / 3) AS average_placement_index
FROM 
    P1, P2, P3;

-- Variables to be passed: $program_id, $year
