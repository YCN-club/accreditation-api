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
