SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    g.semester AS semester,
    u.first_name || ' ' || u.last_name AS publisher_name,
    jp.title AS journal_conference_name,
    jp.journal_volume_number AS volume_number,
    jp.journal_issue_number AS issue_number,
    a.name AS award_name
FROM
    journal_publications jp
JOIN
    journal_publication_authors jpa ON jp.id = jpa.publication_id
JOIN
    users u ON jp.journal_id = u.id
JOIN
    students s ON jpa.author_id = s.id
JOIN
    gpa g ON s.id = g.student_id
LEFT JOIN
    awards a ON s.id = a.user_id
WHERE
    jp.year = $year
ORDER BY
    s.first_name, s.last_name, jp.title;

-- Variables to be passed: $year
