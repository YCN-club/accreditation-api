SELECT 
    i.name AS institution_name,
    i.affiliating_university_name,
    i.affiliating_university_address,
    i.type AS institution_type,
    i.year_of_establishment,
    i.ownership_status,
    i.vision,
    i.mission,
    oai.name AS other_institution_name,
    oai.year_of_establishment AS other_institution_year_of_establishment,
    oai.program_of_study AS other_institution_programs_of_study,
    oai.location AS other_institution_location,
    p.name AS program_name,
    p.year_of_start,
    p.sanctioned_intake,
    p.aicte_approval_details,
    p.accreditation_status,
    p.number_of_times_accredited,
    d.name AS department_name,
    f.id AS faculty_id,
    f.designation,
    f.date_of_join,
    f.currently_associated,
    s.id AS student_id,
    s.batch_year,
    s.year_of_join,
    s.year_of_exit,
    s.type_of_exit,
    s.branch_id,
    h.first_name || ' ' || h.last_name AS head_of_institution_name,
    h.designation AS head_of_institution_designation,
    h.email AS head_of_institution_email,
    h.mobile_number AS head_of_institution_mobile,
    n.first_name || ' ' || n.last_name AS nba_coordinator_name,
    n.designation AS nba_coordinator_designation,
    n.email AS nba_coordinator_email,
    n.mobile_number AS nba_coordinator_mobile
FROM 
    institutes i
LEFT JOIN 
    other_academic_institutes_run_by_trust_society oai ON oai.id = ANY(i.other_academic_institute_ids)
LEFT JOIN 
    programs p ON p.institute_id = i.id
LEFT JOIN 
    departments d ON d.program_id = p.id
LEFT JOIN 
    faculty f ON f.department_id = d.id
LEFT JOIN 
    students s ON s.branch_id = d.id
LEFT JOIN 
    faculty h ON h.id = i.head_of_institute_id
LEFT JOIN 
    faculty n ON n.id = i.nba_coordinator_id
WHERE 
    i.id = $institute_id;
