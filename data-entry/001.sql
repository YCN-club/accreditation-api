-- 1. USERS (no dependencies)
INSERT INTO "users" ("id", "first_name", "middle_name", "last_name", "email")
VALUES 
('6379fcb6-7530-46b1-86d0-13190c8516fa', 'Abhigyan', '','Trips', 'abhigyantrips@gmail.com'),
('6f936c2f-9a9c-43e3-b9b4-59d94a0ac131', 'Raghav' ,'', 'Gupta','rg@gmail.com'),
('11111111-1111-1111-1111-111111111101', 'Alice', 'A.', 'Smith', 'alice.smith@example.com'),
('11111111-1111-1111-1111-111111111102', 'Bob', 'B.', 'Jones', 'bob.jones@example.com'),
('11111111-1111-1111-1111-111111111103', 'Charlie', 'C.', 'Brown', 'charlie.brown@example.com'),
('11111111-1111-1111-1111-111111111104', 'David', 'D.', 'Johnson', 'david.johnson@example.com'),
('11111111-1111-1111-1111-111111111105', 'Eve', 'E.', 'Williams', 'eve.williams@example.com'),
('11111111-1111-1111-1111-111111111106', 'Frank', 'F.', 'Miller', 'frank.miller@example.com'),
('11111111-1111-1111-1111-111111111107', 'Grace', 'G.', 'Davis', 'grace.davis@example.com'),
('11111111-1111-1111-1111-111111111108', 'Hank', 'H.', 'Wilson', 'hank.wilson@example.com'),
('11111111-1111-1111-1111-111111111109', 'Ivy', 'I.', 'Moore', 'ivy.moore@example.com'),
('11111111-1111-1111-1111-111111111110', 'Jake', 'J.', 'Taylor', 'jake.taylor@example.com');

-- 2. AUTH (depends on "users")
INSERT INTO "auth" ("id", "password", "last_login", "requires_reset")
VALUES
('6379fcb6-7530-46b1-86d0-13190c8516fa' ,'$2a$12$fc1eZBkWWMZm0xyo2KimIezjSnlFKY.M55Ibc4h7NDeS/WXBMYGU.', NULL, false),
('6f936c2f-9a9c-43e3-b9b4-59d94a0ac131' ,'$2b$12$Lh22WuDAhIxTMTlZfg9klu0SYf5zomA4wXfPxohwez7WoxJjmLQpS', NULL, false),
('11111111-1111-1111-1111-111111111101', 'password1', '2025-02-01 10:00:00', false),
('11111111-1111-1111-1111-111111111102', 'password2', '2025-02-02 11:00:00', false),
('11111111-1111-1111-1111-111111111103', 'password3', '2025-02-03 12:00:00', false),
('11111111-1111-1111-1111-111111111104', 'password4', '2025-02-04 13:00:00', false),
('11111111-1111-1111-1111-111111111105', 'password5', '2025-02-05 14:00:00', false),
('11111111-1111-1111-1111-111111111106', 'password6', '2025-02-06 15:00:00', false),
('11111111-1111-1111-1111-111111111107', 'password7', '2025-02-07 16:00:00', false),
('11111111-1111-1111-1111-111111111108', 'password8', '2025-02-08 17:00:00', false),
('11111111-1111-1111-1111-111111111109', 'password9', '2025-02-09 18:00:00', false),
('11111111-1111-1111-1111-111111111110', 'password10', '2025-02-10 19:00:00', false);

-- 3. COMPANIES (no dependencies)
INSERT INTO "companies" ("id", "name", "contact_no", "contact_email")
VALUES
('22222222-2222-2222-2222-222222222201', 'ABC Pvt. Ltd.', '111-222-0001', 'hr@abc.com'),
('22222222-2222-2222-2222-222222222202', 'XYZ Corp.', '111-222-0002', 'contact@xyz.com'),
('22222222-2222-2222-2222-222222222203', 'Tech Solutions', '111-222-0003', 'info@techsolutions.com'),
('22222222-2222-2222-2222-222222222204', 'Global Industries', '111-222-0004', 'info@globalind.com'),
('22222222-2222-2222-2222-222222222205', 'Innovate LLC', '111-222-0005', 'hi@innovate.co'),
('22222222-2222-2222-2222-222222222206', 'AutoMech Ltd.', '111-222-0006', 'support@automech.com'),
('22222222-2222-2222-2222-222222222207', 'BioHealth Inc.', '111-222-0007', 'contact@biohealth.com'),
('22222222-2222-2222-2222-222222222208', 'DataPrime', '111-222-0008', 'sales@dataprime.com'),
('22222222-2222-2222-2222-222222222209', 'Foodies Co.', '111-222-0009', 'hello@foodies.co'),
('22222222-2222-2222-2222-222222222210', 'GreenEnergy', '111-222-0010', 'info@greeneng.com');

-- 4. AGENCIES (no dependencies)
INSERT INTO "agencies" ("id", "name", "contact_no", "contact_email")
VALUES
('33333333-3333-3333-3333-333333333301', 'Agency One', '222-333-0001', 'info@agencyone.com'),
('33333333-3333-3333-3333-333333333302', 'Agency Two', '222-333-0002', 'contact@agencytwo.com'),
('33333333-3333-3333-3333-333333333303', 'Agency Three', '222-333-0003', 'mail@agencythree.com'),
('33333333-3333-3333-3333-333333333304', 'Agency Four', '222-333-0004', 'hello@agencyfour.com'),
('33333333-3333-3333-3333-333333333305', 'Agency Five', '222-333-0005', 'support@agencyfive.com'),
('33333333-3333-3333-3333-333333333306', 'Agency Six', '222-333-0006', 'info@agencysix.com'),
('33333333-3333-3333-3333-333333333307', 'Agency Seven', '222-333-0007', 'contact@agencyseven.com'),
('33333333-3333-3333-3333-333333333308', 'Agency Eight', '222-333-0008', 'info@agencyeight.com'),
('33333333-3333-3333-3333-333333333309', 'Agency Nine', '222-333-0009', 'mail@agencynine.com'),
('33333333-3333-3333-3333-333333333310', 'Agency Ten', '222-333-0010', 'hello@agencyten.com');

-- 5. FACILITIES (no dependencies)
INSERT INTO "facilities" ("id", "name", "type", "is_ict", "details", "reasons", "utilization", "relevance_to_pos")
VALUES
('44444444-4444-4444-4444-444444444401', 'Library Building', 'Infrastructure', true, 'Digital library', '{"Space", "Resources"}', 'Daily usage', 'POS1'),
('44444444-4444-4444-4444-444444444402', 'Main Auditorium', 'Auditorium', false, 'Seating for 300', '{"Events", "Conferences"}', 'Weekly events', 'POS2'),
('44444444-4444-4444-4444-444444444403', 'Computer Lab 1', 'Lab', true, 'Equipped with 50 PCs', '{"Classes", "Research"}', 'Daily usage', 'POS3'),
('44444444-4444-4444-4444-444444444404', 'Workshop Hall', 'Workshop', false, 'Mechanical tools', '{"Training", "Workshops"}', 'Occasional training', 'POS4'),
('44444444-4444-4444-4444-444444444405', 'Seminar Room', 'Meeting', false, 'Projector & seats', '{"Meetings", "Seminars"}', 'Frequent sessions', 'POS2'),
('44444444-4444-4444-4444-444444444406', 'Language Lab', 'Lab', true, 'Software for language learning', '{"Classes", "Language Tests"}', 'Daily usage', 'POS3'),
('44444444-4444-4444-4444-444444444407', 'Sports Complex', 'Recreation', false, 'Indoor & outdoor courts', '{"Training", "Tournaments"}', 'Daily usage', 'POS5'),
('44444444-4444-4444-4444-444444444408', 'Music Room', 'Cultural', false, 'Musical instruments', '{"Practice", "Rehearsals"}', 'Weekly practice', 'POS4'),
('44444444-4444-4444-4444-444444444409', 'Cafeteria', 'Food Service', false, 'Dining hall', '{"Meals", "Refreshments"}', 'Daily usage', 'POS1'),
('44444444-4444-4444-4444-444444444410', 'Reading Room', 'Study', true, 'Quiet study area', '{"Research", "Study"}', 'Daily usage', 'POS1');


-- 6. JOURNALS (no new dependency)
INSERT INTO "journals" ("id", "name", "frequency", "type", "scopus_indexed")
VALUES
('66666666-6666-6666-6666-666666666601', 'Journal of AI', 'MONTHLY', 'HARDCOPY', true),
('66666666-6666-6666-6666-666666666602', 'Tech Today', 'WEEKLY', 'SOFTCOPY', false),
('66666666-6666-6666-6666-666666666603', 'Global Science', 'YEARLY', 'HARDCOPY', true),
('66666666-6666-6666-6666-666666666604', 'Engineering Insights', 'QUARTERLY', 'HARDCOPY', false),
('66666666-6666-6666-6666-666666666605', 'Bio Research', 'MONTHLY', 'SOFTCOPY', true),
('66666666-6666-6666-6666-666666666606', 'Robotics Weekly', 'WEEKLY', 'HARDCOPY', false),
('66666666-6666-6666-6666-666666666607', 'Medical Innovations', 'BIWEEKLY', 'SOFTCOPY', true),
('66666666-6666-6666-6666-666666666608', 'Data Analytics Review', 'MONTHLY', 'SOFTCOPY', true),
('66666666-6666-6666-6666-666666666609', 'Quantum Horizons', 'QUARTERLY', 'HARDCOPY', false),
('66666666-6666-6666-6666-666666666610', 'Environmental Studies', 'YEARLY', 'SOFTCOPY', true);

-- 7. SPONSORSHIPS (no new dependency)
INSERT INTO "sponsorships" ("id", "agency_name", "year", "amount_inr", "project_title")
VALUES
('77777777-7777-7777-7777-777777777701', 'Tech Aid', 2024, 500000, 'Research in AI'),
('77777777-7777-7777-7777-777777777702', 'Health & Co.', 2023, 300000, 'Community Health Project'),
('77777777-7777-7777-7777-777777777703', 'Eco Funding', 2022, 200000, 'Green Energy Solutions'),
('77777777-7777-7777-7777-777777777704', 'Innovators Hub', 2025, 750000, 'Robotics Development'),
('77777777-7777-7777-7777-777777777705', 'Software Supporters', 2024, 400000, 'Big Data Research'),
('77777777-7777-7777-7777-777777777706', 'Digital Boost', 2025, 1000000, 'Cloud Computing Lab'),
('77777777-7777-7777-7777-777777777707', 'Bio Grants', 2023, 250000, 'Vaccine Development'),
('77777777-7777-7777-7777-777777777708', 'Auto Sponsors', 2024, 600000, 'Electric Vehicle R&D'),
('77777777-7777-7777-7777-777777777709', 'Infra Aid', 2022, 100000, 'Campus Remodeling'),
('77777777-7777-7777-7777-777777777710', 'Global Corp.', 2025, 850000, 'International Collaboration');

-- 8. IPR (depends on "users" - awardee_id)
INSERT INTO "ipr" ("id", "awardee_id", "awarder_name", "government_recognized", "year", "uuid", "title", "type", "status")
VALUES
('88888888-8888-8888-8888-888888888801', '11111111-1111-1111-1111-111111111101', 'Patent Office A', true, 2023, 'UUID-PT-0001', 'AI Algorithm Patent', 'PATENT', 'FILED'),
('88888888-8888-8888-8888-888888888802', '11111111-1111-1111-1111-111111111102', 'Patent Office B', false, 2022, 'UUID-PT-0002', 'Mechanical Design', 'PATENT', 'GRANTED'),
('88888888-8888-8888-8888-888888888803', '11111111-1111-1111-1111-111111111103', 'Design Office C', false, 2024, 'UUID-DS-0003', 'UI Layout', 'DESIGN', 'FILED'),
('88888888-8888-8888-8888-888888888804', '11111111-1111-1111-1111-111111111104', 'Copyright Agency', true, 2021, 'UUID-CP-0004', 'Textbook Materials', 'COPYRIGHT', 'GRANTED'),
('88888888-8888-8888-8888-888888888805', '11111111-1111-1111-1111-111111111105', 'Patent Office D', false, 2023, 'UUID-PT-0005', 'Nano-Tech Patent', 'PATENT', 'LICENSED'),
('88888888-8888-8888-8888-888888888806', '11111111-1111-1111-1111-111111111106', 'Patent Office E', true, 2024, 'UUID-PT-0006', 'AR/VR Technology', 'PATENT', 'FILED'),
('88888888-8888-8888-8888-888888888807', '11111111-1111-1111-1111-111111111107', 'Design Office D', true, 2025, 'UUID-DS-0007', 'Product Packaging', 'DESIGN', 'GRANTED'),
('88888888-8888-8888-8888-888888888808', '11111111-1111-1111-1111-111111111108', 'Copyright Agency', false, 2020, 'UUID-CP-0008', 'Online Course Materials', 'COPYRIGHT', 'COLLABORATIVE'),
('88888888-8888-8888-8888-888888888809', '11111111-1111-1111-1111-111111111109', 'Patent Office F', true, 2025, 'UUID-PT-0009', 'Water Purification', 'PATENT', 'FILED'),
('88888888-8888-8888-8888-888888888810', '11111111-1111-1111-1111-111111111110', 'Copyright Agency', false, 2022, 'UUID-CP-0010', 'E-Learning Platform', 'COPYRIGHT', 'LICENSED');

-- 9. IPR_EARNINGS (depends on "ipr")
INSERT INTO "ipr_earnings" ("ipr_id", "financial_year", "amount_inr")
VALUES
('88888888-8888-8888-8888-888888888801', 2023, 100000),
('88888888-8888-8888-8888-888888888802', 2022, 50000),
('88888888-8888-8888-8888-888888888803', 2024, 75000),
('88888888-8888-8888-8888-888888888804', 2021, 120000),
('88888888-8888-8888-8888-888888888805', 2023, 185000),
('88888888-8888-8888-8888-888888888806', 2024, 60000),
('88888888-8888-8888-8888-888888888807', 2025, 95000),
('88888888-8888-8888-8888-888888888808', 2020, 70000),
('88888888-8888-8888-8888-888888888809', 2025, 105000),
('88888888-8888-8888-8888-888888888810', 2022, 90000);

-- 10. JOURNAL_PUBLICATIONS (depends on "journals" and "sponsorships")
INSERT INTO "journal_publications"
("id", "journal_id", "journal_volume_number", "journal_issue_number", "sponsor_id", "year", "semester", "doi", "title")
VALUES
('99999999-9999-9999-9999-999999999901', '66666666-6666-6666-6666-666666666601', 1, 1, '77777777-7777-7777-7777-777777777701', 2023, 'ODD', '10.1000/xyz123', 'AI in Healthcare'),
('99999999-9999-9999-9999-999999999902', '66666666-6666-6666-6666-666666666602', 2, 3, '77777777-7777-7777-7777-777777777702', 2024, 'EVEN', '10.1000/xyz124', 'Tech Trends 2024'),
('99999999-9999-9999-9999-999999999903', '66666666-6666-6666-6666-666666666603', 3, 5, '77777777-7777-7777-7777-777777777703', 2022, 'ODD', '10.1000/xyz125', 'Global Science Overview'),
('99999999-9999-9999-9999-999999999904', '66666666-6666-6666-6666-666666666604', 4, 2, '77777777-7777-7777-7777-777777777704', 2025, 'EVEN', '10.1000/xyz126', 'Engineering Insights Vol.4'),
('99999999-9999-9999-9999-999999999905', '66666666-6666-6666-6666-666666666605', 2, 1, '77777777-7777-7777-7777-777777777705', 2023, 'ODD', '10.1000/xyz127', 'Bio Research Findings'),
('99999999-9999-9999-9999-999999999906', '66666666-6666-6666-6666-666666666606', 1, 4, '77777777-7777-7777-7777-777777777706', 2023, 'EVEN', '10.1000/xyz128', 'Weekly Robotics Review'),
('99999999-9999-9999-9999-999999999907', '66666666-6666-6666-6666-666666666607', 3, 6, '77777777-7777-7777-7777-777777777707', 2025, 'ODD', '10.1000/xyz129', 'Medical Innovations Today'),
('99999999-9999-9999-9999-999999999908', '66666666-6666-6666-6666-666666666608', 5, 3, '77777777-7777-7777-7777-777777777708', 2024, 'EVEN', '10.1000/xyz130', 'Big Data & Analytics'),
('99999999-9999-9999-9999-999999999909', '66666666-6666-6666-6666-666666666609', 1, 1, '77777777-7777-7777-7777-777777777709', 2022, 'ODD', '10.1000/xyz131', 'Quantum Horizons Study'),
('99999999-9999-9999-9999-999999999910', '66666666-6666-6666-6666-666666666610', 2, 2, '77777777-7777-7777-7777-777777777710', 2025, 'EVEN', '10.1000/xyz132', 'Environmental Research');
