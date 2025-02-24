from typing import List
from uuid import UUID
from mayim import PostgresExecutor

from api.models.generic_model import GenericModel


class NBAExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NBA/"

    async def get_NBA_4_1(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.1) Enrolment Ratio at First Year Level"""

    async def get_NBA_4_2(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.2) Success Rate of the Students in the Stipulated Period of the Program"""

    async def get_NBA_4_3(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.3) Academic Performance in the Third Year Students of the Program"""

    async def get_NBA_4_4(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.4) Academic Performance in the Second Year Students of the Program"""

    async def get_NBA_4_5(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.5) Academic Performance in the First-Year Students of the Program"""

    async def get_NBA_4_6(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4.6) Placement, Higher Studies and Entrepreneurship"""

    async def get_NBA_4_7_1_1(self) -> List[GenericModel]:
        """NBA (4.7.1.1) List of Clubs"""

    async def get_NBA_4_7_1_2(self) -> List[GenericModel]:
        """NBA (4.7.1.2) Internal Events"""

    async def get_NBA_4_7_2_1(self) -> List[GenericModel]:
        """NBA (4.7.2.1) List of Students Participated in Professional Events"""

    async def get_NBA_4_7_3(self, year: int) -> List[GenericModel]:
        """NBA (4.7.3) Publication of Journals, Magazines, Newsletters, etc."""

    async def get_NBA_4_7_4(self, year: int) -> List[GenericModel]:
        """NBA (4.7.4) Student Publications"""

    async def get_NBA_4A(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4A) Admission details for the program"""

    async def get_NBA_4B(self, program_id: UUID, year: int) -> List[GenericModel]:
        """NBA (4B) Admission details for the program through multiple entry and exit points"""

    async def get_NBA_4C(self, program_id: UUID) -> List[GenericModel]:
        """NBA (4C) No. of students graduated within the stipulated period of the program."""

    async def get_NBA_5_2(self, program_id: UUID) -> List[GenericModel]:
        """NBA (5.2) Faculty Qualification"""

    async def get_NBA_5_3(self, program_id: UUID) -> List[GenericModel]:
        """NBA (5.3) Faculty Cadre Proportion"""

    async def get_NBA_5_4(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (5.4) Visiting/Adjunct Faculty/Professor of Practice"""

    async def get_NBA_5_5(self, program_id: UUID) -> List[GenericModel]:
        """NBA (5.5) Faculty Retention"""

    async def get_NBA_5A(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (5A) Faculty Details"""

    async def get_NBA_6_1_1(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (6.1.1) Memberships in Professional Committees at National/International Levels"""

    async def get_NBA_6_1_3(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (6.1.3) Faculty Contribution in Development of SWAYAM MOOCs and other E-Content"""

    async def get_NBA_6_1_4(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (6.1.4) Faculty Certification of MOOCs through SWAYAM and Other Government Program"""

    async def get_NBA_6_1_6(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (6.1.6) Faculty Support in Student Innovative Projects"""

    async def get_NBA_6_1_7(self, institute_id: UUID) -> List[GenericModel]:
        """NBA (6.1.7) Faculty Internship/Training/Collaboration with Industry"""

    async def get_NBA_6_2_1(self, department_id: UUID) -> List[GenericModel]:
        """NBA (6.2.1) Academic Research"""

    async def get_NBA_6_2_3(self, year: int) -> List[GenericModel]:
        """NBA (6.2.3) Sponsored Research Project"""

    async def get_NBA_6_2_4(self, year: int) -> List[GenericModel]:
        """NBA (6.2.4) Consultancy Work"""

    async def get_NBA_6_2_5(self, year: int) -> List[GenericModel]:
        """NBA (6.2.5) Institution Seed Money or Internal Research Grant to its Teachers for Research Work"""

    async def get_NBA_7_1_1(self) -> List[GenericModel]:
        """NBA (7.1.1) List of laboratories and technical manpower"""

    async def get_NBA_7_2_1(self) -> List[GenericModel]:
        """NBA (7.2.1) List of additional facilities"""

    async def get_NBA_7_4_1(self) -> List[GenericModel]:
        """NBA (7.4.1) List of various safety measures in laboratories"""

    async def get_NBA_institutional_information(
        self, institute_id: UUID
    ) -> List[GenericModel]:
        """NBA Institutional Information"""
