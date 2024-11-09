from nonebot import require

require("nonebot_plugin_htmlrender")
from nonebot_plugin_htmlrender import template_to_pic

from ..config import _TEMPLATES_PATH_
from ..utils.util_time import Func_nowtime
from ..utils.util_urlpath import Func_parseDict


async def _d_rinfo(rDict: dict, rData: dict):
    rDict = rDict["data"]
    rOrg = rData["data"]
    rUrl = await Func_parseDict(rDict, rOrg)
    rImg = await template_to_pic(
        template_path=_TEMPLATES_PATH_,
        template_name="rinfo.jinja2",
        templates={"rDict": rDict, "rUrl": rUrl, "Func_nowtime": Func_nowtime},
        pages={"viewport": {"width": 500, "height": 10}},
    )
    return rImg
