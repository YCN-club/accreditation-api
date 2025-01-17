INSERT INTO collaborative_activities (
    id,
    title,
    type,
    agency_id,
    user_id,
    source_of_financial_support,
    year,
    duration,
    link_to_relevant_documents
) VALUES (
    $id,
    $title,
    $type,
    $agency_id,
    $user_id,
    $source_of_financial_support,
    $year,
    $duration,
    $link_to_relevant_documents
);