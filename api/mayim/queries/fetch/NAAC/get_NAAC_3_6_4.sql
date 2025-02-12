SELECT
    e.name AS activity_name,
    o.name AS organizing_unit,
    e.scheme_name,
    e.year,
    e.date,
    e.location,
    e.link_to_report
FROM
    events e
JOIN
    organizers o ON e.organizer_id = o.id
WHERE
    e.type = 'SOCIAL_RESPONSIBILITY';
