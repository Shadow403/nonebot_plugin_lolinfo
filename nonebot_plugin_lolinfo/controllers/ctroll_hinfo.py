from .api import LOLAPI
from ..config import _PATH_
from nonebot import on_command, require
from nonebot.adapters import Message
from nonebot.params import CommandArg
from ..render.draw_hinfo import _d_hinfo
from nonebot.adapters.onebot.v11 import MessageSegment

require("nonebot_plugin_saa")
import nonebot_plugin_saa as saa


from PIL import Image
from io import BytesIO

API = LOLAPI()

ImgHeroInfo = on_command("hinfo", aliases={"英雄信息"}, block=True, priority=1)


@ImgHeroInfo.handle()
async def heroInfo_handle(Initial: Message = CommandArg()):
    heroName = Initial.extract_plain_text()
    rDict = await API._get_Hinfo(heroName)

    rCode = rDict["code"]
    rMsg = rDict["message"]

    if rCode == 0:
        rImg = await _d_hinfo(rDict)
        img = Image.open(BytesIO(rImg))
        img.show()
        await saa.Image(rImg).finish()
    if rCode == 401:
        await ImgHeroInfo.finish(MessageSegment.text(f"API 请求错误\n{rDict}"))
    if rCode == 404:
        await saa.Image(f"{_PATH_}/templates/images/_rinfo_notfound.png").finish()
    if rCode != 0:
        await ImgHeroInfo.finish(
            MessageSegment.text(f"返回状态码 {rCode}\n信息: {rMsg}")
        )
