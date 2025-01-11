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
