INSERT INTO ipr (
    id,
    awardee_id,
    awarder_name,
    government_recognized,
    year,
    uuid,
    title,
    type,
    status
) VALUES (
    $id,
    $awardee_id,
    $awarder_name,
    $government_recognized,
    $year,
    $uuid,
    $title,
    $type,
    $status
);