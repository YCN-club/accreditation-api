SELECT 
    o.name AS body_name,
    e.name AS event_name,
    e.level,
    e.date
FROM 
    events e
JOIN 
    organizers o ON e.organizer_id = o.id;
