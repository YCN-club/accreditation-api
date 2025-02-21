from mayim import PostgresExecutor

from api.models.db.adjunct_faculty import AdjunctFaculty
from api.models.db.after_graduation_entrepreneurship import (
    AfterGraduationEntrepreneurship,
)
from api.models.db.after_graduation_higher_studies import AfterGraduationHigherStudies
from api.models.db.after_graduation_placements import AfterGraduationPlacements
from api.models.db.after_graduation import AfterGraduation
from api.models.db.agencies import Agencies
from api.models.db.auth import Auth
from api.models.db.awards import Awards
from api.models.db.benefit_programs import BenefitPrograms
from api.models.db.book_publication_author import BookPublicationAuthor
from api.models.db.book_publication import BookPublication
from api.models.db.branch_intake import BranchIntake
from api.models.db.branches import Branches
from api.models.db.collaborative_activities import CollaborativeActivity
from api.models.db.companies import Companies
from api.models.db.competitive_event import CompetitiveEvent
from api.models.db.continuing_education_programs import ContinuingEducationPrograms
from api.models.db.departments import Departments
from api.models.db.e_resources import EResources
from api.models.db.event import Event
from api.models.db.facilities import Facilities
from api.models.db.faculty_courses import FacultyCourses
from api.models.db.faculty_internship_training_collaboration import (
    FacultyInternshipTrainingCollaboration,
)
from api.models.db.faculty_sponsored_research_projects_consultancy_work_institute_seed_money import (
    FacultySponsoredResearchProjectsConsultancyWorkInstituteSeedMoney,
)
from api.models.db.faculty_student_innovative_projects import (
    FacultyStudentInnovativeProjects,
)
from api.models.db.faculty import Faculty
from api.models.db.gpa import GPA
from api.models.db.informational_event import InformationalEvent
from api.models.db.institute import Institute
from api.models.db.ipr_earning import IprEarnings
from api.models.db.ipr import Ipr
from api.models.db.journal_publication_author import JournalPublicationAuthor
from api.models.db.journal_publication import JournalPublication
from api.models.db.journal import Journal
from api.models.db.laboratories_technical_manpower import LaboratoriesTechnicalManpower
from api.models.db.laboratories import Laboratories
from api.models.db.national_government_exams import NationalGovernmentExams
from api.models.db.organizer import Organizer
from api.models.db.other_academic_institutes_run_by_trust_society import (
    OtherAcademicInstitutesRunByTrustSociety,
)
from api.models.db.professional_communities import ProfessionalCommunities
from api.models.db.program_intakes import ProgramIntakes
from api.models.db.program import Program
from api.models.db.sdg_goal import SdgGoal
from api.models.db.sponsorship import Sponsorship
from api.models.db.student import Student
from api.models.db.user import User


class TableExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/tables/"

    async def fetch_adjunct_faculty(self) -> list[AdjunctFaculty]:
        pass

    async def fetch_after_graduation_entrepreneurship(
        self,
    ) -> list[AfterGraduationEntrepreneurship]:
        pass

    async def fetch_after_graduation_higher_studies(
        self,
    ) -> list[AfterGraduationHigherStudies]:
        pass

    async def fetch_after_graduation_placements(
        self,
    ) -> list[AfterGraduationPlacements]:
        pass

    async def fetch_after_graduation(self) -> list[AfterGraduation]:
        pass

    async def fetch_agencies(self) -> list[Agencies]:
        pass

    async def fetch_auth(self) -> list[Auth]:
        pass

    async def fetch_awards(self) -> list[Awards]:
        pass

    async def fetch_benefit_programs(self) -> list[BenefitPrograms]:
        pass

    async def fetch_book_publication_author(self) -> list[BookPublicationAuthor]:
        pass

    async def fetch_book_publication(self) -> list[BookPublication]:
        pass

    async def fetch_branch_intake(self) -> list[BranchIntake]:
        pass

    async def fetch_branches(self) -> list[Branches]:
        pass

    async def fetch_collaborative_activities(self) -> list[CollaborativeActivity]:
        pass

    async def fetch_companies(self) -> list[Companies]:
        pass

    async def fetch_competitive_event(self) -> list[CompetitiveEvent]:
        pass

    async def fetch_continuing_education_programs(
        self,
    ) -> list[ContinuingEducationPrograms]:
        pass

    async def fetch_departments(self) -> list[Departments]:
        pass

    async def fetch_e_resources(self) -> list[EResources]:
        pass

    async def fetch_event(self) -> list[Event]:
        pass

    async def fetch_facilities(self) -> list[Facilities]:
        pass

    async def fetch_faculty_courses(self) -> list[FacultyCourses]:
        pass

    async def fetch_faculty_internship_training_collaboration(
        self,
    ) -> list[FacultyInternshipTrainingCollaboration]:
        pass

    async def fetch_faculty_sponsored_research_projects_consultancy_work_institute_seed_money(
        self,
    ) -> list[FacultySponsoredResearchProjectsConsultancyWorkInstituteSeedMoney]:
        pass

    async def fetch_faculty_student_innovative_projects(
        self,
    ) -> list[FacultyStudentInnovativeProjects]:
        pass

    async def fetch_faculty(self) -> list[Faculty]:
        pass

    async def fetch_gpa(self) -> list[GPA]:
        pass

    async def fetch_informational_event(self) -> list[InformationalEvent]:
        pass

    async def fetch_institute(self) -> list[Institute]:
        pass

    async def fetch_ipr_earning(self) -> list[IprEarnings]:
        pass

    async def fetch_ipr(self) -> list[Ipr]:
        pass

    async def fetch_journal_publication_author(self) -> list[JournalPublicationAuthor]:
        pass

    async def fetch_journal_publication(self) -> list[JournalPublication]:
        pass

    async def fetch_journal(self) -> list[Journal]:
        pass

    async def fetch_laboratories_technical_manpower(
        self,
    ) -> list[LaboratoriesTechnicalManpower]:
        pass

    async def fetch_laboratories(self) -> list[Laboratories]:
        pass

    async def fetch_national_government_exams(self) -> list[NationalGovernmentExams]:
        pass

    async def fetch_organizer(self) -> list[Organizer]:
        pass

    async def fetch_other_academic_institutes_run_by_trust_society(
        self,
    ) -> list[OtherAcademicInstitutesRunByTrustSociety]:
        pass

    async def fetch_professional_communities(self) -> list[ProfessionalCommunities]:
        pass

    async def fetch_program_intakes(self) -> list[ProgramIntakes]:
        pass

    async def fetch_program(self) -> list[Program]:
        pass

    async def fetch_sdg_goal(self) -> list[SdgGoal]:
        pass

    async def fetch_sponsorship(self) -> list[Sponsorship]:
        pass

    async def fetch_student(self) -> list[Student]:
        pass

    async def fetch_user(self) -> list[User]:
        pass
