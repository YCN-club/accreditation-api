from uuid import UUID
from mayim import PostgresExecutor


class DeleteExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/delete/"

    async def delete_adjunct_faculty(self, adjunct_faculty_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_after_graduation_entrepreneurship(
        self, after_graduation_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_after_graduation_higher_studies(
        self, after_graduation_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_after_graduation_placements(
        self, after_graduation_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_after_graduation(self, after_graduation_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_agencies(self, agency_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_auth(self, auth_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_awards(self, award_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_benefit_programs(self, benefit_programs_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_book_publication_author(
        self, publication_id: UUID, author_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_book_publication(self, publication_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_branch_intake(self, branch_id: UUID, year: int) -> None:
        """Delete Resource by ID"""

    async def delete_branches(self, branch_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_collaborative_activities(
        self, collaborative_activity_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_companies(self, company_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_competetive_event(self, competitive_event_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_continuining_education_programs(
        self, continuing_education_programs_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_departments(self, department_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_e_resources(self, e_resources_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_events(self, event_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_facilities(self, facility_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_faculty_courses(
        self, faculty_id: UUID, name_of_course: str
    ) -> None:
        """Delete Resource by ID"""

    async def delete_faculty_internship_training_collaboration(
        self, faculty_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_faculty_sponsored_research_projects_consultancy_work_institute_seed_money(
        self, faculty_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_faculty_student_innovative_projects(
        self, faculty_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_faculty(self, faculty_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_gpa(self, faculty_id: UUID, semester: int) -> None:
        """Delete Resource by ID"""

    async def delete_informational_event(self, informational_event_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_institute(self, institute_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_ipr_earning(self, ipr_earning_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_ipr(self, ipr_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_journal_publication_author(
        self, publication_id: UUID, author_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_journal_publication(self, journal_publication_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_journal(self, journal_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_laboratories_technical_manpower(
        self, laboratories_technical_manpower_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_laboratories(self, laboratory_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_login_data(self, user_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_national_government_exams(
        self, national_government_exams_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_organizer(self, organizer_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_other_academic_institutes_run_by_trust_society(
        self, other_academic_institutes_run_by_trust_society_id: UUID
    ) -> None:
        """Delete Resource by ID"""

    async def delete_professional_communities(
        self, faculty_id: UUID, name_of_society: str
    ) -> None:
        """Delete Resource by ID"""

    async def delete_program_intakes(self, program_id: UUID, year: int) -> None:
        """Delete Resource by ID"""

    async def delete_program(self, program_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_sdg_goal(self, sdg_goal_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_sponsorship(self, sponsorship_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_student(self, student_id: UUID) -> None:
        """Delete Resource by ID"""

    async def delete_user(self, user_id: UUID) -> None:
        """Delete Resource by ID"""
