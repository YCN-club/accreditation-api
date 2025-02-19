SELECT
    u.first_name || ' ' || u.last_name AS faculty_name,
    f.pan_no,
    f.apaar_id,
    f.highest_degree,
    f.university,
    f.area_of_specialization,
    f.date_of_join,
    f.designation_at_join,
    f.designation AS present_designation,
    f.designated_as_professor,
    f.designated_as_associate_professor,
    f.designated_as_assistant_professor,
    f.nature_of_association,
    f.contractual_obligation,
    f.currently_associated,
    f.date_of_leave
FROM
    faculty f
JOIN
    users u ON f.id = u.id
WHERE
    f.institute_id = $institute_id;

-- Variables to be passed: $institute_id
