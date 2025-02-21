import uuid
from typing import TypeVar

from mayim import Mayim
from sanic import Request, json
from sanic.log import logger
from sanic.views import HTTPMethodView
from sanic_ext import validate

from api.mayim.create_executor import CreateExecutor
from api.models.generic_protocol import GenericProtocol
from api.models.requests.faculty_research_consultancy_seed_money import (
    faculty_research_consultancy_seed_money,
)
from api.models.requests.insert_adjunct_faculty import adjunct_faculty
from api.models.requests.insert_after_graduation import after_graduation
from api.models.requests.insert_after_graduation_entrepreneurship import (
    after_graduation_entrepreneurship,
)
from api.models.requests.insert_after_graduation_higher_studies import (
    after_graduation_higher_studies,
)
from api.models.requests.insert_after_graduation_placements import (
    after_graduation_placements,
)
from api.models.requests.insert_agency import agency
from api.models.requests.insert_award import award
from api.models.requests.insert_benefit_programs import benefit_programs
from api.models.requests.insert_book_publication import book_publication
from api.models.requests.insert_book_publication_author import book_publication_author
from api.models.requests.insert_branch import branch
from api.models.requests.insert_branch_intake import branch_intake
from api.models.requests.insert_collaborative_activity import collaborative_activity
from api.models.requests.insert_company import company
from api.models.requests.insert_competitive_event import competitive_event
from api.models.requests.insert_continuing_programs import continuing_programs
from api.models.requests.insert_department import department
from api.models.requests.insert_e_resource import e_resource
from api.models.requests.insert_event import event
from api.models.requests.insert_event_sdg_goals import event_sdg_goals
from api.models.requests.insert_facility import facility
from api.models.requests.insert_faculty import faculty
from api.models.requests.insert_faculty_course import faculty_course
from api.models.requests.insert_faculty_internship_training_collaboration import (
    faculty_internship_training_collaboration,
)
from api.models.requests.insert_faculty_student_innovative_projects import (
    faculty_student_innovative_projects,
)
from api.models.requests.insert_gpa import gpa
from api.models.requests.insert_information_event import information_event
from api.models.requests.insert_institute import institute
from api.models.requests.insert_institute_other_academic_institutes import (
    institute_other_academic_institutes,
)
from api.models.requests.insert_institute_programs_considered import (
    institute_programs_considered,
)
from api.models.requests.insert_institute_programs_offered import (
    institute_programs_offered,
)
from api.models.requests.insert_ipr import ipr
from api.models.requests.insert_ipr_earning import ipr_earning
from api.models.requests.insert_journal import journal
from api.models.requests.insert_journal_publication import journal_publication
from api.models.requests.insert_journal_publication_author import (
    journal_publication_author,
)
from api.models.requests.insert_laboratories_technical_manpower import (
    laboratories_technical_manpower,
)
from api.models.requests.insert_laboratory import laboratory
from api.models.requests.insert_laboratory_technical_manpower import (
    laboratory_technical_manpower,
)
from api.models.requests.insert_national_government_exam import national_government_exam
from api.models.requests.insert_organizer import organizer
from api.models.requests.insert_other_academic_institutes_run_by_trust_society import (
    other_academic_institutes_run_by_trust_society,
)
from api.models.requests.insert_professional_communities import professional_communities
from api.models.requests.insert_program import program
from api.models.requests.insert_program_intake import program_intake
from api.models.requests.insert_sdg_goal import sdg_goal
from api.models.requests.insert_sponsorship import sponsorship
from api.models.requests.insert_student import student
from api.models.requests.insert_user import user

T = TypeVar("T", bound=GenericProtocol)


class CreateItem(HTTPMethodView):

    # TODO: Make Dynamic
    validation_classes = {
        "adjunct_faculty": adjunct_faculty,
        "after_graduation_entrepreneurship": after_graduation_entrepreneurship,
        "after_graduation_higher_studies": after_graduation_higher_studies,
        "after_graduation_placements": after_graduation_placements,
        "after_graduation": after_graduation,
        "agency": agency,
        "award": award,
        "benefit_programs": benefit_programs,
        "book_publication_author": book_publication_author,
        "book_publication": book_publication,
        "branch_intake": branch_intake,
        "branch": branch,
        "collaborative_activity": collaborative_activity,
        "company": company,
        "competitive_event": competitive_event,
        "continuing_programs": continuing_programs,
        "department": department,
        "e_resource": e_resource,
        "event_sdg_goals": event_sdg_goals,
        "event": event,
        "facility": facility,
        "faculty_course": faculty_course,
        "faculty_internship_training_collaboration": faculty_internship_training_collaboration,
        "faculty_research_consultancy_seed_money": faculty_research_consultancy_seed_money,
        "faculty_student_innovative_projects": faculty_student_innovative_projects,
        "faculty": faculty,
        "gpa": gpa,
        "information_event": information_event,
        "institute_other_academic_institutes": institute_other_academic_institutes,
        "institute_programs_considered": institute_programs_considered,
        "institute_programs_offered": institute_programs_offered,
        "institute": institute,
        "ipr_earning": ipr_earning,
        "ipr": ipr,
        "journal_publication_author": journal_publication_author,
        "journal_publication": journal_publication,
        "journal": journal,
        "laboratories_technical_manpower": laboratories_technical_manpower,
        "laboratory_technical_manpower": laboratory_technical_manpower,
        "laboratory": laboratory,
        "national_government_exam": national_government_exam,
        "organizer": organizer,
        "other_academic_institutes_run_by_trust_society": other_academic_institutes_run_by_trust_society,
        "professional_communities": professional_communities,
        "program_intake": program_intake,
        "program": program,
        "sdg_goal": sdg_goal,
        "sponsorship": sponsorship,
        "student": student,
        "user": user,
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
