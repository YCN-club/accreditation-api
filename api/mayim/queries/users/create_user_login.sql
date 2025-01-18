INSERT INTO auth (id, password, requires_reset, is_active)
VALUES ($user_id, $password_hash, true, true)
