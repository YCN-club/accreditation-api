import uuid
from typing import TypeVar

from mayim import Mayim
from sanic import Request, json
from sanic.log import logger
from sanic.views import HTTPMethodView
from sanic_ext import validate

from api.mayim.create_executor import CreateExecutor
from api.models.generic_protocol import GenericProtocol
from api.models.requests.insert_adjunct_faculty import AdjunctFaculty
from api.models.requests.insert_after_graduation import AfterGraduation
from api.models.requests.insert_after_graduation_entrepreneurship import (
    AfterGraduationEntrepreneurship,
)
from api.models.requests.insert_after_graduation_higher_studies import (
    AfterGraduationHigherStudies,
)
from api.models.requests.insert_after_graduation_placements import (
    AfterGraduationPlacements,
)
from api.models.requests.insert_agency import Agencies
from api.models.requests.insert_award import Awards
from api.models.requests.insert_benefit_programs import BenefitPrograms
from api.models.requests.insert_book_publication import BookPublication
from api.models.requests.insert_book_publication_author import BookPublicationAuthor
from api.models.requests.insert_branch import Branches
from api.models.requests.insert_branch_intake import BranchIntake
from api.models.requests.insert_collaborative_activity import CollaborativeActivity
from api.models.requests.insert_company import Companies
from api.models.requests.insert_competitive_event import CompetitiveEvent
from api.models.requests.insert_continuing_programs import ContinuingEducationPrograms
from api.models.requests.insert_department import Departments
from api.models.requests.insert_e_resource import EResources
from api.models.requests.insert_event import Event
from api.models.requests.insert_event_sdg_goals import event_sdg_goals
from api.models.requests.insert_facility import Facilities
from api.models.requests.insert_faculty import Faculty
from api.models.requests.insert_faculty_course import FacultyCourses
from api.models.requests.insert_faculty_internship_training_collaboration import (
    FacultyInternshipTrainingCollaboration,
)
from api.models.requests.insert_faculty_sponsored_research_projects_consultancy_work_institute_seed_money import (  # noqa: E501
    FacultySponsoredResearchProjectsConsultancyWorkInstituteSeedMoney,
)
from api.models.requests.insert_faculty_student_innovative_projects import (
    FacultyStudentInnovativeProjects,
)
from api.models.requests.insert_gpa import GPA
from api.models.requests.insert_information_event import InformationalEvent
from api.models.requests.insert_institute import Institute
from api.models.requests.insert_institute_other_academic_institutes import (
    institute_other_academic_institutes,
)
from api.models.requests.insert_institute_programs_considered import (
    institute_programs_considered,
)
from api.models.requests.insert_institute_programs_offered import (
    institute_programs_offered,
)
from api.models.requests.insert_ipr import Ipr
from api.models.requests.insert_ipr_earning import IprEarnings
from api.models.requests.insert_journal import Journal
from api.models.requests.insert_journal_publication import JournalPublication
from api.models.requests.insert_journal_publication_author import (
    JournalPublicationAuthor,
)
from api.models.requests.insert_laboratories_technical_manpower import (
    LaboratoriesTechnicalManpower,
)
from api.models.requests.insert_laboratory import Laboratories
from api.models.requests.insert_laboratory_technical_manpower import (
    laboratory_technical_manpower,
)
from api.models.requests.insert_national_government_exam import NationalGovernmentExams
from api.models.requests.insert_organizer import Organizer
from api.models.requests.insert_other_academic_institutes_run_by_trust_society import (
    OtherAcademicInstitutesRunByTrustSociety,
)
from api.models.requests.insert_professional_communities import professional_communities
from api.models.requests.insert_program import Program
from api.models.requests.insert_program_intake import ProgramIntakes
from api.models.requests.insert_sdg_goal import SdgGoal
from api.models.requests.insert_sponsorship import Sponsorship
from api.models.requests.insert_student import Student
from api.models.requests.insert_user import User

T = TypeVar("T", bound=GenericProtocol)


class CreateItem(HTTPMethodView):

    # TODO: Check the feasibility of making this dynamic
    validation_classes = {
        "adjunct_faculty": AdjunctFaculty,
        "after_graduation_entrepreneurship": AfterGraduationEntrepreneurship,
        "after_graduation_higher_studies": AfterGraduationHigherStudies,
        "after_graduation_placements": AfterGraduationPlacements,
        "after_graduation": AfterGraduation,
        "agency": Agencies,
        "award": Awards,
        "benefit_programs": BenefitPrograms,
        "book_publication_author": BookPublicationAuthor,
        "book_publication": BookPublication,
        "branch_intake": BranchIntake,
        "branch": Branches,
        "collaborative_activity": CollaborativeActivity,
        "company": Companies,
        "competitive_event": CompetitiveEvent,
        "continuing_programs": ContinuingEducationPrograms,
        "department": Departments,
        "e_resource": EResources,
        "event_sdg_goals": event_sdg_goals,
        "event": Event,
        "facility": Facilities,
        "faculty_course": FacultyCourses,
        "faculty_internship_training_collaboration": FacultyInternshipTrainingCollaboration,
        "faculty_research_consultancy_seed_money": FacultySponsoredResearchProjectsConsultancyWorkInstituteSeedMoney,  # noqa: E501
        "faculty_student_innovative_projects": FacultyStudentInnovativeProjects,
        "faculty": Faculty,
        "gpa": GPA,
        "information_event": InformationalEvent,
        "institute_other_academic_institutes": institute_other_academic_institutes,
        "institute_programs_considered": institute_programs_considered,
        "institute_programs_offered": institute_programs_offered,
        "institute": Institute,
        "ipr_earning": IprEarnings,
        "ipr": Ipr,
        "journal_publication_author": JournalPublicationAuthor,
        "journal_publication": JournalPublication,
        "journal": Journal,
        "laboratories_technical_manpower": LaboratoriesTechnicalManpower,
        "laboratory_technical_manpower": laboratory_technical_manpower,
        "laboratory": Laboratories,
        "national_government_exam": NationalGovernmentExams,
        "organizer": Organizer,
        "other_academic_institutes_run_by_trust_society": OtherAcademicInstitutesRunByTrustSociety,
        "professional_communities": professional_communities,
        "program_intake": ProgramIntakes,
        "program": Program,
        "sdg_goal": SdgGoal,
        "sponsorship": Sponsorship,
        "student": Student,
        "user": User,
    }

    async def post(self, request: Request, slug: str):
        validation_class = self.validation_classes.get(slug, None)
        if validation_class is None:
            return json({"error": "Invalid type"}, status=400)

        @validate(form=validation_class)
        async def create_item(request: Request, slug: str, body: T):
            # Get the executor
            executor = Mayim.get(CreateExecutor)
            # Get the function
            create_function = getattr(executor, f"create_{slug}")
            try:
                # Call the function
                await create_function(body)
                return json({"message": "Success"}, status=201)
            except Exception as e:
                ref_id = uuid.uuid4()
                logger.error(f"Error: {e} Ref ID: {ref_id}")
                return json(
                    {"error": "Internal Server Error", "ref_id": ref_id}, status=500
                )

        # Call the internal function to validate the data
        try:
            await create_item(request, slug)
        except Exception as e:
            logger.error(e)
            return json({"error": "Validation Error"}, status=500)
