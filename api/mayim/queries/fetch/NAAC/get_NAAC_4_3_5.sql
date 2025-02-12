SELECT
    f.name AS teacher_name,
    e.name AS module_name,
    e.development_platform AS platform,
    e.date_of_launch AS launch_date,
    e.link_to_relevant_document AS document_link,
    e.institute
FROM
    e_resources e
JOIN
    faculty f ON e.faculty_id = f.id;
