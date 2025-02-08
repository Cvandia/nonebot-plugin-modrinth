import json
from typing import ClassVar, Literal, TypeAlias

from httpx import AsyncClient

from .exception import RequestError

IndexType: TypeAlias = Literal["relevance", "downloads", "follows", "newest", "updated"]
ProjectType: TypeAlias = Literal[
    "mod", "resoucepack", "datapack", "shader", "modpack", "plugin"
]


class Modrinth:
    base_url = "https://api.modrinth.com/v2"
    _headers: ClassVar[dict] = {
        "Accept": "application/json",
    }

    @property
    def client(self) -> AsyncClient:
        if not hasattr(self, "_client"):
            self._client = AsyncClient(base_url=self.base_url, headers=self._headers)
        return self._client

    async def _search_by_query(
        self,
        query: str,
        game_version: str,
        index: IndexType = "relevance",
        project_type: ProjectType = "mod",
        limit: int = 5,
    ) -> dict:
        """
        搜索模组

        Args:
            query (str): 查询内容
            index (IndexType, optional): 排序方式. 默认为 "relevance".
            limit (int, optional): 返回数量. 默认为 5.

        Returns:
            dict: 搜索结果
        """
        async with self.client as client:
            params = {
                "query": query,
                "index": index,
                "limit": limit,
                "facets": json.dumps(
                    [
                        [f"verisons:{game_version}", f"project_type:{project_type}"],
                    ]
                ),
            }
            response = await client.get("/search", params=params)
            if error := response.json().get("error"):
                raise RequestError(error)
            return response.json()
