import os

_PATH_ = os.path.dirname(__file__)

class PluginConfig:
    _plugin_version_: str = "0.2.0"
    api_url: str = "https://api-dev.shadow403.cn/api/lol"
    httpx_headers: dict = {"User-Agent": "nonebot_plugin_lolinfo"}
    img_url: str = "https://game.gtimg.cn/images/lol/act/img/item"
    img_minetype: str = ".png"
    html_str: str = '<img src="'
    html_end: str = '" alt="">'

