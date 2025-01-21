SELECT 
    s.name AS student_name,
    e.name AS event_name,
    e.level,
    e.date,
    ce.award
FROM 
    students s
JOIN 
    competitive_events ce ON s.id = ce.participant_id
JOIN 
    events e ON ce.id = e.id;
