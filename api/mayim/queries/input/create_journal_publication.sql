INSERT INTO journal_publications (
    id,
    journal_id,
    journal_volume_number,
    journal_issue_number,
    sponsor_id,
    year,
    semester,
    doi,
    title
) VALUES (
    $id,
    $journal_id,
    $journal_volume_number,
    $journal_issue_number,
    $sponsor_id,
    $year,
    $semester,
    $doi,
    $title
);