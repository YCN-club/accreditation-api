SELECT 
    f.name AS facility_name,
    f.details,
    f.reasons,
    f.utilization,
    f.relevance_to_pos
FROM 
    facilities f;
