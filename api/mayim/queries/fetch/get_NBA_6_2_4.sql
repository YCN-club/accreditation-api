SELECT 
    fpi.first_name || ' ' || fpi.last_name AS principal_investigator_name,
    fcpi.first_name || ' ' || fcpi.last_name AS co_principal_investigator_name,
    d.name AS department_name,
    srp.project_title,
    srp.name_of_funding_agency,
    srp.duration_of_project,
    srp.amount_inr / 100000 AS amount_in_lacs
FROM 
    faculty_sponsored_research_projects_consultancy_work_institute_seed_money srp
JOIN 
    faculty fpi ON srp.name_of_principal_investigator = fpi.id
LEFT JOIN 
    faculty fcpi ON srp.name_of_co_principal_investigator = fcpi.id
JOIN 
    departments d ON srp.department_id = d.id
WHERE 
    srp.type = 'CONSULTANCY_WORK'
    AND srp.year = $year;

-- Variables to be passed: $year
