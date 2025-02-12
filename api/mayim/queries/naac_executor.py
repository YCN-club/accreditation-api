from mayim import PostgresExecutor


class NAACExecutor(PostgresExecutor):
    generic_prefix = ""
    path = "./queries/fetch/NAAC/"

    async def get_NAAC_3_1_3(self, year: int):
        """NAAC 3.1.3"""
        ...

    async def get_NAAC_3_3_3(self, year: int):
        """NAAC 3.3.3"""
        ...

    async def get_NAAC_3_4_3(self, year: int):
        """NAAC 3.4.3"""
        ...

    async def get_NAAC_3_6_1(self):
        """NAAC 3.6.1"""
        ...

    async def get_NAAC_3_6_3(self):
        """NAAC 3.6.3"""
        ...

    async def get_NAAC_3_6_4(self):
        """NAAC 3.6.4"""
        ...

    async def get_NAAC_3_7_1(self, year: int):
        """NAAC 3.7.1"""
        ...

    async def get_NAAC_4_3_5(self):
        """NAAC 4.3.5"""
        ...

    async def get_NAAC_5_1_1(self, year: int):
        """NAAC 5.1.1"""
        ...

    async def get_NAAC_5_1_3(self, year: int):
        """NAAC 5.1.3"""
        ...

    async def get_NAAC_5_2_1(self, year: int):
        """NAAC 5.2.1"""
        ...

    async def get_NAAC_5_2_2(self, year: int):
        """NAAC 5.2.2"""
        ...

    async def get_NAAC_5_2_3(self, year: int):
        """NAAC 5.2.3"""
        ...

    async def get_NAAC_5_3_1(self):
        """NAAC 5.3.1"""
        ...

    async def get_NAAC_5_3_3(self):
        """NAAC 5.3.3"""
        ...
