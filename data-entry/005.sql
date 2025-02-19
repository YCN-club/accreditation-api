-- 41. LABORATORIES_TECHNICAL_MANPOWER
INSERT INTO "laboratories_technical_manpower" ("id", "name", "designation", "qualification")
VALUES
('LT000000-0000-0000-0000-000000000001', 'John Doe', 'Technician', 'Diploma in Electronics'),
('LT000000-0000-0000-0000-000000000002', 'Jane Smith', 'Senior Technician', 'B.Tech in Electronics'),
('LT000000-0000-0000-0000-000000000003', 'Alice Johnson', 'Lab Assistant', 'Certificate in Lab Management'),
('LT000000-0000-0000-0000-000000000004', 'Robert Brown', 'Technician', 'Diploma in Mechanical Engineering'),
('LT000000-0000-0000-0000-000000000005', 'Emily Davis', 'Senior Technician', 'B.Tech in Mechanical Engineering'),
('LT000000-0000-0000-0000-000000000006', 'Michael Wilson', 'Lab Engineer', 'B.Tech in Chemical Engineering'),
('LT000000-0000-0000-0000-000000000007', 'Sarah Miller', 'Assistant Lab Engineer', 'Diploma in Chemical Technology'),
('LT000000-0000-0000-0000-000000000008', 'David Taylor', 'Technician', 'Diploma in IT'),
('LT000000-0000-0000-0000-000000000009', 'Laura Moore', 'Senior Technician', 'B.Tech in IT'),
('LT000000-0000-0000-0000-000000000010', 'Daniel Anderson', 'Lab Supervisor', 'MBA');

-- 42. E_RESOURCES
INSERT INTO "e_resources" ("faculty_id", "name", "development_platform", "date_of_launch", "link_to_relevant_document", "institute")
VALUES
('F0000000-0000-0000-0000-000000000001', 'E-Resource Portal A', 'Moodle', '2025-01-15', 'http://example.com/eresourceA', 'Institute A'),
('F0000000-0000-0000-0000-000000000002', 'E-Resource Portal B', 'Blackboard', '2025-02-20', 'http://example.com/eresourceB', 'Institute B'),
('F0000000-0000-0000-0000-000000000003', 'Digital Library', 'Canvas', '2025-03-10', 'http://example.com/digitallibrary', 'Institute C'),
('F0000000-0000-0000-0000-000000000004', 'Online Lab Manual', 'Google Classroom', '2025-04-05', 'http://example.com/olabmanual', 'Institute D'),
('F0000000-0000-0000-0000-000000000005', 'Video Tutorials', 'YouTube', '2025-05-15', 'http://example.com/videotutorials', 'Institute E'),
('F0000000-0000-0000-0000-000000000006', 'Webinars Hub', 'Zoom', '2025-06-25', 'http://example.com/webinars', 'Institute F'),
('F0000000-0000-0000-0000-000000000007', 'Interactive Module', 'Articulate', '2025-07-30', 'http://example.com/module', 'Institute G'),
('F0000000-0000-0000-0000-000000000008', 'Resource Center', 'Custom LMS', '2025-08-15', 'http://example.com/resourcecenter', 'Institute H'),
('F0000000-0000-0000-0000-000000000009', 'E-Learning Suite', 'Moodle', '2025-09-10', 'http://example.com/elearningsuite', 'Institute I'),
('F0000000-0000-0000-0000-000000000010', 'Digital Courseware', 'Canvas', '2025-10-05', 'http://example.com/digitalcourseware', 'Institute J');

-- 43. AFTER_GRADUATION
INSERT INTO "after_graduation" ("id", "student_id", "year", "type")
VALUES
('AG000000-0000-0000-0000-000000000001', 'S0000000-0000-0000-0000-000000000001', 2029, 'PLACEMENT'),
('AG000000-0000-0000-0000-000000000002', 'S0000000-0000-0000-0000-000000000002', 2029, 'ENTREPRENEURSHIP'),
('AG000000-0000-0000-0000-000000000003', 'S0000000-0000-0000-0000-000000000003', 2028, 'HIGHER_STUDIES'),
('AG000000-0000-0000-0000-000000000004', 'S0000000-0000-0000-0000-000000000004', 2029, 'PLACEMENT'),
('AG000000-0000-0000-0000-000000000005', 'S0000000-0000-0000-0000-000000000005', 2029, 'ENTREPRENEURSHIP'),
('AG000000-0000-0000-0000-000000000006', 'S0000000-0000-0000-0000-000000000006', 2028, 'HIGHER_STUDIES'),
('AG000000-0000-0000-0000-000000000007', 'S0000000-0000-0000-0000-000000000007', 2029, 'PLACEMENT'),
('AG000000-0000-0000-0000-000000000008', 'S0000000-0000-0000-0000-000000000008', 2029, 'ENTREPRENEURSHIP'),
('AG000000-0000-0000-0000-000000000009', 'S0000000-0000-0000-0000-000000000009', 2028, 'HIGHER_STUDIES'),
('AG000000-0000-0000-0000-000000000010', 'S0000000-0000-0000-0000-000000000010', 2029, 'PLACEMENT');

-- 44. AFTER_GRADUATION_PLACEMENTS
INSERT INTO "after_graduation_placements" ("after_graduation_id", "employer_id", "salary")
VALUES
('AG000000-0000-0000-0000-000000000001', 'COMP00001-0000-0000-0000-000000000001', 50000),
('AG000000-0000-0000-0000-000000000004', 'COMP00001-0000-0000-0000-000000000002', 60000),
('AG000000-0000-0000-0000-000000000007', 'COMP00001-0000-0000-0000-000000000003', 55000),
('AG000000-0000-0000-0000-000000000010', 'COMP00001-0000-0000-0000-000000000004', 65000),
('AG000000-0000-0000-0000-000000000002', 'COMP00001-0000-0000-0000-000000000005', 70000),
('AG000000-0000-0000-0000-000000000005', 'COMP00001-0000-0000-0000-000000000006', 52000),
('AG000000-0000-0000-0000-000000000008', 'COMP00001-0000-0000-0000-000000000007', 58000),
('AG000000-0000-0000-0000-000000000003', 'COMP00001-0000-0000-0000-000000000008', 60000),
('AG000000-0000-0000-0000-000000000006', 'COMP00001-0000-0000-0000-000000000009', 54000),
('AG000000-0000-0000-0000-000000000009', 'COMP00001-0000-0000-0000-000000000010', 59000);

-- 45. AFTER_GRADUATION_HIGHER_STUDIES
INSERT INTO "after_graduation_higher_studies" ("after_graduation_id", "institute_name", "program_name", "with_exam")
VALUES
('AG000000-0000-0000-0000-000000000003', 'Univ X', 'Masters in Data Science', true),
('AG000000-0000-0000-0000-000000000006', 'Univ Y', 'MBA', false),
('AG000000-0000-0000-0000-000000000009', 'Univ Z', 'PhD in Renewable Energy', true),
('AG000000-0000-0000-0000-000000000002', 'Univ A', 'Masters in Management', true),
('AG000000-0000-0000-0000-000000000005', 'Univ B', 'Masters in Mechanical Engineering', false),
('AG000000-0000-0000-0000-000000000008', 'Univ C', 'Masters in Computer Science', true),
('AG000000-0000-0000-0000-000000000001', 'Univ D', 'Masters in Electrical Engineering', false),
('AG000000-0000-0000-0000-000000000004', 'Univ E', 'Masters in Biotechnology', true),
('AG000000-0000-0000-0000-000000000007', 'Univ F', 'Masters in Chemical Engineering', false),
('AG000000-0000-0000-0000-000000000010', 'Univ G', 'Masters in Civil Engineering', true);

-- 46. BENEFIT_PROGRAMS
INSERT INTO "benefit_programs" ("id", "student_id", "year", "type")
VALUES
('BP000000-0000-0000-0000-000000000001', 'S0000000-0000-0000-0000-000000000001', 2025, 'GOVERNMENT'),
('BP000000-0000-0000-0000-000000000002', 'S0000000-0000-0000-0000-000000000002', 2025, 'NON_GOVERNMENT'),
('BP000000-0000-0000-0000-000000000003', 'S0000000-0000-0000-0000-000000000003', 2025, 'INSTITUTIONAL'),
('BP000000-0000-0000-0000-000000000004', 'S0000000-0000-0000-0000-000000000004', 2025, 'COMPETITIVE_EXAM_GUIDANCE'),
('BP000000-0000-0000-0000-000000000005', 'S0000000-0000-0000-0000-000000000005', 2025, 'GOVERNMENT'),
('BP000000-0000-0000-0000-000000000006', 'S0000000-0000-0000-0000-000000000006', 2025, 'INSTITUTIONAL'),
('BP000000-0000-0000-0000-000000000007', 'S0000000-0000-0000-0000-000000000007', 2025, 'NON_GOVERNMENT'),
('BP000000-0000-0000-0000-000000000008', 'S0000000-0000-0000-0000-000000000008', 2025, 'GOVERNMENT'),
('BP000000-0000-0000-0000-000000000009', 'S0000000-0000-0000-0000-000000000009', 2025, 'COMPETITIVE_EXAM_GUIDANCE'),
('BP000000-0000-0000-0000-000000000010', 'S0000000-0000-0000-0000-000000000010', 2025, 'INSTITUTIONAL');

-- 47. NATIONAL_GOVERNMENT_EXAMS
INSERT INTO "national_government_exams" ("id", "student_id", "exam_type")
VALUES
('NGE000000-0000-0000-0000-000000000001', 'S0000000-0000-0000-0000-000000000001', 'GATE'),
('NGE000000-0000-0000-0000-000000000002', 'S0000000-0000-0000-0000-000000000002', 'NET'),
('NGE000000-0000-0000-0000-000000000003', 'S0000000-0000-0000-0000-000000000003', 'CAT'),
('NGE000000-0000-0000-0000-000000000004', 'S0000000-0000-0000-0000-000000000004', 'GRE'),
('NGE000000-0000-0000-0000-000000000005', 'S0000000-0000-0000-0000-000000000005', 'GATE'),
('NGE000000-0000-0000-0000-000000000006', 'S0000000-0000-0000-0000-000000000006', 'GMAT'),
('NGE000000-0000-0000-0000-000000000007', 'S0000000-0000-0000-0000-000000000007', 'NET'),
('NGE000000-0000-0000-0000-000000000008', 'S0000000-0000-0000-0000-000000000008', 'SLET'),
('NGE000000-0000-0000-0000-000000000009', 'S0000000-0000-0000-0000-000000000009', 'GATE'),
('NGE000000-0000-0000-0000-000000000010', 'S0000000-0000-0000-0000-000000000010', 'CAT');

-- 48. FACILITIES
INSERT INTO "facilities" ("id", "name", "type", "is_ict", "details", "reasons", "utilization", "relevance_to_pos")
VALUES
('FCLT0000-0000-0000-0000-000000000001', 'Main Auditorium', 'Auditorium', false, 'Large capacity auditorium', '{"Spacious", "Well-equipped"}', '80%', 'High'),
('FCLT0000-0000-0000-0000-000000000002', 'Library', 'Library', true, 'Central library with digital resources', '{"Modern", "Accessible"}', '90%', 'Very High'),
('FCLT0000-0000-0000-0000-000000000003', 'Computer Lab', 'Lab', true, 'High-spec computers and networked', '{"Up-to-date", "Secure"}', '85%', 'High'),
('FCLT0000-0000-0000-0000-000000000004', 'Workshop', 'Workshop', false, 'Technical workshop space', '{"Well-ventilated", "Spacious"}', '75%', 'Medium'),
('FCLT0000-0000-0000-0000-000000000005', 'Conference Room', 'Conference', true, 'Room equipped with AV facilities', '{"Modern", "Ergonomic"}', '70%', 'Medium'),
('FCLT0000-0000-0000-0000-000000000006', 'Sports Complex', 'Sports', false, 'Indoor sports facility', '{"Brand new", "Spacious"}', '65%', 'High'),
('FCLT0000-0000-0000-0000-000000000007', 'Canteen', 'Canteen', false, 'Food and beverage facility', '{"Clean", "Efficient"}', '50%', 'Low'),
('FCLT0000-0000-0000-0000-000000000008', 'Research Center', 'Research', true, 'Lab for research activities', '{"Advanced", "Specialized"}', '80%', 'Very High'),
('FCLT0000-0000-0000-0000-000000000009', 'Admin Block', 'Administration', true, 'Main administrative block', '{"Central", "Modern"}', '95%', 'High'),
('FCLT0000-0000-0000-0000-000000000010', 'Multipurpose Hall', 'Hall', false, 'Hall for events and ceremonies', '{"Spacious", "Versatile"}', '85%', 'High');

-- 49. LABORATORIES
INSERT INTO "laboratories" ("id", "batch_size", "name_of_equipment", "safety_measures", "weekly_utilization", "technical_manpower_ids")
VALUES
('LAB000000-0000-0000-0000-000000000001', 30, '{"Microscopes", "Spectrometers"}', '{"Fire Extinguishers", "First Aid Kit"}', 40, '{"LT000000-0000-0000-0000-000000000001", "LT000000-0000-0000-0000-000000000002"}'),
('LAB000000-0000-0000-0000-000000000002', 25, '{"Oscilloscopes", "Power Supplies"}', '{"Safety Goggles", "Lab Coats"}', 35, '{"LT000000-0000-0000-0000-000000000003"}'),
('LAB000000-0000-0000-0000-000000000003', 40, '{"3D Printers", "Laser Cutters"}', '{"Emergency Exits", "Fire Alarms"}', 50, '{"LT000000-0000-0000-0000-000000000004", "LT000000-0000-0000-0000-000000000005"}'),
('LAB000000-0000-0000-0000-000000000004', 20, '{"Robotics Kits", "Soldering Stations"}', '{"Ventilation", "Safety Training"}', 30, '{"LT000000-0000-0000-0000-000000000006"}'),
('LAB000000-0000-0000-0000-000000000005', 35, '{"VR Headsets", "High-performance PCs"}', '{"Surge Protectors", "Air Conditioners"}', 45, '{"LT000000-0000-0000-0000-000000000007"}'),
('LAB000000-0000-0000-0000-000000000006', 28, '{"Chemical Analyzers", "Fume Hoods"}', '{"Gloves", "Face Shields"}', 38, '{"LT000000-0000-0000-0000-000000000008"}'),
('LAB000000-0000-0000-0000-000000000007', 32, '{"Biometric Scanners", "DNA Sequencers"}', '{"Biosafety Cabinets", "Emergency Showers"}', 42, '{"LT000000-0000-0000-0000-000000000009"}'),
('LAB000000-0000-0000-0000-000000000008', 22, '{"Thermal Cameras", "Infrared Sensors"}', '{"Fire Blankets", "Emergency Lights"}', 33, '{"LT000000-0000-0000-0000-000000000010"}'),
('LAB000000-0000-0000-0000-000000000009', 27, '{"Automated Analyzers", "Data Loggers"}', '{"Safety Signage", "Spill Kits"}', 37, '{"LT000000-0000-0000-0000-000000000001"}'),
('LAB000000-0000-0000-0000-000000000010', 30, '{"High-speed Cameras", "Measurement Instruments"}', '{"Emergency Exits", "Personal Protective Equipment"}', 40, '{"LT000000-0000-0000-0000-000000000002", "LT000000-0000-0000-0000-000000000003"}');

-- 50. LABORATORIES_TECHNICAL_MANPOWER
INSERT INTO "laboratories_technical_manpower" ("id", "name", "designation", "qualification")
VALUES
('LT000000-0000-0000-0000-000000000001', 'John Doe', 'Technician', 'Diploma in Electronics'),
('LT000000-0000-0000-0000-000000000002', 'Jane Smith', 'Senior Technician', 'B.Tech in Electronics'),
('LT000000-0000-0000-0000-000000000003', 'Alice Johnson', 'Lab Assistant', 'Certificate in Lab Management'),
('LT000000-0000-0000-0000-000000000004', 'Robert Brown', 'Technician', 'Diploma in Mechanical Engineering'),
('LT000000-0000-0000-0000-000000000005', 'Emily Davis', 'Senior Technician', 'B.Tech in Mechanical Engineering'),
('LT000000-0000-0000-0000-000000000006', 'Michael Wilson', 'Lab Engineer', 'B.Tech in Chemical Engineering'),
('LT000000-0000-0000-0000-000000000007', 'Sarah Miller', 'Assistant Lab Engineer', 'Diploma in Chemical Technology'),
('LT000000-0000-0000-0000-000000000008', 'David Taylor', 'Technician', 'Diploma in IT'),
('LT000000-0000-0000-0000-000000000009', 'Laura Moore', 'Senior Technician', 'B.Tech in IT'),
('LT000000-0000-0000-0000-000000000010', 'Daniel Anderson', 'Lab Supervisor', 'MBA');

-- 51. LABORATORY_TECHNICAL_MANPOWER (Junction Table)
INSERT INTO "laboratory_technical_manpower" ("laboratory_id", "technical_manpower_id")
VALUES
('LAB000000-0000-0000-0000-000000000001', 'LT000000-0000-0000-0000-000000000001'),
('LAB000000-0000-0000-0000-000000000001', 'LT000000-0000-0000-0000-000000000002'),
('LAB000000-0000-0000-0000-000000000002', 'LT000000-0000-0000-0000-000000000003'),
('LAB000000-0000-0000-0000-000000000003', 'LT000000-0000-0000-0000-000000000004'),
('LAB000000-0000-0000-0000-000000000003', 'LT000000-0000-0000-0000-000000000005'),
('LAB000000-0000-0000-0000-000000000004', 'LT000000-0000-0000-0000-000000000006'),
('LAB000000-0000-0000-0000-000000000005', 'LT000000-0000-0000-0000-000000000007'),
('LAB000000-0000-0000-0000-000000000006', 'LT000000-0000-0000-0000-000000000008'),
('LAB000000-0000-0000-0000-000000000007', 'LT000000-0000-0000-0000-000000000009'),
('LAB000000-0000-0000-0000-000000000008', 'LT000000-0000-0000-0000-000000000010'),
('LAB000000-0000-0000-0000-000000000009', 'LT000000-0000-0000-0000-000000000001'),
('LAB000000-0000-0000-0000-000000000010', 'LT000000-0000-0000-0000-000000000002'),
('LAB000000-0000-0000-0000-000000000010', 'LT000000-0000-0000-0000-000000000003');

-- 52. E_RESOURCES
INSERT INTO "e_resources" ("faculty_id", "name", "development_platform", "date_of_launch", "link_to_relevant_document", "institute")
VALUES
('F0000000-0000-0000-0000-000000000001', 'Learning Portal A', 'Moodle', '2025-01-05', 'http://example.com/portalA', 'Institute A'),
('F0000000-0000-0000-0000-000000000002', 'Digital Library', 'Blackboard', '2025-02-10', 'http://example.com/digitallib', 'Institute B'),
('F0000000-0000-0000-0000-000000000003', 'Online Courseware', 'Canvas', '2025-03-15', 'http://example.com/courseware', 'Institute C'),
('F0000000-0000-0000-0000-000000000004', 'Resource Hub', 'Google Classroom', '2025-04-20', 'http://example.com/resourcehub', 'Institute D'),
('F0000000-0000-0000-0000-000000000005', 'E-Learning Center', 'Custom LMS', '2025-05-25', 'http://example.com/elearn', 'Institute E'),
('F0000000-0000-0000-0000-000000000006', 'Virtual Lab', 'Moodle', '2025-06-30', 'http://example.com/virtuallab', 'Institute F'),
('F0000000-0000-0000-0000-000000000007', 'Interactive Tutorials', 'YouTube', '2025-07-05', 'http://example.com/tutorials', 'Institute G'),
('F0000000-0000-0000-0000-000000000008', 'Webinars Portal', 'Zoom', '2025-08-10', 'http://example.com/webinars', 'Institute H'),
('F0000000-0000-0000-0000-000000000009', 'Digital Archives', 'Canvas', '2025-09-15', 'http://example.com/archives', 'Institute I'),
('F0000000-0000-0000-0000-000000000010', 'Online Repository', 'Moodle', '2025-10-20', 'http://example.com/repository', 'Institute J');