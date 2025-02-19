SELECT
    srp.year AS financial_year,
    srp.project_title AS title_of_project,
    srp.name_of_funding_agency AS funding_agency,
    srp.amount_inr / 100000 AS amount_in_lakh_inr
FROM
    faculty_sponsored_research_projects_consultancy_work_institute_seed_money srp
WHERE
    srp.year = $year;

-- Variables to be passed: $year
