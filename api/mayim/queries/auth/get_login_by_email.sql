SELECT u.id AS user_id,
    CONCAT(
        u.first_name,
        CASE
            WHEN u.middle_name IS NOT NULL THEN CONCAT(' ', u.middle_name)
            ELSE ''
        END,
        ' ',
        u.last_name
    ) AS name,
    u.email,
    a.password,
    a.is_active,
    a.requires_reset
FROM users u
    JOIN auth a ON u.id = a.id
WHERE u.email = $email;
