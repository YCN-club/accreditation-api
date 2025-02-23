from typing import List
from uuid import UUID
from mayim import PostgresExecutor

from api.models.generic_model import GenericModel


class NIRFExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NIRF/"

    async def get_NIRF_C3_post_interation(self, year: int) -> List[GenericModel]:
        """NIRF (C3) IPR - Post Interaction"""
        ...

    async def get_NIRF_C3_pre_interaction(self, year: int) -> List[GenericModel]:
        """NIRF (C3) IPR - Pre Interaction"""
        ...

    async def get_NIRF_C4(self, year: int) -> List[GenericModel]:
        """NIRF (C4) Sponsored Research"""
        ...

    async def get_NIRF_C7(self, year: int) -> List[GenericModel]:
        """NIRF (C7) Students Details Year-wise for the Last 3 Academic Years"""
        ...

    async def get_NIRF_C8(self, year: int) -> List[GenericModel]:
        """NIRF (C8) Top Position in Inter-college Sports / Extra Curricular
        Events for the Past 3 Academic Years"""
        ...

    async def get_NIRF_institutional_information(
        self, institute_id: UUID
    ) -> List[GenericModel]:
        """NIRF Institutional Information"""
        ...

    async def get_NIRF_IQAC_Development(self) -> List[GenericModel]:
        """NIRF IQAC Development"""
        ...

    async def get_NIRF_Student_Events(self) -> List[GenericModel]:
        """NIRF Student Events"""
        ...
