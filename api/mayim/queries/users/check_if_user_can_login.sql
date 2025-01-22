SELECT EXISTS (
        SELECT 1
        FROM auth NATURAL
            JOIN users
        WHERE email = $email_id
    );
