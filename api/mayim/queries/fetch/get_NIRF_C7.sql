SELECT 
    s.year_of_join AS year,
    p.name AS program_name,
    p.level AS program_level,
    p.sanctioned_intake AS approved_intake,
    COUNT(s.id) AS actual_intake,
    COUNT(CASE WHEN s.year_of_join = $year AND s.origin = 'IN_STATE' THEN 1 END) AS in_state_first_year,
    COUNT(CASE WHEN s.year_of_join = $year AND s.origin = 'OUT_OF_STATE' THEN 1 END) AS out_of_state_first_year,
    COUNT(CASE WHEN s.year_of_join = $year AND s.origin = 'INTERNATIONAL' THEN 1 END) AS international_first_year,
    COUNT(CASE WHEN s.year_of_join = $year - 1 AND s.type_of_join = 'LATERAL_ENTRY' AND s.origin = 'IN_STATE' THEN 1 END) AS in_state_lateral_entry,
    COUNT(CASE WHEN s.year_of_join = $year - 1 AND s.type_of_join = 'LATERAL_ENTRY' AND s.origin = 'OUT_OF_STATE' THEN 1 END) AS out_of_state_lateral_entry,
    COUNT(CASE WHEN s.year_of_join = $year - 1 AND s.type_of_join = 'LATERAL_ENTRY' AND s.origin = 'INTERNATIONAL' THEN 1 END) AS international_lateral_entry,
    COUNT(CASE WHEN s.gender = 'MALE' THEN 1 END) AS total_male_students,
    COUNT(CASE WHEN s.gender = 'FEMALE' THEN 1 END) AS total_female_students,
    COUNT(s.id) AS total_students,
    COUNT(CASE WHEN s.economic_disadvantage = true THEN 1 END) AS economically_backward_students,
    COUNT(CASE WHEN s.social_disadvantage = 'SC' THEN 1 END) AS sc_students,
    COUNT(CASE WHEN s.social_disadvantage = 'ST' THEN 1 END) AS st_students,
    COUNT(CASE WHEN s.social_disadvantage = 'OBC' THEN 1 END) AS obc_students,
    COUNT(CASE WHEN s.physically_challenged = true THEN 1 END) AS physically_challenged_students,
    COUNT(CASE WHEN s.year_of_exit - s.year_of_join <= p.duration_year THEN 1 END) AS students_graduating_in_min_time,
    COUNT(CASE WHEN nge.exam_type = 'UPSC' THEN 1 END) AS upsc_students,
    COUNT(CASE WHEN nge.exam_type = 'STATE_GOVERNMENT_EXAMS' THEN 1 END) AS state_gov_students,
    COUNT(CASE WHEN nge.exam_type = 'GATE' THEN 1 END) AS gate_students,
    COUNT(CASE WHEN nge.exam_type = 'CAT' THEN 1 END) AS cat_students,
    COUNT(CASE WHEN nge.exam_type = 'OTHERS' THEN 1 END) AS other_exam_students,
    COUNT(CASE WHEN ag.type = 'PLACEMENT' THEN 1 END) AS placed_students,
    MIN(agp.salary) AS min_salary,
    MAX(agp.salary) AS max_salary,
    AVG(agp.salary) AS avg_salary,
    COUNT(CASE WHEN aghs.with_exam = true THEN 1 END) AS higher_studies_with_exam,
    COUNT(CASE WHEN aghs.with_exam = false THEN 1 END) AS higher_studies_without_exam,
    COUNT(CASE WHEN ag.type = 'ENTREPRENEURSHIP' THEN 1 END) AS entrepreneurship_students
FROM 
    students s
JOIN 
    branches b ON s.branch_id = b.id
JOIN 
    departments d ON b.department_id = d.id
JOIN 
    programs p ON d.program_id = p.id
LEFT JOIN 
    national_government_exams nge ON s.id = nge.student_id
LEFT JOIN 
    after_graduation ag ON s.id = ag.student_id
LEFT JOIN 
    after_graduation_placements agp ON ag.id = agp.after_graduation_id
LEFT JOIN 
    after_graduation_higher_studies aghs ON ag.id = aghs.after_graduation_id
WHERE 
    s.year_of_join IN ($year - 2, $year - 3, $year - 4)
GROUP BY 
    s.year_of_join, p.name, p.level, p.sanctioned_intake;

-- Variables to be passed: $year
