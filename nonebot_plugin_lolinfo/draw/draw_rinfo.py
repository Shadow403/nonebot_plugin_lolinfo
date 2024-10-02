from . import md_to_pic
from ..config import _PATH_
from ..utils.util_time import Func_nowtime
from ..utils.util_urlpath import Func_parseDict

async def _d_rinfo(rDict: dict = None):
    rDict = rDict["data"]
    rUrl = Func_parseDict(rDict)
    rMarkdown = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="{rDict["H_INFO"]["HERO_CONF"]["skins"]["sourceImg"]}" alt="" class="header-img">
            <div class="hid">{rDict["H_INFO"]["HERO_CONF"]["hero"]["heroId"]}</div>
            <img src="https://lol-img.pages.dev/position/middle/{rDict["H_INFO"]["HERO_CONF"]["hero"]["position"]}.png" alt="" class="position-img">
            <div class="timestamp">{rDict["R_DETAIL_DICT"]["FILE_TIME"]}</div>
        </div>
        <div class="main-content">
            <div class="left-column">
                <img src="{rDict["H_INFO"]["HERO_CONF"]["skins"]["loadingImg"]}" alt="" class="character-img">
                <div class="skills-icons">
                    <img src="{rDict["H_INFO"]["HERO_CONF"]["spells"][1]["abilityIconPath"]}" alt="P">
                    <img src="{rDict["H_INFO"]["HERO_CONF"]["spells"][2]["abilityIconPath"]}" alt="Q">
                    <img src="{rDict["H_INFO"]["HERO_CONF"]["spells"][4]["abilityIconPath"]}" alt="W">
                    <img src="{rDict["H_INFO"]["HERO_CONF"]["spells"][0]["abilityIconPath"]}" alt="E">
                    <img src="{rDict["H_INFO"]["HERO_CONF"]["spells"][3]["abilityIconPath"]}" alt="R">
                </div>
                <div class="base-info">
                    <p>胜率: {str(int(rDict["H_INFO"]["RANK_PROB"]["winrate"])/100)}%</p>
                    <p>Ban率: {str(int(rDict["H_INFO"]["RANK_PROB"]["banrate"])/100)}%</p>
                    <p>登场率: {str(int(rDict["H_INFO"]["RANK_PROB"]["showrate"])/100)}%</p>
                </div>
            </div>
            <div class="right-column">
                <div class="rune-section">
                    <h3>基础符文</h3>
                    <div class="rune-icons">
                        {rUrl[3][0]}
                        <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_RUNE"]["RUNE_DEATIL_LIST"]["1"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_RUNE"]["RUNE_DEATIL_LIST"]["1"]["1"]["winrate"])/100)}%</span>
                    </div>
                    <div class="rune-icons">
                        {rUrl[3][1]}
                        <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_RUNE"]["RUNE_DEATIL_LIST"]["2"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_RUNE"]["RUNE_DEATIL_LIST"]["2"]["1"]["winrate"])/100)}%</span>
                    </div>
                </div>
                <div class="equip-section">
                    <h3>鞋子出装</h3>
                    <div class="equip-icons">
                        <div class="equip-row">
                            {rUrl[0][0]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["1"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[0][1]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["2"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["2"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[0][2]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["3"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["BOOTS_EQUIP"]["3"]["winrate"])/100)}%</span>
                        </div>
                    </div>
                    <h3>核心出装</h3>
                    <div class="equip-icons">
                        <div class="equip-row">
                            {rUrl[1][0]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["1"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[1][1]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["2"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["2"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[1][2]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["3"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["CORE_EQUIP"]["3"]["winrate"])/100)}%</span>
                        </div>
                    </div>
                    <h3>出门出装</h3>
                    <div class="equip-icons">
                        <div class="equip-row">
                            {rUrl[2][0]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["OUT_EQUIP"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["OUT_EQUIP"]["1"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[2][1]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["OUT_EQUIP"]["2"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["OUT_EQUIP"]["2"]["winrate"])/100)}%</span>
                        </div>
                    </div>
                    <h3>召唤师技能</h3>
                    <div class="equip-icons">
                        <div class="equip-row">
                            {rUrl[4][0]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["SPELL_INFO"]["SPELL_EQUIP"]["1"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["SPELL_INFO"]["SPELL_EQUIP"]["1"]["winrate"])/100)}%</span>
                        </div>
                        <div class="equip-row">
                            {rUrl[4][1]}
                            <span>出场: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["SPELL_INFO"]["SPELL_EQUIP"]["2"]["showrate"])/100)}% | 胜率: {str(int(rDict["R_DETAIL_DICT"]["R_EQUIP"]["SPELL_INFO"]["SPELL_EQUIP"]["2"]["winrate"])/100)}%</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer">
            <p>Generated By ShadowAPI © 2024 | {Func_nowtime()}</p>
        </div>
    </div>
</body>
</html>
"""
    rImg = await md_to_pic(md=rMarkdown, css_path=f"{_PATH_}/draw/css/rinfo.css")
    return rImg
