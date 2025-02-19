SELECT
    u.id AS user_id,
    u.first_name || ' ' || u.last_name AS name,
    u.email,
    a.password,
    a.is_active,
    a.requires_reset
FROM
    users u
JOIN
    auth a ON u.id = a.id;
