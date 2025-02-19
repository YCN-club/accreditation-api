SELECT
    d.name AS department_name,
    e.name AS event_name,
    o.name AS organizer_name,
    co.name AS co_organizer_name,
    e.start_time,
    e.end_time,
    e.number_of_attendees,
    e.venue,
    e.description,
    e.speaker_details,
    e.attendance_doc,
    e.feedback_doc,
    e.brochure_doc,
    e.sdg_goal,
    e.photos_docs,
    e.event_report_doc
FROM
    events e
JOIN
    departments d ON e.department_id = d.id
JOIN
    organizers o ON e.organizer_id = o.id
LEFT JOIN
    organizers co ON e.co_organizer_id = co.id;
