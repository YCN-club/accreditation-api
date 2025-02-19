SELECT
    ca.title AS activity_title,
    a.name AS collaborating_agency,
    a.contact_no AS agency_contact_no,
    a.contact_email AS agency_contact_email,
    u.first_name || ' ' || u.last_name AS participant_name,
    ca.source_of_financial_support,
    ca.year AS year_of_collaboration,
    ca.duration,
    ca.type AS nature_of_activity,
    ca.link_to_relevant_documents
FROM
    collaborative_activities ca
JOIN
    agencies a ON ca.agency_id = a.id
JOIN
    users u ON ca.user_id = u.id
WHERE
    ca.year = $year;

-- Variables to be passed: $year
