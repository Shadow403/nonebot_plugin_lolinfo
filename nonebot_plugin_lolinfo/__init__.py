from .utils import *
from .controllers import *
from nonebot import logger
from .config import PluginConfig
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="lolinfo",
    description="查询LOL各种信息🚧",
    usage="https://github.com/Shadow403/nonebot_plugin_lolinfo",
    type="application",
    homepage="https://github.com/Shadow403/nonebot_plugin_lolinfo",
    supported_adapters={"~onebot.v11"},
    config=PluginConfig,
    extra={},
)

logger.info(f"当前版本 {PluginConfig._plugin_version_}")
