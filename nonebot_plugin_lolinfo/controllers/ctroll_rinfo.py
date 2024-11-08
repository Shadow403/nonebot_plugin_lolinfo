from .api import LOLAPI
from ..config import _PATH_
from nonebot import on_command, require
from nonebot.adapters import Message
from nonebot.params import CommandArg
from ..render.draw_rinfo import _d_rinfo

require("nonebot_plugin_saa")
import nonebot_plugin_saa as saa
API = LOLAPI()

ImgHeroRank = on_command("rinfo", aliases={"英雄排位"}, block=True, priority=1)


@ImgHeroRank.handle()
async def heroRank_handle(Initial: Message = CommandArg()):
    InfoList = Initial.extract_plain_text().split(" ")
    if len(InfoList) == 2:
        rDict = await API._get_Rinfo(InfoList[0], InfoList[1])
    else:
        rDict = await API._get_Rinfo(InfoList[0])

    rCode = rDict["code"]
    rMsg = rDict["message"]

    if rCode == 0:
        rImg = await _d_rinfo(rDict)
        await saa.Image(rImg).finish()
    if rCode == 401:
        await saa.Text(f"API 请求错误\n{rDict}").finish()
    if rCode == 404:
        await saa.Image(f"{_PATH_}/images/_rinfo_notfound.png").finish()
    if rCode != 0:
        await saa.Text(f"返回状态码 {rCode}\n信息: {rMsg}").finish()
