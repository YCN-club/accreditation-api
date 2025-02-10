from uuid import UUID
from mayim import PostgresExecutor


class NBAExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NBA/"

    async def get_NBA_4_1(self, program_id: UUID, year: int):
        """NBA 4.1"""
        ...

    async def get_NBA_4_2(self, program_id: UUID, year: int):
        """NBA 4.2"""
        ...

    async def get_NBA_4_3(self, program_id: UUID, year: int):
        """NBA 4.3"""
        ...

    async def get_NBA_4_4(self, program_id: UUID, year: int):
        """NBA 4.4"""
        ...

    async def get_NBA_4_5(self, program_id: UUID, year: int):
        """NBA 4.5"""
        ...

    async def get_NBA_4_6(self, program_id: UUID, year: int):
        """NBA 4.6"""
        ...

    async def get_NBA_4_7_1_1(self):
        """NBA 4.7.1.1"""
        ...

    async def get_NBA_4_7_1_2(self):
        """NBA 4.7.1.2"""
        ...

    async def get_NBA_4_7_2_1(self):
        """NBA 4.7.2.1"""
        ...

    async def get_NBA_4_7_3(self, year: int):
        """NBA 4.7.3"""
        ...

    async def get_NBA_4_7_4(self, year: int):
        """NBA 4.7.4"""
        ...

    async def get_NBA_4A(self, program_id: UUID, year: int):
        """NBA 4A"""
        ...

    async def get_NBA_4B(self, program_id: UUID, year: int):
        """NBA 4B"""
        ...

    async def get_NBA_4C(self, program_id: UUID):
        """NBA 4C"""
        ...

    async def get_NBA_5_2(self, program_id: UUID):
        """NBA 5.2"""
        ...

    async def get_NBA_5_3(self, program_id: UUID):
        """NBA 5.3"""
        ...

    async def get_NBA_5_4(self, institute_id: UUID):
        """NBA 5.4"""
        ...

    async def get_NBA_5_5(self, program_id: UUID):
        """NBA 5.5"""
        ...

    async def get_NBA_5A(self, institute_id: UUID):
        """NBA 5A"""
        ...

    async def get_NBA_6_1_1(self, institute_id: UUID):
        """NBA 6.1.1"""
        ...

    async def get_NBA_6_1_3(self, institute_id: UUID):
        """NBA 6.1.3"""
        ...

    async def get_NBA_6_1_4(self, institute_id: UUID):
        """NBA 6.1.4"""
        ...

    async def get_NBA_6_1_6(self, institute_id: UUID):
        """NBA 6.1.6"""
        ...

    async def get_NBA_6_1_7(self, institute_id: UUID):
        """NBA 6.1.7"""
        ...

    async def get_NBA_6_2_1(self, department_id: UUID):
        """NBA 6.2.1"""
        ...

    async def get_NBA_6_2_3(self, year: int):
        """NBA 6.2.3"""
        ...

    async def get_NBA_6_2_4(self, year: int):
        """NBA 6.2.4"""
        ...

    async def get_NBA_6_2_5(self, year: int):
        """NBA 6.2.5"""
        ...

    async def get_NBA_7_1_1(self):
        """NBA 7.1.1"""
        ...

    async def get_NBA_7_2_1(self):
        """NBA 7.2.1"""
        ...

    async def get_NBA_7_4_1(self):
        """NBA 7.4.1"""
        ...

    async def get_NBA_institutional_information(self, institute_id: UUID):
        """NBA Institutional Information"""
        ...
