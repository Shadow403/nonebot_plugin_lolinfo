from .api import API
from ..config import _PATH_
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot import on_command, require
from ..render.draw_hinfo import _d_hinfo

require("nonebot_plugin_saa")
import nonebot_plugin_saa as saa

ImgHeroInfo = on_command("hinfo", aliases={"英雄信息"}, block=True, priority=1)

@ImgHeroInfo.handle()
async def heroInfo_handle(Initial: Message = CommandArg()):
    heroName = Initial.extract_plain_text()
    rDict = await API._get_Hinfo(heroName)

    rCode = rDict["code"]
    rMsg = rDict["message"]

    if rCode == 0:
        rImg = await _d_hinfo(rDict)
        await saa.Image(rImg).finish()
    if rCode == 422:
        await saa.Text(f"API 请求错误\n{rDict}").finish()
    if rCode == 404:
        await saa.Image(f"{_PATH_}/templates/images/_hinfo_notfound.png").finish()
    if rCode != 0:
        await saa.Text(f"返回状态码 {rCode}\n信息: {rMsg}").finish()
