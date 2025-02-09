SELECT
    e.year,
    e.name AS event_name,
    ce.position,
    ce.type AS event_type
FROM
    competitive_events ce
JOIN
    events e ON ce.id = e.id
WHERE
    e.date >= NOW() - INTERVAL '3 years'
ORDER BY
    e.date DESC;
