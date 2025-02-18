from mayim import PostgresExecutor


class CreateExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/insert/"

    async def create_adjunct_faculty(self, faculty_id, hours_handled, subjects):
        """Create Adjunct Faculty"""

    async def create_user(self, id, first_name, middle_name, last_name, email):
        """Create User"""

    async def create_student(
        self,
        id,
        admission_no,
        registration_no,
        origin,
        gender,
        branch_id,
        batch_year,
        year_of_join,
        type_of_join,
        year_of_exit,
        type_of_exit,
        social_disadvantage,
        economic_disadvantage,
        physically_challenged,
    ):
        """Create Student"""

    async def create_sponsorship(
        self, id, agency_name, year, amount_inr, project_title
    ):
        """Create Sponsorship"""

    async def create_sdg_goal(self, id, number, goal):
        """Create SDG Goal"""

    async def create_program(
        self,
        id,
        program_code,
        duration_year,
        name,
        year_of_start,
        sanctioned_intake,
        aicte_approval_details,
        accreditation_status,
        number_of_times_accredited,
        institute_id,
    ):
        """Create Program"""

    async def create_program_intake(self, program_id, year, intake):
        """Create Program Intake"""

    async def create_professional_community(
        self, faculty_id, name_of_society, position
    ):
        """Create Professional Community"""

    async def create_other_academic_institute(
        self, id, name, year_of_establishment, program_of_study, location
    ):
        """Create Other Academic Institute"""

    async def create_organizer(self, id, type, name):
        """Create Organizer"""

    async def create_national_government_exam(self, id, student_id, exam_type):
        """Create National Government Exam"""

    async def create_login_data(
        self, user_id, name, email, employee_id, password, is_active, requires_reset
    ):
        """Create Login Data"""

    async def create_laboratory(
        self, id, batch_size, name_of_equipment, safety_measures, weekly_utilization
    ):
        """Create Laboratory"""

    async def create_laboratory_technical_manpower(
        self, laboratory_id, technical_manpower_id
    ):
        """Create Laboratory Technical Manpower"""

    async def create_laboratories_technical_manpower(
        self, id, name, designation, qualification
    ):
        """Create Laboratories Technical Manpower"""

    async def create_journal(self, id, name, frequency, type, scopus_indexed):
        """Create Journal"""

    async def create_journal_publication(
        self,
        id,
        journal_id,
        journal_volume_number,
        journal_issue_number,
        sponsor_id,
        year,
        semester,
        doi,
        title,
    ):
        """Create Journal Publication"""

    async def create_journal_publication_author(
        self, publication_id, author_id, author_index
    ):
        """Create Journal Publication Author"""

    async def create_ipr(
        self,
        id,
        awardee_id,
        awarder_name,
        government_recognized,
        year,
        uuid,
        title,
        type,
        status,
    ):
        """Create IPR"""

    async def create_ipr_earning(self, id, financial_year, amount_inr):
        """Create IPR Earning"""

    async def create_institute(
        self,
        id,
        institute_code,
        name,
        type,
        year_of_establishment,
        ownership_status,
        affiliating_university_name,
        affiliating_university_address,
        vision,
        mission,
        head_of_institute_id,
        nba_coordinator_id,
    ):
        """Create Institute"""

    async def create_institute_programs_offered(self, institute_id, program_id):
        """Create Institute Programs Offered"""

    async def create_institute_programs_considered(self, institute_id, program_id):
        """Create Institute Programs Considered"""

    async def create_institute_other_academic_institutes(
        self, institute_id, other_academic_institute_id
    ):
        """Create Institute Other Academic Institutes"""

    async def create_informational_event(
        self, id, speaker, no_of_students, no_of_teachers
    ):
        """Create Informational Event"""

    async def create_gpa(self, student_id, semester, gpa, credits):
        """Create GPA"""

    async def create_faculty(
        self,
        id,
        employee_id,
        department,
        designation,
        pan_no,
        apaar_id,
        highest_degree,
        university,
        area_of_specialization,
        date_of_join,
        designation_at_join,
        designated_as_professor,
        designated_as_associate_professor,
        designated_as_assistant_professor,
        nature_of_association,
        contractual_obligation,
        currently_associated,
        date_of_leave,
    ):
        """Create Faculty"""

    async def create_faculty_student_innovative_project(
        self, faculty_id, name_of_event, link_of_website
    ):
        """Create Faculty Student Innovative Project"""

    async def create_faculty_sponsored_research_project(
        self,
        faculty_id,
        name_of_principal_investigator,
        name_of_co_principal_investigator,
        department_id,
        project_title,
        name_of_funding_agency,
        duration_of_project,
        amount_inr,
        outcomes,
    ):
        """Create Faculty Sponsored Research Project"""

    async def create_faculty_internship_training_collaboration(
        self, faculty_id, name_of_itc, name_of_company, type, outcomes
    ):
        """Create Faculty Internship Training Collaboration"""

    async def create_faculty_course(self, faculty_id, name_of_course, developed):
        """Create Faculty Course"""

    async def create_facility(
        self, id, name, type, is_ict, details, reasons, utilization, relevance_to_pos
    ):
        """Create Facility"""

    async def create_event(
        self,
        id,
        name,
        date,
        start_time,
        end_time,
        venue,
        organizer_id,
        level,
        objective,
        description,
    ):
        """Create Event"""

    async def create_event_sdg_goal(self, event_id, sdg_goal_id):
        """Create Event SDG Goal"""

    async def create_e_resource(
        self,
        faculty_id,
        name,
        development_platform,
        date_of_launch,
        link_to_relevant_document,
        institute,
    ):
        """Create E-Resource"""

    async def create_department(self, id, name, program_id):
        """Create Department"""

    async def create_continuing_education_program(
        self, id, year, name, no_of_participants, no_of_days
    ):
        """Create Continuing Education Program"""

    async def create_competitive_event(
        self, id, classification, participant_id, position, award, type
    ):
        """Create Competitive Event"""

    async def create_company(self, id, name, contact_no, contact_email):
        """Create Company"""

    async def create_collaborative_activity(
        self,
        id,
        title,
        type,
        agency_id,
        user_id,
        source_of_financial_support,
        year,
        duration,
        link_to_relevant_documents,
    ):
        """Create Collaborative Activity"""

    async def create_branch(self, id, name, department_id):
        """Create Branch"""

    async def create_branch_intake(self, branch_id, year, allowed_batch_size):
        """Create Branch Intake"""

    async def create_book_publication(self, id, year, semester, title, isbn, type):
        """Create Book Publication"""

    async def create_book_publication_author(
        self, publication_id, author_id, author_index
    ):
        """Create Book Publication Author"""

    async def create_benefit_program(self, id, student_id, year, type):
        """Create Benefit Program"""

    async def create_award(
        self, id, name, type, awarding_agency, user_type, user_id, year
    ):
        """Create Award"""

    async def create_auth(self, id, password, last_login, requires_reset):
        """Create Auth"""

    async def create_agency(self, id, name, contact_no, contact_email):
        """Create Agency"""

    async def create_after_graduation(self, id, student_id, year, type):
        """Create After Graduation"""

    async def create_after_graduation_placement(
        self, after_graduation_id, employer_id, salary
    ):
        """Create After Graduation Placement"""

    async def create_after_graduation_higher_study(
        self, after_graduation_id, institute_name, program_name, with_exam
    ):
        """Create After Graduation Higher Study"""

    async def create_after_graduation_entrepreneurship(
        self, after_graduation_id, company_name
    ):
        """Create After Graduation Entrepreneurship"""
