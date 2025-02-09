from uuid import UUID
from mayim import PostgresExecutor


class NIRFExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NIRF/"

    async def get_NIRF_C3_post_interation(self, year: int):
        """NIRF C3 - Post Interaction"""
        ...

    async def get_NIRF_C3_pre_interaction(self, year: int):
        """NIRF C3 - Pre Interaction"""
        ...

    async def get_NIRF_C4(self, year: int):
        """NIRF C4"""
        ...

    async def get_NIRF_C7(self, year: int):
        """NIRF C7"""
        ...

    async def get_NIRF_C8(self, year: int):
        """NIRF C8"""
        ...

    async def get_NIRF_institutional_information(self, institute_id: UUID):
        """NIRF Institutional Information"""
        ...

    async def get_NIRF_IQAC_Development(self):
        """NIRF IQAC Development"""
        ...

    async def get_NIRF_Student_Events(self):
        """NIRF Student Events"""
        ...
