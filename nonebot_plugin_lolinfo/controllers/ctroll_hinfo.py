from .api import LOLAPI
from ..config import _PATH_
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from ..draw.draw_hinfo import _d_hinfo
from nonebot.adapters.onebot.v11 import MessageSegment

API = LOLAPI()

ImgHeroInfo = on_command(
        "/hinfo",
        aliases={"/英雄信息"},
        block=1,
        priority=1
    )

@ImgHeroInfo.handle()
async def heroInfo_handle(Initial: Message = CommandArg()):
    heroName = Initial.extract_plain_text()
    rDict = await API._get_Hinfo(heroName)

    if rDict["code"] == 0:
        rImg = await _d_hinfo(rDict)
        await ImgHeroInfo.finish(MessageSegment.image(rImg))
    if rDict["code"] == 401:
        await ImgHeroInfo.finish(MessageSegment.text(f"API 请求错误\n{rDict}"))
    if rDict["code"] == 404:
        await ImgHeroInfo.finish(MessageSegment.image(f"{_PATH_}/images/_rinfo_notfound.png"))
    if rDict["code"] != 0:
        await ImgHeroInfo.finish(MessageSegment.text(f"返回状态码 {rDict['code']}\n信息: {rDict['message']}"))
