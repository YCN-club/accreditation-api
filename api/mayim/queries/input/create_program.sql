INSERT INTO programs (
    id,
    program_code,
    duration_year,
    name,
    year_of_start,
    sanctioned_intake,
    aicte_approval_details,
    accreditation_status,
    number_of_times_accredited,
    institute_id
) VALUES (
    $id,
    $program_code,
    $duration_year,
    $name,
    $year_of_start,
    $sanctioned_intake,
    $aicte_approval_details,
    $accreditation_status,
    $number_of_times_accredited,
    $institute_id
);