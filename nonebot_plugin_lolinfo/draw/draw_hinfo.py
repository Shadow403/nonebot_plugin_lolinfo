from . import md_to_pic
from ..config import _PATH_
from ..utils.util_time import Func_nowtime

async def _d_hinfo(rDict: dict):
    rDict = rDict["data"]
    rMarkdown = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="header">
        <img src="{rDict['skins']['sourceImg']}" alt="">
        <div class="hid">{rDict['hero']['heroId']}</div>
        <div class="timestamp">{rDict['fileTime']}</div>
    </div>
    <div class="container">
        <div class="left-panel">
            <div class="hero-image">
                <img src="{rDict['skins']['loadingImg']}" alt="">
            </div>
            <div class="hero-name">{rDict['hero']['name']}</div>
            <div class="hero-title">{rDict['hero']['title']}</div>
            <div class="hero-description">
                {rDict['hero']['shortBio']}
            </div>
        </div>
        <div class="right-panel">
            <div class="skill">
                <h3 class="skill-title">
                    <img src="{rDict['spells'][1]['abilityIconPath']}" alt=""> {rDict['spells'][1]['name']}
                </h3>
                <p class="skill-description">
                    {rDict['spells'][1]['description'].replace("\n", "")}
                </p>
            </div>
            <div class="skill">
                <h3 class="skill-title">
                    <img src="{rDict['spells'][2]['abilityIconPath']}" alt=""> {rDict['spells'][2]['name']}
                </h3>
                <p class="skill-description">
                    {rDict['spells'][2]['description'].replace("\n", "")}
                </p>
            </div>
            <div class="skill">
                <h3 class="skill-title">
                    <img src="{rDict['spells'][4]['abilityIconPath']}" alt=""> {rDict['spells'][4]['name']}
                </h3>
                <p class="skill-description">
                    {rDict['spells'][4]['description'].replace("\n", "")}
                </p>
            </div>
            <div class="skill">
                <h3 class="skill-title">
                    <img src="{rDict['spells'][0]['abilityIconPath']}" alt=""> {rDict['spells'][0]['name']}
                </h3>
                <p class="skill-description">
                    {rDict['spells'][0]['description'].replace("\n", "")}
                </p>
            </div>
            <div class="skill">
                <h3 class="skill-title">
                    <img src="{rDict['spells'][3]['abilityIconPath']}" alt=""> {rDict['spells'][3]['name']}
                </h3>
                <p class="skill-description">
                    {rDict['spells'][3]['description'].replace("\n", "")}
                </p>
            </div>
        </div>
    </div>
    <div class="footer">
        <p>Generated By ShadowAPI © {Func_nowtime()}</p>
    </div>
</body>
</html>
"""
    rImg = await md_to_pic(md=rMarkdown, css_path=f"{_PATH_}/draw/css/hinfo.css")
    return rImg
