import os
from pydantic import BaseModel
from nonebot import get_plugin_config

_PATH_: str = os.path.dirname(__file__)
_PLUGINVER_: str = "0.2.3"

class PluginConfig(BaseModel):
    lol_api_url: str = "https://api-dev.shadow403.cn/api/lol"
    lol_img_url: str = "https://game.gtimg.cn/images/lol/act/img/item"
    lol_httpx_headers: dict = {"User-Agent": "nonebot_plugin_lolinfo"}
    lol_httpx_timeout: int = 40

    # 请勿修改和添加以下改名称的配置项
    lol_img_minetype: str = ".png"
    lol_html_str: str = '<img src="'
    lol_html_end: str = '" alt="">'
    
config: PluginConfig = get_plugin_config(PluginConfig)
