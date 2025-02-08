from nonebot.plugin import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    send_format: str
    """发送格式"""


plugin_config = get_plugin_config(Config)
