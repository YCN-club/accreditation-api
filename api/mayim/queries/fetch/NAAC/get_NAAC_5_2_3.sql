SELECT
    ag.year,
    STRING_AGG(u.first_name || ' ' || u.last_name, ', ') AS student_names,
    p.name AS program_graduated_from,
    d.name AS department_graduated_from,
    aghs.institute_name,
    aghs.program_name AS program_admitted_to
FROM
    after_graduation ag
JOIN
    students s ON ag.student_id = s.id
JOIN
    users u ON s.id = u.id
JOIN
    after_graduation_higher_studies aghs ON ag.id = aghs.after_graduation_id
JOIN
    branches b ON s.branch_id = b.id
JOIN
    departments d ON b.department_id = d.id
JOIN
    programs p ON d.program_id = p.id
WHERE
    ag.year = $year
GROUP BY
    ag.year, p.name, d.name, aghs.institute_name, aghs.program_name;

-- Variables to be passed: $year
