from .api import LOLAPI
from ..config import _PATH_
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from ..draw.draw_rinfo import _d_rinfo
from nonebot.adapters.onebot.v11 import MessageSegment

API = LOLAPI()

ImgHeroRank = on_command(
        "/rinfo",
        aliases={"/英雄排位"},
        block=1,
        priority=1
    )

@ImgHeroRank.handle()
async def heroRank_handle(Initial: Message = CommandArg()):
    InfoList = Initial.extract_plain_text().split(" ")
    if len(InfoList) == 2:
        rDict = await API._get_Rinfo(InfoList[0], InfoList[1])
    else:
        rDict = await API._get_Rinfo(InfoList[0])

    if rDict["code"] == 0:
        rImg = await _d_rinfo(rDict)
        await ImgHeroRank.finish(MessageSegment.image(rImg))
    if rDict["code"] == 401:
        await ImgHeroRank.finish(MessageSegment.text(f"API 请求错误\n{rDict}"))
    if rDict["code"] == 404:
        await ImgHeroRank.finish(MessageSegment.image(f"{_PATH_}/images/_rinfo_notfound.png"))
    if rDict["code"] != 0:
        await ImgHeroRank.finish(MessageSegment.text(f"返回状态码 {rDict["code"]}\n信息: {rDict["message"]}"))
