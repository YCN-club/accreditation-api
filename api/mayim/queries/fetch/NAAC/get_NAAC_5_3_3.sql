SELECT
    e.year,
    e.date AS event_date,
    e.name AS activity_name,
    e.level
FROM
    events e
WHERE
    e.date >= NOW() - INTERVAL '5 years'
AND
    e.type IN ('SPORTS', 'CULTURAL')
ORDER BY
    e.date DESC;
