from nonebot import require

require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import template_to_pic

from ..config import _TEMPLATES_PATH_
from ..utils.util_time import Func_nowtime


async def _d_hinfo(rDict: dict):
    rDict = rDict["data"]

    rImg = await template_to_pic(
        template_path=_TEMPLATES_PATH_,
        template_name="hinfo.jinja2",
        templates={"rDict": rDict, "Func_nowtime": Func_nowtime},
        pages={"viewport": {"width": 500, "height": 10}},
    )
    return rImg
