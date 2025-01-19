WITH FacultyRequired AS (
    SELECT 
        CEIL(COUNT(*) / 20.0) AS total_faculty_required
    FROM 
        students s
    JOIN 
        branches b ON s.branch_id = b.id
    JOIN 
        departments d ON b.department_id = d.id
    JOIN 
        programs p ON d.program_id = p.id
    WHERE 
        p.id = $program_id
)
SELECT 
    total_faculty_required,
    CEIL(total_faculty_required * (1.0 / 9.0)) AS F1, -- Professors
    CEIL(total_faculty_required * (2.0 / 9.0)) AS F2, -- Associate Professors
    CEIL(total_faculty_required * (6.0 / 9.0)) AS F3, -- Assistant Professors
    CONCAT(CEIL(total_faculty_required * (1.0 / 9.0)), ':', 
           CEIL(total_faculty_required * (2.0 / 9.0)), ':', 
           CEIL(total_faculty_required * (6.0 / 9.0))) AS proportion
FROM 
    FacultyRequired;

-- Variables to be passed: $program_id
