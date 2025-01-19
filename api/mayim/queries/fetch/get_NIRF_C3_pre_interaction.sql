-- Pre Interaction
SELECT 
    CASE 
        WHEN jp.type = 'HARDCOPY' THEN 'Article'
        WHEN jp.type = 'SOFTCOPY' THEN 'Book'
        ELSE 'Book Chapter'
    END AS publication_type,
    STRING_AGG(u.last_name || ', ' || u.first_name || ' ' || u.middle_name, '; ') AS authors,
    jp.title AS full_title,
    jp.year AS year_of_publication
FROM 
    journal_publications jp
JOIN 
    journal_publication_authors jpa ON jp.id = jpa.publication_id
JOIN 
    users u ON jpa.author_id = u.id
WHERE 
    jp.year = $year
GROUP BY 
    jp.type, jp.title, jp.year;

-- Variables to be passed: $year
