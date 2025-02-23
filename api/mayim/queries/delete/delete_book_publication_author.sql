DELETE FROM book_publication_author
WHERE publication_id = $publication_id AND author_id = $author_id;
