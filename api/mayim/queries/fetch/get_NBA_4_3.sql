WITH AP1 AS (
    SELECT 
        AVG(g.gpa) AS X,
        COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) AS Y,
        COUNT(*) AS Z,
        (AVG(g.gpa) * (COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) / COUNT(*))) AS AP1
    FROM 
        gpa g
    JOIN 
        students s ON g.student_id = s.id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND g.semester IN (5, 6) -- Assuming 3rd year includes 5th and 6th semesters
        AND s.year_of_join = $year - 2
    GROUP BY 
        p.id
),
AP2 AS (
    SELECT 
        AVG(g.gpa) AS X,
        COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) AS Y,
        COUNT(*) AS Z,
        (AVG(g.gpa) * (COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) / COUNT(*))) AS AP2
    FROM 
        gpa g
    JOIN 
        students s ON g.student_id = s.id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND g.semester IN (5, 6) -- Assuming 3rd year includes 5th and 6th semesters
        AND s.year_of_join = $year - 3
    GROUP BY 
        p.id
),
AP3 AS (
    SELECT 
        AVG(g.gpa) AS X,
        COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) AS Y,
        COUNT(*) AS Z,
        (AVG(g.gpa) * (COUNT(CASE WHEN g.gpa >= 5 THEN 1 END) / COUNT(*))) AS AP3
    FROM 
        gpa g
    JOIN 
        students s ON g.student_id = s.id
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
        AND g.semester IN (5, 6) -- Assuming 3rd year includes 5th and 6th semesters
        AND s.year_of_join = $year - 4
    GROUP BY 
        p.id
)
SELECT 
    AP1.X AS X1, AP1.Y AS Y1, AP1.Z AS Z1, AP1.AP1,
    AP2.X AS X2, AP2.Y AS Y2, AP2.Z AS Z2, AP2.AP2,
    AP3.X AS X3, AP3.Y AS Y3, AP3.Z AS Z3, AP3.AP3,
    ((AP1.AP1 + AP2.AP2 + AP3.AP3) / 3) AS API
FROM 
    AP1, AP2, AP3;

-- Variables to be passed: $program_id, $year
