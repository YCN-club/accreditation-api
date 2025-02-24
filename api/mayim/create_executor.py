from typing import TypeVar
from mayim import PostgresExecutor

from api.models.generic_protocol import GenericProtocol

T = TypeVar("T", bound=GenericProtocol)


class CreateExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/input/"

    async def create_adjunct_faculty(self, obj: T):
        """Create Adjunct Faculty"""
        return await self.execute(
            self.get_query("create_adjunct_faculty"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_after_graduation(self, obj: T):
        """Create After Graduation"""
        return await self.execute(
            self.get_query("create_after_graduation"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_after_graduation_placements(self, obj: T):
        """Create After Graduation Placement"""
        return await self.execute(
            self.get_query("create_after_graduation_placements"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_after_graduation_higher_studies(self, obj: T):
        """Create After Graduation Higher Study"""
        return await self.execute(
            self.get_query("create_after_graduation_higher_studies"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_after_graduation_entrepreneurship(self, obj: T):
        """Create After Graduation Entrepreneurship"""
        return await self.execute(
            self.get_query("create_after_graduation_entrepreneurship"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_agencies(self, obj: T):
        """Create Agency"""
        return await self.execute(
            self.get_query("create_agencies"), allow_none=True, params=obj.to_dict()
        )

    async def create_auth(self, obj: T):
        """Create Auth"""
        return await self.execute(
            self.get_query("create_auth"), allow_none=True, params=obj.to_dict()
        )

    async def create_awards(self, obj: T):
        """Create Award"""
        return await self.execute(
            self.get_query("create_awards"), allow_none=True, params=obj.to_dict()
        )

    async def create_benefit_programs(self, obj: T):
        """Create Benefit Program"""
        return await self.execute(
            self.get_query("create_benefit_programs"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_book_publications(self, obj: T):
        """Create Book Publication"""
        return await self.execute(
            self.get_query("create_book_publications"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_book_publication_author(self, obj: T):
        """Create Book Publication Author"""
        return await self.execute(
            self.get_query("create_book_publication_author"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_branches(self, obj: T):
        """Create Branch"""
        return await self.execute(
            self.get_query("create_branches"), allow_none=True, params=obj.to_dict()
        )

    async def create_branch_intakes(self, obj: T):
        """Create Branch Intake"""
        return await self.execute(
            self.get_query("create_branch_intakes"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_collaborative_activities(self, obj: T):
        """Create Collaborative Activity"""
        return await self.execute(
            self.get_query("create_collaborative_activities"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_companies(self, obj: T):
        """Create Company"""
        return await self.execute(
            self.get_query("create_companies"), allow_none=True, params=obj.to_dict()
        )

    async def create_competitive_events(self, obj: T):
        """Create Competitive Event"""
        return await self.execute(
            self.get_query("create_competitive_events"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_continuing_education_programs(self, obj: T):
        """Create Continuing Education Program"""
        return await self.execute(
            self.get_query("create_continuing_education_programs"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_departments(self, obj: T):
        """Create Department"""
        return await self.execute(
            self.get_query("create_departments"), allow_none=True, params=obj.to_dict()
        )

    async def create_e_resources(self, obj: T):
        """Create E-Resource"""
        return await self.execute(
            self.get_query("create_e_resources"), allow_none=True, params=obj.to_dict()
        )

    async def create_event_sdg_goals(self, obj: T):
        """Create Event SDG Goal"""
        return await self.execute(
            self.get_query("create_event_sdg_goals"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_events(self, obj: T):
        """Create Event"""
        return await self.execute(
            self.get_query("create_events"), allow_none=True, params=obj.to_dict()
        )

    async def create_facilities(self, obj: T):
        """Create Facility"""
        return await self.execute(
            self.get_query("create_facilities"), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty_courses(self, obj: T):
        """Create Faculty Course"""
        return await self.execute(
            self.get_query("create_faculty_courses"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_faculty_internship_training_collaboration(self, obj: T):
        """Create Faculty Internship Training Collaboration"""
        return await self.execute(
            self.get_query("create_faculty_internship_training_collaboration"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_faculty_sponsored_research_projects_consultancy_work_institute_work_institute_seed_money(
        self, obj: T
    ):
        """Create Faculty Sponsored Research Project"""
        return await self.execute(
            self.get_query(
                "create_faculty_sponsored_research_projects_consultancy_work_institute_work_institute_seed_money"  # noqa: E501
            ),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_faculty_student_innovative_projects(self, obj: T):
        """Create Faculty Student Innovative Project"""
        return await self.execute(
            self.get_query("create_faculty_student_innovative_projects"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_faculty(self, obj: T):
        """Create Faculty"""
        return await self.execute(
            self.get_query("create_faculty"), allow_none=True, params=obj.to_dict()
        )

    async def create_gpa(self, obj: T):
        """Create GPA"""
        return await self.execute(
            self.get_query("create_gpa"), allow_none=True, params=obj.to_dict()
        )

    async def create_informational_events(self, obj: T):
        """Create Informational Event"""
        return await self.execute(
            self.get_query("create_informational_events"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_institute_programs_offered(self, obj: T):
        """Create Institute Programs Offered"""
        return await self.execute(
            self.get_query("create_institute_programs_offered"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_institute_programs_considered(self, obj: T):
        """Create Institute Programs Considered"""
        return await self.execute(
            self.get_query("create_institute_programs_considered"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_institute_other_academic_institutes(self, obj: T):
        """Create Institute Other Academic Institutes"""
        return await self.execute(
            self.get_query("create_institute_other_academic_institutes"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_institutes(self, obj: T):
        """Create Institute"""
        return await self.execute(
            self.get_query("create_institutes"), allow_none=True, params=obj.to_dict()
        )

    async def create_ipr_earnings(self, obj: T):
        """Create IPR Earning"""
        return await self.execute(
            self.get_query("create_ipr_earnings"), allow_none=True, params=obj.to_dict()
        )

    async def create_ipr(self, obj: T):
        """Create IPR"""
        return await self.execute(
            self.get_query("create_ipr"), allow_none=True, params=obj.to_dict()
        )

    async def create_journal_publication_author(self, obj: T):
        """Create Journal Publication Author"""
        return await self.execute(
            self.get_query("create_journal_publication_author"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_journal_publications(self, obj: T):
        """Create Journal Publication"""
        return await self.execute(
            self.get_query("create_journal_publications"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_journals(self, obj: T):
        """Create Journal"""
        return await self.execute(
            self.get_query("create_journals"), allow_none=True, params=obj.to_dict()
        )

    async def create_laboratory_technical_manpower(self, obj: T):
        """Create Laboratory Technical Manpower"""
        return await self.execute(
            self.get_query("create_laboratory_technical_manpower"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_laboratories_technical_manpower(self, obj: T):
        """Create Laboratories Technical Manpower"""
        return await self.execute(
            self.get_query("create_laboratories_technical_manpower"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_national_government_exams(self, obj: T):
        """Create National Government Exam"""
        return await self.execute(
            self.get_query("create_national_government_exams"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_organizers(self, obj: T):
        """Create Organizer"""
        return await self.execute(
            self.get_query("create_organizers"), allow_none=True, params=obj.to_dict()
        )

    async def create_other_academic_institutes_run_by_society(self, obj: T):
        """Create Other Academic Institute"""
        return await self.execute(
            self.get_query("create_other_academic_institutes_run_by_society"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_professional_communities(self, obj: T):
        """Create Professional Community"""
        return await self.execute(
            self.get_query("create_professional_communities"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_program_intakes(self, obj: T):
        """Create Program Intake"""
        return await self.execute(
            self.get_query("create_program_intakes"),
            allow_none=True,
            params=obj.to_dict(),
        )

    async def create_programs(self, obj: T):
        """Create Program"""
        return await self.execute(
            self.get_query("create_programs"), allow_none=True, params=obj.to_dict()
        )

    async def create_sdg_goals(self, obj: T):
        """Create SDG Goal"""
        return await self.execute(
            self.get_query("create_sdg_goals"), allow_none=True, params=obj.to_dict()
        )

    async def create_sponsorships(self, obj: T):
        """Create Sponsorship"""
        return await self.execute(
            self.get_query("create_sponsorships"), allow_none=True, params=obj.to_dict()
        )

    async def create_students(self, obj: T):
        """Create Student"""
        return await self.execute(
            self.get_query("create_students"), allow_none=True, params=obj.to_dict()
        )

    async def create_user(self, obj: T):
        """Create User"""
        return await self.execute(
            self.get_query("create_user"), allow_none=True, params=obj.to_dict()
        )

    async def create_login_data(self, obj: T):
        """Create Login Data"""
        return await self.execute(
            self.get_query("create_login_data"), allow_none=True, params=obj.to_dict()
        )
