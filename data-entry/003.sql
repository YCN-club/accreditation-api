-- 21. DEPARTMENTS (depends on programs)
INSERT INTO "departments" ("id", "name", "program_id")
VALUES
('aaaaaaaa-0000-0000-0000-000000000001', 'Computer Science Department', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD1'),
('aaaaaaaa-0000-0000-0000-000000000002', 'Mechanical Engineering Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD2'),
('aaaaaaaa-0000-0000-0000-000000000003', 'Business Administration Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD3'),
('aaaaaaaa-0000-0000-0000-000000000004', 'Electrical Engineering Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD4'),
('aaaaaaaa-0000-0000-0000-000000000005', 'Civil Engineering Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD5'),
('aaaaaaaa-0000-0000-0000-000000000006', 'Information Technology Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD6'),
('aaaaaaaa-0000-0000-0000-000000000007', 'Design Department', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD7'),
('aaaaaaaa-0000-0000-0000-000000000008', 'Chemical Engineering Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD8'),
('aaaaaaaa-0000-0000-0000-000000000009', 'Electronics Engineering Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDD9'),
('aaaaaaaa-0000-0000-0000-000000000010', 'Automation Dept', 'DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDD10');

-- 22. BRANCHES (depends on departments)
INSERT INTO "branches" ("id", "name", "department_id")
VALUES
('bbbbbbbb-0000-0000-0000-000000000001', 'Branch A', 'aaaaaaaa-0000-0000-0000-000000000001'),
('bbbbbbbb-0000-0000-0000-000000000002', 'Branch B', 'aaaaaaaa-0000-0000-0000-000000000002'),
('bbbbbbbb-0000-0000-0000-000000000003', 'Branch C', 'aaaaaaaa-0000-0000-0000-000000000003'),
('bbbbbbbb-0000-0000-0000-000000000004', 'Branch D', 'aaaaaaaa-0000-0000-0000-000000000004'),
('bbbbbbbb-0000-0000-0000-000000000005', 'Branch E', 'aaaaaaaa-0000-0000-0000-000000000005'),
('bbbbbbbb-0000-0000-0000-000000000006', 'Branch F', 'aaaaaaaa-0000-0000-0000-000000000006'),
('bbbbbbbb-0000-0000-0000-000000000007', 'Branch G', 'aaaaaaaa-0000-0000-0000-000000000007'),
('bbbbbbbb-0000-0000-0000-000000000008', 'Branch H', 'aaaaaaaa-0000-0000-0000-000000000008'),
('bbbbbbbb-0000-0000-0000-000000000009', 'Branch I', 'aaaaaaaa-0000-0000-0000-000000000009'),
('bbbbbbbb-0000-0000-0000-000000000010', 'Branch J', 'aaaaaaaa-0000-0000-0000-000000000010');

-- 23. BRANCH_INTAKES (depends on branches)
INSERT INTO "branch_intakes" ("branch_id", "year", "allowed_batch_size")
VALUES
('bbbbbbbb-0000-0000-0000-000000000001', 2021, 60),
('bbbbbbbb-0000-0000-0000-000000000002', 2021, 55),
('bbbbbbbb-0000-0000-0000-000000000003', 2021, 70),
('bbbbbbbb-0000-0000-0000-000000000004', 2022, 65),
('bbbbbbbb-0000-0000-0000-000000000005', 2022, 80),
('bbbbbbbb-0000-0000-0000-000000000006', 2023, 50),
('bbbbbbbb-0000-0000-0000-000000000007', 2023, 75),
('bbbbbbbb-0000-0000-0000-000000000008', 2024, 60),
('bbbbbbbb-0000-0000-0000-000000000009', 2024, 85),
('bbbbbbbb-0000-0000-0000-000000000010', 2025, 40);

-- 24. ORGANIZERS (no dependencies; type is COMMUNITY_TYPE)
INSERT INTO "organizers" ("id", "type", "name")
VALUES
('cccccccc-0000-0000-0000-000000000001', 'CLUBS', 'Science Club'),
('cccccccc-0000-0000-0000-000000000002', 'NGO', 'Youth Empowerment Org'),
('cccccccc-0000-0000-0000-000000000003', 'GOVERNMENT', 'City Council'),
('cccccccc-0000-0000-0000-000000000004', 'INDUSTRY', 'Tech Innovators Inc.'),
('cccccccc-0000-0000-0000-000000000005', 'CLUBS', 'Debate Club'),
('cccccccc-0000-0000-0000-000000000006', 'NGO', 'Green Earth'),
('cccccccc-0000-0000-0000-000000000007', 'GOVERNMENT', 'State Department'),
('cccccccc-0000-0000-0000-000000000008', 'INDUSTRY', 'Auto Makers Ltd.'),
('cccccccc-0000-0000-0000-000000000009', 'CLUBS', 'Art Club'),
('cccccccc-0000-0000-0000-000000000010', 'NGO', 'Community Helpers');

-- 25. SDG_GOALS (no dependencies)
INSERT INTO "sdg_goals" ("id", "number", "goal")
VALUES
('dddddddd-0000-0000-0000-000000000001', 1, 'No Poverty'),
('dddddddd-0000-0000-0000-000000000002', 2, 'Zero Hunger'),
('dddddddd-0000-0000-0000-000000000003', 3, 'Good Health and Well-being'),
('dddddddd-0000-0000-0000-000000000004', 4, 'Quality Education'),
('dddddddd-0000-0000-0000-000000000005', 5, 'Gender Equality'),
('dddddddd-0000-0000-0000-000000000006', 6, 'Clean Water and Sanitation'),
('dddddddd-0000-0000-0000-000000000007', 7, 'Affordable and Clean Energy'),
('dddddddd-0000-0000-0000-000000000008', 8, 'Decent Work and Economic Growth'),
('dddddddd-0000-0000-0000-000000000009', 9, 'Industry, Innovation and Infrastructure'),
('dddddddd-0000-0000-0000-000000000010', 10, 'Reduced Inequalities');

-- 26. EVENTS
INSERT INTO "events" ("id", "name", "date", "start_time", "end_time", "venue", "organizer_id", "level", "objective", "description", "sdg_goals")
VALUES
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE01', 'Tech Expo 2025', '2025-05-10 09:00:00', '2025-05-10 09:00:00', '2025-05-10 17:00:00', 'Main Convention Center', 'cccccccc-0000-0000-0000-000000000001', 'INTERNATIONAL', 'COMPETITIVE', 'Annual tech exhibition showcasing innovations', '{"dddddddd-0000-0000-0000-000000000001"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE02', 'Innovation Summit', '2025-06-15 10:00:00', '2025-06-15 10:00:00', '2025-06-15 16:00:00', 'City Hall', 'cccccccc-0000-0000-0000-000000000002', 'NATIONAL', 'INFORMATIONAL', 'A summit to discuss cutting-edge ideas', '{"dddddddd-0000-0000-0000-000000000002"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE03', 'Research Conference', '2025-07-20 08:30:00', '2025-07-20 08:30:00', '2025-07-20 15:30:00', 'University Auditorium', 'cccccccc-0000-0000-0000-000000000003', 'INTERNAL', 'COMPETITIVE', 'Conference on latest research trends', '{"dddddddd-0000-0000-0000-000000000003"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE04', 'Cultural Fest', '2025-08-05 11:00:00', '2025-08-05 11:00:00', '2025-08-05 19:00:00', 'Cultural Ground', 'cccccccc-0000-0000-0000-000000000004', 'STATE', 'INFORMATIONAL', 'A festival celebrating diverse cultures', '{"dddddddd-0000-0000-0000-000000000004"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE05', 'Startup Pitch', '2025-09-12 14:00:00', '2025-09-12 14:00:00', '2025-09-12 18:00:00', 'Innovation Hub', 'cccccccc-0000-0000-0000-000000000005', 'NATIONAL', 'COMPETITIVE', 'Pitching session for startups', '{"dddddddd-0000-0000-0000-000000000005"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE06', 'Health Symposium', '2025-10-01 09:30:00', '2025-10-01 09:30:00', '2025-10-01 17:30:00', 'Medical College Auditorium', 'cccccccc-0000-0000-0000-000000000006', 'INTERNATIONAL', 'INFORMATIONAL', 'Symposium focusing on healthcare innovations', '{"dddddddd-0000-0000-0000-000000000006"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE07', 'Data Science Workshop', '2025-11-05 10:15:00', '2025-11-05 10:15:00', '2025-11-05 15:15:00', 'Tech Park', 'cccccccc-0000-0000-0000-000000000007', 'STATE', 'COMPETITIVE', 'Hands-on workshop on data science', '{"dddddddd-0000-0000-0000-000000000007"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE08', 'Art & Design Exhibition', '2025-12-10 11:00:00', '2025-12-10 11:00:00', '2025-12-10 17:00:00', 'Art Gallery', 'cccccccc-0000-0000-0000-000000000008', 'INTERNAL', 'INFORMATIONAL', 'Exhibition of design and art projects', '{"dddddddd-0000-0000-0000-000000000008"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE09', 'Robotics Challenge', '2026-01-15 08:00:00', '2026-01-15 08:00:00', '2026-01-15 14:00:00', 'Robotics Lab', 'cccccccc-0000-0000-0000-000000000009', 'NATIONAL', 'COMPETITIVE', 'Competition among robotics teams', '{"dddddddd-0000-0000-0000-000000000009"}'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE10', 'Literary Meet', '2026-02-20 10:00:00', '2026-02-20 10:00:00', '2026-02-20 16:00:00', 'Community Hall', 'cccccccc-0000-0000-0000-000000000010', 'STATE', 'INFORMATIONAL', 'Literary discussion and book reviews', '{"dddddddd-0000-0000-0000-000000000010"}');

-- 27. EVENT_SDG_GOALS
INSERT INTO "event_sdg_goals" ("event_id", "sdg_goal_id")
VALUES
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE01', 'dddddddd-0000-0000-0000-000000000001'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE02', 'dddddddd-0000-0000-0000-000000000002'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE03', 'dddddddd-0000-0000-0000-000000000003'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE04', 'dddddddd-0000-0000-0000-000000000004'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE05', 'dddddddd-0000-0000-0000-000000000005'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE06', 'dddddddd-0000-0000-0000-000000000006'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE07', 'dddddddd-0000-0000-0000-000000000007'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE08', 'dddddddd-0000-0000-0000-000000000008'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE09', 'dddddddd-0000-0000-0000-000000000009'),
('EEEEEEEE-EEEE-EEEE-EEEE-EEEEEEEEEE10', 'dddddddd-0000-0000-0000-000000000010');

-- 28. COMPETITIVE_EVENTS
INSERT INTO "competitive_events" ("id", "classification", "type", "participant_id", "position", "award")
VALUES
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF01', 'INDIVIDUAL', 'SPORTS', '11111111-1111-1111-1111-111111111101', 1, 'Gold Medal'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF02', 'TEAM', 'CULTURAL', '11111111-1111-1111-1111-111111111102', 2, 'Silver Medal'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF03', 'INDIVIDUAL', 'ACADEMIC', '11111111-1111-1111-1111-111111111103', 3, 'Certificate of Excellence'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF04', 'TEAM', 'OTHER', '11111111-1111-1111-1111-111111111104', 1, 'Trophy'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF05', 'INDIVIDUAL', 'SPORTS', '11111111-1111-1111-1111-111111111105', 2, 'Medal'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF06', 'TEAM', 'CULTURAL', '11111111-1111-1111-1111-111111111106', 3, 'Plaque'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF07', 'INDIVIDUAL', 'ACADEMIC', '11111111-1111-1111-1111-111111111107', 4, 'Award'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF08', 'TEAM', 'OTHER', '11111111-1111-1111-1111-111111111108', 1, 'Honor'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF09', 'INDIVIDUAL', 'SPORTS', '11111111-1111-1111-1111-111111111109', 2, 'Gold Medal'),
('FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFF10', 'TEAM', 'CULTURAL', '11111111-1111-1111-1111-111111111110', 3, 'Silver Medal');

-- 29. INFORMATIONAL_EVENTS
INSERT INTO "informational_events" ("id", "speaker", "no_of_students", "no_of_teachers", "link_to_report", "geotagged_photographs")
VALUES
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG01', 'Dr. Smith', 100, 10, 'http://example.com/report1', '{"photo1.jpg", "photo2.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG02', 'Prof. Johnson', 150, 15, 'http://example.com/report2', '{"photo3.jpg", "photo4.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG03', 'Dr. Williams', 200, 20, 'http://example.com/report3', '{"photo5.jpg", "photo6.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG04', 'Dr. Brown', 120, 12, 'http://example.com/report4', '{"photo7.jpg", "photo8.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG05', 'Prof. Davis', 130, 13, 'http://example.com/report5', '{"photo9.jpg", "photo10.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG06', 'Dr. Miller', 110, 11, 'http://example.com/report6', '{"photo11.jpg", "photo12.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG07', 'Prof. Wilson', 140, 14, 'http://example.com/report7', '{"photo13.jpg", "photo14.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG08', 'Dr. Moore', 160, 16, 'http://example.com/report8', '{"photo15.jpg", "photo16.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG09', 'Dr. Taylor', 170, 17, 'http://example.com/report9', '{"photo17.jpg", "photo18.jpg"}'),
('GGGGGGGG-GGGG-GGGG-GGGG-GGGGGGGG10', 'Prof. Anderson', 180, 18, 'http://example.com/report10', '{"photo19.jpg", "photo20.jpg"}');

-- 30. GPA
INSERT INTO "GPA" ("student_id", "semester", "GPA", "credits")
VALUES
('11111111-1111-1111-1111-111111111101', 1, 8.50, 20),
('11111111-1111-1111-1111-111111111102', 1, 7.80, 18),
('11111111-1111-1111-1111-111111111103', 2, 8.20, 22),
('11111111-1111-1111-1111-111111111104', 2, 7.90, 19),
('11111111-1111-1111-1111-111111111105', 3, 8.70, 24),
('11111111-1111-1111-1111-111111111106', 3, 8.00, 21),
('11111111-1111-1111-1111-111111111107', 4, 7.50, 20),
('11111111-1111-1111-1111-111111111108', 4, 8.10, 23),
('11111111-1111-1111-1111-111111111109', 5, 8.30, 25),
('11111111-1111-1111-1111-111111111110', 5, 7.70, 19);
