from enum import Enum


class JournalPublicationType(str, Enum):
    HARDCOPY = "HARDCOPY"
    SOFTCOPY = "SOFTCOPY"


class JournalFrequency(str, Enum):
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    YEARLY = "YEARLY"


class BookPublicationType(str, Enum):
    BOOK = "BOOK"
    CHAPTER = "CHAPTER"


class IprType(str, Enum):
    PATENT = "PATENT"
    DESIGN = "DESIGN"
    COPYRIGHT = "COPYRIGHT"


class IprStatus(str, Enum):
    FILED = "FILED"
    GRANTED = "GRANTED"
    LICENSED = "LICENSED"
    COLLABORATIVE = "COLLABORATIVE"


class AcademicSemester(str, Enum):
    ODD = "ODD"
    EVEN = "EVEN"


class SocialDisadvantage(str, Enum):
    SC = "SC"
    ST = "ST"
    OBC = "OBC"


class EventLevel(str, Enum):
    INTERNAL = "INTERNAL"
    STATE = "STATE"
    NATIONAL = "NATIONAL"
    INTERNATIONAL = "INTERNATIONAL"


class EventClassification(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    TEAM = "TEAM"


class EventObjective(str, Enum):
    COMPETITIVE = "COMPETITIVE"
    INFORMATIONAL = "INFORMATIONAL"


class CompetitiveEventType(str, Enum):
    SPORTS = "SPORTS"
    CULTURAL = "CULTURAL"
    ACADEMIC = "ACADEMIC"
    OTHER = "OTHER"


class CommunityType(str, Enum):
    CLUBS = "CLUBS"
    NGO = "NGO"
    GOVERNMENT = "GOVERNMENT"
    INDUSTRY = "INDUSTRY"


class StudentOrigin(str, Enum):
    IN_STATE = "IN_STATE"
    OUT_OF_STATE = "OUT_OF_STATE"
    INTERNATIONAL = "INTERNATIONAL"


class StudentGender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class StudentEntries(str, Enum):
    REGULAR = "REGULAR"
    LATERAL_ENTRY = "LATERAL_ENTRY"
    OTHER = "OTHER"


class StudentExits(str, Enum):
    REGULAR = "REGULAR"
    LATE = "LATE"
    LEFT = "LEFT"


class FacultyHighestDegree(str, Enum):
    ASSOCIATE = "ASSOCIATE"
    BACHELORS = "BACHELORS"
    MASTERS = "MASTERS"
    DOCTORAL = "DOCTORAL"


class FacultyNatureOfAssociation(str, Enum):
    REGULAR = "REGULAR"
    CONTRACT = "CONTRACT"
    AD_HOC = "AD_HOC"


class FacultyContractualObligation(str, Enum):
    PART_TIME = "PART_TIME"
    FULL_TIME = "FULL_TIME"


class FacultyItcType(str, Enum):
    INTERNSHIP = "INTERNSHIP"
    TRAINING = "TRAINING"
    COLLABORATION = "COLLABORATION"


class FacultySrpcwismType(str, Enum):
    SPONSORED_RESEARCH_PROJECT = "SPONSORED_RESEARCH_PROJECT"
    CONSULTANCY_WORK = "CONSULTANCY_WORK"
    INSTITUTE_SEED_MONEY = "INSTITUTE_SEED_MONEY"


class AfterGraduationType(str, Enum):
    PLACEMENT = "PLACEMENT"
    ENTREPRENEURSHIP = "ENTREPRENEURSHIP"
    HIGHER_STUDIES = "HIGHER_STUDIES"


class AwardType(str, Enum):
    SPORTS = "SPORTS"
    RESEARCH = "RESEARCH"
    CULTURAL = "CULTURAL"
    FELLOWSHIP = "FELLOWSHIP"


class AwardUserType(str, Enum):
    FACULTY = "FACULTY"
    STUDENT = "STUDENT"


class CollaborativeActivityType(str, Enum):
    RESEARCH = "RESEARCH"
    STUDENT_EXCHANGE = "STUDENT_EXCHANGE"
    FACULTY_EXCHANGE = "FACULTY_EXCHANGE"
    INDUSTRY_INTERNSHIP = "INDUSTRY_INTERNSHIP"


class BenefitSchemeType(str, Enum):
    GOVERNMENT = "GOVERNMENT"
    NON_GOVERNMENT = "NON_GOVERNMENT"
    INSTITUTIONAL = "INSTITUTIONAL"
    COMPETITIVE_EXAM_GUIDANCE = "COMPETITIVE_EXAM_GUIDANCE"


class NationalGovernmentExamType(str, Enum):
    NET = "NET"
    SLET = "SLET"
    GATE = "GATE"
    GMAT = "GMAT"
    GPAT = "GPAT"
    CAT = "CAT"
    GRE = "GRE"
    IELET = "IELET"
    TOEFL = "TOEFL"
    PLAB = "PLAB"
    USMLE = "USMLE"
    AYUSH = "AYUSH"
    STATE_GOVERNMENT_EXAMS = "STATE_GOVERNMENT_EXAMS"
    UPSC = "UPSC"
    PG_NEET = "PG_NEET"
    OTHERS = "OTHERS"
