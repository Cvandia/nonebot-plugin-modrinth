from contextlib import suppress

from nonebot import require

require("nonebot_plugin_waiter")

from . import handler as handler
from .config import Config

usage = """
搜索模组: /modrinth search <模组名>
获取模组: /modrinth get <模组ID>
获取模组列表: /modrinth list <模组类型>
获取模组文件: /modrinth file <模组ID> <文件ID>
获取模组依赖: /modrinth deps <模组ID>
""".strip()

with suppress(Exception):
    from nonebot.plugin import PluginMetadata

    __plugin_meta__ = PluginMetadata(
        name="Minecraft 模组获取",
        description="通过 Modrinth API 获取 Minecraft 模组信息",
        usage=usage,
        homepage="https://github.com/Cvandia/nonebot-plugin-modrinth",
        config=Config,
        type="application",
        supported_adapters=None,
        extra={"author": "Cvandia", "email": "1141538825@qq.com"},
    )
