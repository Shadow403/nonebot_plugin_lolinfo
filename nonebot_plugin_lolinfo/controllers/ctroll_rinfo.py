from .api import LOLAPI
from ..config import _PATH_
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import on_command, require
from ..render.draw_rinfo import _d_rinfo

require("nonebot_plugin_saa")
import nonebot_plugin_saa as saa

API = LOLAPI()

ImgHeroRank = on_command("rinfo", aliases={"英雄排位"}, block=True, priority=1)

@ImgHeroRank.handle()
async def heroRank_handle(Initial: Message = CommandArg()):
    rData = await API._get_DList()
    if rData["code"] != 0:
        await saa.Text(f"返回状态码 {rCode}\n信息: {rData["message"]}").finish()

    InfoList = Initial.extract_plain_text().split(" ")
    if len(InfoList) == 2:
        rDict = await API._get_Rinfo(InfoList[0], InfoList[1])
    else:
        rDict = await API._get_Rinfo(InfoList[0])

    rCode = rDict["code"]
    if rCode == 0:
        rImg = await _d_rinfo(rDict, rData)
        await saa.Image(rImg).finish()
    if rCode == 422:
        await saa.Text(f"API 请求错误\n{rDict}").finish()
    if rCode == 1005:
        await saa.Image(f"{_PATH_}/templates/images/_rinfo_notfound.png").finish()
    if rCode != 0:
        await saa.Text(f"返回状态码 {rCode}\n信息: {rDict["message"]}").finish()
