from .api import LOLAPI
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageSegment

API = LOLAPI()

ImgHeroInfo = on_command("/hinfo", aliases={"/英雄信息"}, block=1, priority=1)
ImgHeroRank = on_command("/rinfo", aliases={"/英雄排位"}, block=1, priority=1)

@ImgHeroInfo.handle()
async def heroInfo_handle(Initial: Message = CommandArg()):
    heroName = Initial.extract_plain_text()
    rImg = API.getHeroInfo(heroName)

    await ImgHeroInfo.send(MessageSegment.image(rImg))

@ImgHeroRank.handle()
async def heroRank_handle(Initial: Message = CommandArg()):
    InfoList = Initial.extract_plain_text().split(" ")
    print(InfoList)

    if len(InfoList) == 1:
        rImg = API.getHeroRank(InfoList[0], "None")
    else:
        rImg = API.getHeroRank(InfoList[0], InfoList[1])

    await ImgHeroRank.send(MessageSegment.image(rImg))
