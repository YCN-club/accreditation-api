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
    f.employee_id,
    a.password,
    a.is_active,
    a.requires_reset
FROM faculty f
    JOIN users u ON f.id = u.id
    JOIN auth a ON u.id = a.id
WHERE f.employee_id = $employee_id;
