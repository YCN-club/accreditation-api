-- 31. FACULTY_COURSES
INSERT INTO "faculty_courses" ("faculty_id", "name_of_course", "developed")
VALUES
('11111111-1111-1111-1111-111111111101', 'Introduction to Computer Science', true),
('11111111-1111-1111-1111-111111111102', 'Advanced Mathematics', false),
('11111111-1111-1111-1111-111111111103', 'Physics I', true),
('11111111-1111-1111-1111-111111111104', 'Chemistry Basics', false),
('11111111-1111-1111-1111-111111111105', 'Engineering Mechanics', true),
('11111111-1111-1111-1111-111111111106', 'Software Engineering', true),
('11111111-1111-1111-1111-111111111107', 'Data Structures', false),
('11111111-1111-1111-1111-111111111108', 'Algorithms', true),
('11111111-1111-1111-1111-111111111109', 'Operating Systems', false),
('11111111-1111-1111-1111-111111111110', 'Database Systems', true);

-- 32. FACULTY_STUDENT_INNOVATIVE_PROJECTS
INSERT INTO "faculty_student_innovative_projects" ("faculty_id", "name_of_event", "link_of_website")
VALUES
('11111111-1111-1111-1111-111111111101', 'Innovate 2025', 'http://example.com/innovate2025'),
('11111111-1111-1111-1111-111111111102', 'Tech Fair', 'http://example.com/techfair'),
('11111111-1111-1111-1111-111111111103', 'Robotics Expo', 'http://example.com/robotics'),
('11111111-1111-1111-1111-111111111104', 'Coding Hackathon', 'http://example.com/hackathon'),
('11111111-1111-1111-1111-111111111105', 'AI Summit', 'http://example.com/aisummit'),
('11111111-1111-1111-1111-111111111106', 'Data Science Challenge', 'http://example.com/dschallenge'),
('11111111-1111-1111-1111-111111111107', 'Design Marathon', 'http://example.com/designmarathon'),
('11111111-1111-1111-1111-111111111108', 'Innovation Week', 'http://example.com/innovationweek'),
('11111111-1111-1111-1111-111111111109', 'Research Conclave', 'http://example.com/researchconclave'),
('11111111-1111-1111-1111-111111111110', 'Startup Garage', 'http://example.com/startupgarage');

-- 33. FACULTY_INTERNSHIP_TRAINING_COLLABORATION
INSERT INTO "faculty_internship_training_collaboration" ("faculty_id", "name_of_itc", "name_of_company", "type", "outcomes")
VALUES
('11111111-1111-1111-1111-111111111101', 'Internship Program A', 'Company A', 'INTERNSHIP', 'Interns gained practical skills'),
('11111111-1111-1111-1111-111111111102', 'Training Session B', 'Company B', 'TRAINING', 'Participants received training certificates'),
('11111111-1111-1111-1111-111111111103', 'Collaboration Project C', 'Company C', 'COLLABORATION', 'Joint research project outcome'),
('11111111-1111-1111-1111-111111111104', 'Internship Program D', 'Company D', 'INTERNSHIP', 'Enhanced industry exposure'),
('11111111-1111-1111-1111-111111111105', 'Training Workshop E', 'Company E', 'TRAINING', 'Improved technical skills'),
('11111111-1111-1111-1111-111111111106', 'Collaboration Initiative F', 'Company F', 'COLLABORATION', 'Developed innovative solutions'),
('11111111-1111-1111-1111-111111111107', 'Internship Program G', 'Company G', 'INTERNSHIP', 'Hands-on project experience'),
('11111111-1111-1111-1111-111111111108', 'Training Session H', 'Company H', 'TRAINING', 'Enhanced soft skills'),
('11111111-1111-1111-1111-111111111109', 'Collaboration Project I', 'Company I', 'COLLABORATION', 'Successful joint venture'),
('11111111-1111-1111-1111-111111111110', 'Internship Program J', 'Company J', 'INTERNSHIP', 'Valuable industry exposure');

-- 34. FACULTY_SPONSORED_RESEARCH_PROJECTS_CONSULTANCY_WORK_INSTITUTE_SEED_MONEY
INSERT INTO "faculty_sponsored_research_projects_consultancy_work_institute_seed_money"
("type", "name_of_principal_investigator", "name_of_co_principal_investigator", "department_id", "project_title", "name_of_funding_agency", "duration_of_project", "amount_inr", "outcomes")
VALUES
('SPONSORED_RESEARCH_PROJECT', 'Dr. Alpha', 'Dr. Beta', 'aaaaaaaa-0000-0000-0000-000000000001', 'Project Quantum', 'Funding Org A', '2 years', 500000, 'Breakthrough in quantum computing'),
('CONSULTANCY_WORK', 'Dr. Gamma', 'Dr. Delta', 'aaaaaaaa-0000-0000-0000-000000000002', 'Project Delta', 'Consultancy Inc.', '1 year', 300000, 'Enhanced process efficiency'),
('INSTITUTE_SEED_MONEY', 'Dr. Epsilon', 'Dr. Zeta', 'aaaaaaaa-0000-0000-0000-000000000003', 'Project Zeta', 'Seed Fund Corp.', '18 months', 250000, 'Pilot project success'),
('SPONSORED_RESEARCH_PROJECT', 'Dr. Eta', 'Dr. Theta', 'aaaaaaaa-0000-0000-0000-000000000004', 'Project Theta', 'Fund Agency', '2 years', 600000, 'Novel research findings'),
('CONSULTANCY_WORK', 'Dr. Iota', 'Dr. Kappa', 'aaaaaaaa-0000-0000-0000-000000000005', 'Project Kappa', 'Consultancy Experts', '1.5 years', 350000, 'Improved system design'),
('INSTITUTE_SEED_MONEY', 'Dr. Lambda', 'Dr. Mu', 'aaaaaaaa-0000-0000-0000-000000000006', 'Project Mu', 'Seed Money Org', '2 years', 400000, 'Successful prototype development'),
('SPONSORED_RESEARCH_PROJECT', 'Dr. Nu', 'Dr. Xi', 'aaaaaaaa-0000-0000-0000-000000000007', 'Project Xi', 'Research Fund X', '3 years', 750000, 'Advanced research outcomes'),
('CONSULTANCY_WORK', 'Dr. Omicron', 'Dr. Pi', 'aaaaaaaa-0000-0000-0000-000000000008', 'Project Pi', 'Consultancy Group', '1 year', 200000, 'Operational improvements'),
('INSTITUTE_SEED_MONEY', 'Dr. Rho', 'Dr. Sigma', 'aaaaaaaa-0000-0000-0000-000000000009', 'Project Sigma', 'Seed Money Group', '2.5 years', 800000, 'Innovative technology development'),
('SPONSORED_RESEARCH_PROJECT', 'Dr. Tau', 'Dr. Upsilon', 'aaaaaaaa-0000-0000-0000-000000000010', 'Project Upsilon', 'Funding Agency B', '2 years', 550000, 'Significant research impact');

-- 35. ADJUNCT_FACULTY
INSERT INTO "adjunct_faculty" ("faculty_id", "hours_handled", "subjects")
VALUES
('11111111-1111-1111-1111-111111111101', 10, '{"Mathematics", "Physics"}'),
('11111111-1111-1111-1111-111111111102', 12, '{"Chemistry"}'),
('11111111-1111-1111-1111-111111111103', 8, '{"Biology", "Environmental Science"}'),
('11111111-1111-1111-1111-111111111104', 15, '{"Computer Science", "Data Structures"}'),
('11111111-1111-1111-1111-111111111105', 9, '{"History", "Social Studies"}'),
('11111111-1111-1111-1111-111111111106', 11, '{"Economics", "Statistics"}'),
('11111111-1111-1111-1111-111111111107', 10, '{"Philosophy"}'),
('11111111-1111-1111-1111-111111111108', 14, '{"Political Science", "Law"}'),
('11111111-1111-1111-1111-111111111109', 7, '{"Sociology"}'),
('11111111-1111-1111-1111-111111111110', 13, '{"Psychology", "Management"}');

-- 36. STUDENTS
INSERT INTO "students" 
("id", "admission_no", "registration_no", "origin", "gender", "branch_id", "batch_year", "year_of_join", "type_of_join", "year_of_exit", "type_of_exit", "social_disadvantage", "economic_disadvantage", "physically_challenged")
VALUES
('S0000000-0000-0000-0000-000000000001', 'ADM2025001', 'REG2025001', 'IN_STATE', 'FEMALE', 'bbbbbbbb-0000-0000-0000-000000000001', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'SC', false, false),
('S0000000-0000-0000-0000-000000000002', 'ADM2025002', 'REG2025002', 'INTERNATIONAL', 'MALE', 'bbbbbbbb-0000-0000-0000-000000000002', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'OBC', false, false),
('S0000000-0000-0000-0000-000000000003', 'ADM2025003', 'REG2025003', 'IN_STATE', 'FEMALE', 'bbbbbbbb-0000-0000-0000-000000000003', 2025, 2025, 'OTHER', 2028, 'LEFT', 'SC', true, false),
('S0000000-0000-0000-0000-000000000004', 'ADM2025004', 'REG2025004', 'INTERNATIONAL', 'MALE', 'bbbbbbbb-0000-0000-0000-000000000004', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'OBC', false, true),
('S0000000-0000-0000-0000-000000000005', 'ADM2025005', 'REG2025005', 'IN_STATE', 'FEMALE', 'bbbbbbbb-0000-0000-0000-000000000005', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'SC', false, false),
('S0000000-0000-0000-0000-000000000006', 'ADM2025006', 'REG2025006', 'INTERNATIONAL', 'MALE', 'bbbbbbbb-0000-0000-0000-000000000006', 2025, 2025, 'OTHER', 2028, 'LEFT', 'OBC', true, false),
('S0000000-0000-0000-0000-000000000007', 'ADM2025007', 'REG2025007', 'IN_STATE', 'FEMALE', 'bbbbbbbb-0000-0000-0000-000000000007', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'SC', false, false),
('S0000000-0000-0000-0000-000000000008', 'ADM2025008', 'REG2025008', 'INTERNATIONAL', 'MALE', 'bbbbbbbb-0000-0000-0000-000000000008', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'OBC', false, false),
('S0000000-0000-0000-0000-000000000009', 'ADM2025009', 'REG2025009', 'IN_STATE', 'FEMALE', 'bbbbbbbb-0000-0000-0000-000000000009', 2025, 2025, 'OTHER', 2028, 'LEFT', 'SC', true, true),
('S0000000-0000-0000-0000-000000000010', 'ADM2025010', 'REG2025010', 'INTERNATIONAL', 'MALE', 'bbbbbbbb-0000-0000-0000-000000000010', 2025, 2025, 'REGULAR', 2029, 'REGULAR', 'OBC', false, false);

-- 37. FACULTY
INSERT INTO "faculty" 
("id", "employee_id", "department_id", "designation", "pan_no", "apaar_id", "highest_degree", "university", "area_of_specialization", "date_of_join", "designation_at_join", "designated_as_professor", "designated_as_associate_professor", "designated_as_assistant_professor", "nature_of_association", "contractual_obligation", "currently_associated", "date_of_leave")
VALUES
('F0000000-0000-0000-0000-000000000001', 'EMP1001', 'aaaaaaaa-0000-0000-0000-000000000001', 'Assistant Professor', 'PAN001', 'AP001', 'DOCTORAL', 'Univ A', 'Computer Science', '2020-07-01', 'Lecturer', '2023-01-01', '2021-06-01', '2020-09-01', 'REGULAR', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000002', 'EMP1002', 'aaaaaaaa-0000-0000-0000-000000000002', 'Associate Professor', 'PAN002', 'AP002', 'ASSOCIATE', 'Univ B', 'Mechanical Engineering', '2019-08-15', 'Senior Lecturer', '2022-02-01', '2020-05-01', '2019-10-01', 'AD_HOC', 'PART_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000003', 'EMP1003', 'aaaaaaaa-0000-0000-0000-000000000003', 'Professor', 'PAN003', 'AP003', 'DOCTORAL', 'Univ C', 'Business Administration', '2018-09-10', 'Assistant Professor', '2021-03-01', '2020-04-01', '2018-11-01', 'REGULAR', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000004', 'EMP1004', 'aaaaaaaa-0000-0000-0000-000000000004', 'Assistant Professor', 'PAN004', 'AP004', 'ASSOCIATE', 'Univ D', 'Electrical Engineering', '2021-01-20', 'Lecturer', '2023-05-01', '2021-08-01', '2021-01-20', 'REGULAR', 'PART_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000005', 'EMP1005', 'aaaaaaaa-0000-0000-0000-000000000005', 'Associate Professor', 'PAN005', 'AP005', 'DOCTORAL', 'Univ E', 'Civil Engineering', '2017-06-30', 'Assistant Professor', '2022-07-01', '2020-03-01', '2017-06-30', 'REGULAR', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000006', 'EMP1006', 'aaaaaaaa-0000-0000-0000-000000000006', 'Professor', 'PAN006', 'AP006', 'DOCTORAL', 'Univ F', 'Information Technology', '2016-05-10', 'Lecturer', '2022-01-01', '2020-11-01', '2016-05-10', 'AD_HOC', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000007', 'EMP1007', 'aaaaaaaa-0000-0000-0000-000000000007', 'Assistant Professor', 'PAN007', 'AP007', 'ASSOCIATE', 'Univ G', 'Design', '2020-03-05', 'Instructor', '2023-02-01', '2021-01-15', '2020-03-05', 'REGULAR', 'PART_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000008', 'EMP1008', 'aaaaaaaa-0000-0000-0000-000000000008', 'Associate Professor', 'PAN008', 'AP008', 'DOCTORAL', 'Univ H', 'Chemical Engineering', '2019-12-01', 'Lecturer', '2022-10-01', '2020-08-01', '2019-12-01', 'AD_HOC', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000009', 'EMP1009', 'aaaaaaaa-0000-0000-0000-000000000009', 'Professor', 'PAN009', 'AP009', 'DOCTORAL', 'Univ I', 'Electronics Engineering', '2015-11-11', 'Assistant Professor', '2021-09-01', '2018-12-01', '2015-11-11', 'REGULAR', 'FULL_TIME', true, '9999-12-31'),
('F0000000-0000-0000-0000-000000000010', 'EMP1010', 'aaaaaaaa-0000-0000-0000-000000000010', 'Assistant Professor', 'PAN010', 'AP010', 'ASSOCIATE', 'Univ J', 'Automation', '2021-04-01', 'Lecturer', '2023-07-01', '2021-09-01', '2021-04-01', 'REGULAR', 'PART_TIME', true, '9999-12-31');

-- 38. PROFESSIONAL_COMMUNITIES
-- Assumed columns: "id", "name", "description"
INSERT INTO "professional_communities" ("id", "name", "description")
VALUES
('PC000000-0000-0000-0000-000000000001', 'IEEE', 'Institute of Electrical and Electronics Engineers'),
('PC000000-0000-0000-0000-000000000002', 'ACM', 'Association for Computing Machinery'),
('PC000000-0000-0000-0000-000000000003', 'ASME', 'American Society of Mechanical Engineers'),
('PC000000-0000-0000-0000-000000000004', 'AIChE', 'American Institute of Chemical Engineers'),
('PC000000-0000-0000-0000-000000000005', 'NAFSA', 'Association of International Educators'),
('PC000000-0000-0000-0000-000000000006', 'NACE', 'National Association of Colleges and Employers'),
('PC000000-0000-0000-0000-000000000007', 'SII', 'Society of Indian Industrialists'),
('PC000000-0000-0000-0000-000000000008', 'ISM', 'International Society of Magicians'),
('PC000000-0000-0000-0000-000000000009', 'SEMI', 'Semiconductor Equipment and Materials International'),
('PC000000-0000-0000-0000-000000000010', 'SPIE', 'International Society for Optics and Photonics');

-- 39. CONTINUING_EDUCATION_PROGRAMS
-- Assumed columns: "id", "program_name", "duration", "provider", "start_date"
INSERT INTO "continuing_education_programs" ("id", "program_name", "duration", "provider", "start_date")
VALUES
('CEP000000-0000-0000-0000-000000000001', 'Data Analytics Bootcamp', '3 months', 'Tech Institute', '2025-03-01'),
('CEP000000-0000-0000-0000-000000000002', 'AI and ML Workshop', '1 month', 'Innovate Academy', '2025-04-15'),
('CEP000000-0000-0000-0000-000000000003', 'Cybersecurity Essentials', '2 months', 'SecureTech', '2025-05-05'),
('CEP000000-0000-0000-0000-000000000004', 'Cloud Computing Fundamentals', '1 month', 'CloudPro', '2025-06-10'),
('CEP000000-0000-0000-0000-000000000005', 'Digital Marketing Course', '2 months', 'MarketMinds', '2025-07-01'),
('CEP000000-0000-0000-0000-000000000006', 'Project Management', '3 months', 'PMI Institute', '2025-08-20'),
('CEP000000-0000-0000-0000-000000000007', 'Entrepreneurship 101', '1.5 months', 'Startup Hub', '2025-09-15'),
('CEP000000-0000-0000-0000-000000000008', 'Advanced Excel', '1 month', 'OfficePro', '2025-10-05'),
('CEP000000-0000-0000-0000-000000000009', 'Blockchain Basics', '2 months', 'CryptoEd', '2025-11-01'),
('CEP000000-0000-0000-0000-000000000010', 'Soft Skills Development', '1 month', 'SkillUp', '2025-12-01');

-- 40. COLLABORATIVE_ACTIVITIES
-- Assumed columns: "id", "activity_type" (enum: 'RESEARCH' or 'INDUSTRY_INTERNSHIP'), "description", "agency_id", "user_id"
INSERT INTO "collaborative_activities" ("id", "activity_type", "description", "agency_id", "user_id")
VALUES
('CA000000-0000-0000-0000-000000000001', 'RESEARCH', 'Joint research project on AI ethics', '33333333-3333-3333-3333-333333333301', '11111111-1111-1111-1111-111111111101'),
('CA000000-0000-0000-0000-000000000002', 'INDUSTRY_INTERNSHIP', 'Internship collaboration with Tech Corp', '33333333-3333-3333-3333-333333333302', '11111111-1111-1111-1111-111111111102'),
('CA000000-0000-0000-0000-000000000003', 'RESEARCH', 'Research on renewable energy solutions', '33333333-3333-3333-3333-333333333303', '11111111-1111-1111-1111-111111111103'),
('CA000000-0000-0000-0000-000000000004', 'INDUSTRY_INTERNSHIP', 'Internship program in automotive innovation', '33333333-3333-3333-3333-333333333304', '11111111-1111-1111-1111-111111111104'),
('CA000000-0000-0000-0000-000000000005', 'RESEARCH', 'Collaboration on sustainable agriculture techniques', '33333333-3333-3333-3333-333333333305', '11111111-1111-1111-1111-111111111105'),
('CA000000-0000-0000-0000-000000000006', 'INDUSTRY_INTERNSHIP', 'Industry internship in semiconductor fabrication', '33333333-3333-3333-3333-333333333306', '11111111-1111-1111-1111-111111111106'),
('CA000000-0000-0000-0000-000000000007', 'RESEARCH', 'Joint project on biotechnology advancements', '33333333-3333-3333-3333-333333333307', '11111111-1111-1111-1111-111111111107'),
('CA000000-0000-0000-0000-000000000008', 'INDUSTRY_INTERNSHIP', 'Internship in financial technology solutions', '33333333-3333-3333-3333-333333333308', '11111111-1111-1111-1111-111111111108'),
('CA000000-0000-0000-0000-000000000009', 'RESEARCH', 'Research on smart city innovations', '33333333-3333-3333-3333-333333333309', '11111111-1111-1111-1111-111111111109'),
('CA000000-0000-0000-0000-000000000010', 'INDUSTRY_INTERNSHIP', 'Internship program in renewable energy', '33333333-3333-3333-3333-333333333310', '11111111-1111-1111-1111-111111111110');
