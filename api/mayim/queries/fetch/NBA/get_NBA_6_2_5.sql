SELECT
    fpi.first_name || ' ' || fpi.last_name AS principal_investigator_name,
    srp.project_title,
    srp.duration_of_project,
    srp.amount_inr / 100000 AS amount_in_lacs,
    srp.outcomes
FROM
    faculty_sponsored_research_projects_consultancy_work_institute_seed_money srp
JOIN
    faculty fpi ON srp.name_of_principal_investigator = fpi.id
WHERE
    srp.type = 'INSTITUTE_SEED_MONEY'
    AND srp.year = $year;

-- Variables to be passed: $year
