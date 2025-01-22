UPDATE auth
SET password = $password_hash,
    requires_reset = false
WHERE id = $user_id;
