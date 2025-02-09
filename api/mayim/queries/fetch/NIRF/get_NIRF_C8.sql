SELECT
  e.year,
  e.name AS event_name,
  ce.position,
  e.level AS event_level,
  CASE
    WHEN ce.classification = 'TEAM' THEN (
      SELECT
        u.first_name || ' ' || u.last_name
      FROM
        users u
        JOIN students s ON u.id = s.id
      WHERE
        s.id = ce.participant_id
      LIMIT
        1
    )
    ELSE (
      SELECT
        u.first_name || ' ' || u.last_name
      FROM
        users u
      WHERE
        u.id = ce.participant_id
    )
  END AS participant_name
FROM
  competitive_events ce
  JOIN events e ON ce.id = e.id
  JOIN users u ON ce.participant_id = u.id
WHERE
  e.year IN ($ year - 2, $ year - 3, $ year - 4)
ORDER BY
  e.year,
  e.level,
  ce.position;

-- Variables to be passed: $year
