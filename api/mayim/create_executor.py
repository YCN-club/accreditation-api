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
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_user(self, obj: T):
        """Create User"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_student(self, obj: T):
        """Create Student"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_sponsorship(self, obj: T):
        """Create Sponsorship"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_sdg_goal(self, obj: T):
        """Create SDG Goal"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_program(self, obj: T):
        """Create Program"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_program_intake(self, obj: T):
        """Create Program Intake"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_professional_community(self, obj: T):
        """Create Professional Community"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_other_academic_institute(self, obj: T):
        """Create Other Academic Institute"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_organizer(self, obj: T):
        """Create Organizer"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_national_government_exam(self, obj: T):
        """Create National Government Exam"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_login_data(self, obj: T):
        """Create Login Data"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_laboratory(self, obj: T):
        """Create Laboratory"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_laboratory_technical_manpower(self, obj: T):
        """Create Laboratory Technical Manpower"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_laboratories_technical_manpower(self, obj: T):
        """Create Laboratories Technical Manpower"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_journal(self, obj: T):
        """Create Journal"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_journal_publication(self, obj: T):
        """Create Journal Publication"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_journal_publication_author(self, obj: T):
        """Create Journal Publication Author"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_ipr(self, obj: T):
        """Create IPR"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_ipr_earning(self, obj: T):
        """Create IPR Earning"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_institute(self, obj: T):
        """Create Institute"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_institute_programs_offered(self, obj: T):
        """Create Institute Programs Offered"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_institute_programs_considered(self, obj: T):
        """Create Institute Programs Considered"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_institute_other_academic_institutes(self, obj: T):
        """Create Institute Other Academic Institutes"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_informational_event(self, obj: T):
        """Create Informational Event"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_gpa(self, obj: T):
        """Create GPA"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty(self, obj: T):
        """Create Faculty"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty_student_innovative_project(self, obj: T):
        """Create Faculty Student Innovative Project"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty_sponsored_research_project(self, obj: T):
        """Create Faculty Sponsored Research Project"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty_internship_training_collaboration(self, obj: T):
        """Create Faculty Internship Training Collaboration"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_faculty_course(self, obj: T):
        """Create Faculty Course"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_facility(self, obj: T):
        """Create Facility"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_event(self, obj: T):
        """Create Event"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_event_sdg_goal(self, obj: T):
        """Create Event SDG Goal"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_e_resource(self, obj: T):
        """Create E-Resource"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_department(self, obj: T):
        """Create Department"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_continuing_education_program(self, obj: T):
        """Create Continuing Education Program"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_competitive_event(self, obj: T):
        """Create Competitive Event"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_company(self, obj: T):
        """Create Company"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_collaborative_activity(self, obj: T):
        """Create Collaborative Activity"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_branch(self, obj: T):
        """Create Branch"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_branch_intake(self, obj: T):
        """Create Branch Intake"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_book_publication(self, obj: T):
        """Create Book Publication"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_book_publication_author(self, obj: T):
        """Create Book Publication Author"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_benefit_program(self, obj: T):
        """Create Benefit Program"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_award(self, obj: T):
        """Create Award"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_auth(self, obj: T):
        """Create Auth"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_agency(self, obj: T):
        """Create Agency"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_after_graduation(self, obj: T):
        """Create After Graduation"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_after_graduation_placement(self, obj: T):
        """Create After Graduation Placement"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_after_graduation_higher_study(self, obj: T):
        """Create After Graduation Higher Study"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )

    async def create_after_graduation_entrepreneurship(self, obj: T):
        """Create After Graduation Entrepreneurship"""
        return await self.execute(
            self.get_query(), allow_none=True, params=obj.to_dict()
        )
