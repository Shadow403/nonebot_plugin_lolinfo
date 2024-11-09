from .controllers import *
from nonebot import logger,require
from .config import PluginConfig, _PLUGINVER_
from nonebot.plugin import PluginMetadata,inherit_supported_adapters

require("nonebot_plugin_saa")

__plugin_meta__ = PluginMetadata(
    name="lolinfo",
    description="查询LOL各种信息🚧",
    usage="https://github.com/Shadow403/nonebot_plugin_lolinfo",
    type="application",
    homepage="https://github.com/Shadow403/nonebot_plugin_lolinfo",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_saa"),
    config=PluginConfig,
    extra={},
)

logger.info(f"当前版本 {_PLUGINVER_}")
