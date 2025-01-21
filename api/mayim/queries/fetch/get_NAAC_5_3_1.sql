SELECT 
    a.year,
    a.name AS award_name,
    a.team_or_individual,
    a.event_type,
    a.classification,
    s.name AS student_name,
    s.id AS student_id
FROM 
    awards a
JOIN 
    students s ON a.user_id = s.id
WHERE 
    a.type IN ('SPORTS', 'CULTURAL');
