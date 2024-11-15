import os
from pydantic import BaseModel
from nonebot import get_plugin_config

_PLUGINVER_: str = "0.3.2"
_PATH_: str = os.path.dirname(__file__)
_TEMPLATES_PATH_: str = f"{_PATH_}/templates"

class PluginConfig(BaseModel):
    lol_api_url: str = "https://shadow403.github.io/nonebot_plugin_lolinfo/urls.json"
    lol_img_url: str = "https://game.gtimg.cn/images/lol/act/img/item"
    lol_httpx_headers: dict = {"User-Agent": "nonebot_plugin_lolinfo"}
    lol_httpx_timeout: int = 40

    # 请勿修改和添加以下名称的配置项
    lol_img_minetype: str = ".png"
    lol_html_str: str = '<img src="'
    lol_html_end: str = '" alt="">'

config: PluginConfig = get_plugin_config(PluginConfig)
