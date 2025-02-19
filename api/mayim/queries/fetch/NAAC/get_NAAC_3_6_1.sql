SELECT
    e.date,
    e.name AS activity_name,
    o.name AS organizing_unit,
    e.no_of_students AS students_participated,
    e.no_of_teachers AS teachers_participated,
    e.link_to_report
FROM
    events e
JOIN
    organizers o ON e.organizer_id = o.id
WHERE
    e.date BETWEEN DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 year' + INTERVAL '1 month' AND DATE_TRUNC('year', CURRENT_DATE) + INTERVAL '5 months';
