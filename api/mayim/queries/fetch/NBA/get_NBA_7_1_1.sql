SELECT
    l.name AS laboratory_name,
    l.batch_size AS,
    l.name_of_equipment AS equipment_name,
    l.weekly_utilization AS equipment_utilization,
    tm.name AS technical_staff_name AS staff_name,
    tm.designation AS staff_designation,
    tm.qualification AS staff_qualification,
FROM
    laboratories l
JOIN
    laboratory_technical_manpower ltm ON l.id = ltm.laboratory_id
JOIN
    laboratories_technical_manpower tm ON ltm.technical_manpower_id = tm.id;
