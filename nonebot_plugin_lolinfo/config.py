import os
from pydantic import BaseModel
from nonebot import get_plugin_config

_PATH_: str = os.path.dirname(__file__)
_PLUGINVER_: str = "0.2.3"

class PluginConfig(BaseModel):
    api_url: str = "https://api-dev.shadow403.cn/api/lol"
    httpx_headers: dict = {"User-Agent": "nonebot_plugin_lolinfo"}
    img_url: str = "https://game.gtimg.cn/images/lol/act/img/item"
    img_minetype: str = ".png"
    html_str: str = '<img src="'
    html_end: str = '" alt="">'

config: PluginConfig = get_plugin_config(PluginConfig)
