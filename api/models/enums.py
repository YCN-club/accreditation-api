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
