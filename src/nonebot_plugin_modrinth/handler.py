from typing import Any

from nonebot.adapters import Event
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.plugin import on_command
from nonebot_plugin_waiter import prompt

from .modrinth import Modrinth

modrinth = Modrinth()

search = on_command("search", aliases={"搜索模组"})
get = on_command("get", aliases={"获取模组"})
list = on_command("list", aliases={"获取模组列表"})
file = on_command("file", aliases={"获取模组文件"})
deps = on_command("deps", aliases={"获取模组依赖"})


def handle_user_input(event: Event):
    message = event.get_plaintext()
    if message in ["取消", "取消操作"]:
        return "q"
    return message


@search.handle()
async def _(matcher: Matcher, arg: Any = CommandArg()):  # noqa: B008
    if not arg:
        user_input = prompt("请输入模组名", handler=handle_user_input, timeout=60)
        if not user_input:
            await matcher.finish("超时")
        elif user_input == "q":
            await matcher.finish("已取消")
        arg = user_input
    await matcher.send("搜索中...")
    result = await modrinth._search_by_query(arg, "1.16.5")
    await matcher.finish(result)
