from nonebot import require

require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import template_to_pic

from ..config import _PATH_
from ..utils.util_time import Func_nowtime
from ..utils.util_urlpath import Func_parseDict

TEMPLATE_PATH = f"{_PATH_}/templates"


async def _d_rinfo(rDict: dict):
    rDict = rDict["data"]
    rUrl = Func_parseDict(rDict)
    rImg = await template_to_pic(
        template_path=TEMPLATE_PATH,
        template_name="rinfo.jinja2",
        templates={"rDict": rDict, "rUrl": rUrl, "Func_nowtime": Func_nowtime},
        pages={"viewport": {"width": 1000, "height": 10}},
    )
    return rImg
