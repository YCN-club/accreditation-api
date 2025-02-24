from typing import List
from mayim import PostgresExecutor

from api.models.generic_model import GenericModel


class NAACExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NAAC/"

    async def get_NAAC_3_1_3(self, year: int) -> List[GenericModel]:
        """NAAC (3.1.3) Number of teachers awarded national / international
        fellowship / Financial support for advanced studies / collaborative
        research participation in Indian and Overseas Institutions during the year"""

    async def get_NAAC_3_3_3(self, year: int) -> List[GenericModel]:
        """NAAC (3.3.3) Number of awards / recognitions received for
        innovation / discoveries by the institution / teachers / research
        scholars / students from recognized bodies during the year"""

    async def get_NAAC_3_4_3(self, year: int) -> List[GenericModel]:
        """NAAC (3.4.3) Number of Patents / Copyrights
        published / awarded / technology - transferred during the year"""

    async def get_NAAC_3_6_1(self) -> List[GenericModel]:
        """NAAC (3.6.1) Industry, Gov, NGO and Club Events"""

    async def get_NAAC_3_6_3(self) -> List[GenericModel]:
        """NAAC (3.6.3) Number of awards and recognition received for
        extension and outreach activities from Government / other
        recognised bodies during 1st July 2023 - 30th June 2024"""

    async def get_NAAC_3_6_4(self) -> List[GenericModel]:
        """NAAC (3.6.4) Institutional Social responsibility activities"""

    async def get_NAAC_3_7_1(self, year: int) -> List[GenericModel]:
        """NAAC (3.7.1) Number of Collaborative activities for research,
        faculty exchange, student exchange / Industry - internship in the year"""

    async def get_NAAC_4_3_5(self) -> List[GenericModel]:
        """NAAC (4.3.5) E - content resources used by teachers / students"""

    async def get_NAAC_5_1_1(self, year: int) -> List[GenericModel]:
        """NAAC (5.1.1) Average percentage of students benefited by
        scholarships, freeships, etc., provided by the institution,
        Government, and non - government agencies."""

    async def get_NAAC_5_1_3(self, year: int) -> List[GenericModel]:
        """NAAC (5.1.3) Following Capacity development and skills
        enhancement initiatives are taken by the institution"""

    async def get_NAAC_5_2_1(self, year: int) -> List[GenericModel]:
        """NAAC (5.2.1) Student qualifying for National / Gov Exams"""

    async def get_NAAC_5_2_2(self, year: int) -> List[GenericModel]:
        """NAAC (5.2.2) Number of placement / self - employment in professional
        services of outgoing students during the year"""

    async def get_NAAC_5_2_3(self, year: int) -> List[GenericModel]:
        """NAAC (5.2.3) Number of the graduates in the preceding academic
        year who have had progressed to higher education"""

    async def get_NAAC_5_3_1(self) -> List[GenericModel]:
        """NAAC (5.3.1) Awards / Medals for Sports / Cultural activities"""

    async def get_NAAC_5_3_3(self) -> List[GenericModel]:
        """NAAC (5.3.3) No. of sports and cultural events / competitions"""
