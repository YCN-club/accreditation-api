SELECT 
    year,
    name AS program_name,
    no_of_participants AS participants_certified,
    no_of_days
FROM 
    continuing_education_programs
WHERE 
    institute_id = $institute_id;
