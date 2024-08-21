import httpx
from nonebot import logger

headers = {"User-Agent": "nonebot_plugin_lolinfo"}
HTTPClient = httpx.Client(timeout=None, verify=False, headers=headers)

class LOLAPI:
    """
    `https://api-docs.shadow403.cn/docs/LOL/`
    """
    def __init__(self):
        self.url = "https://api-dev.shadow403.cn/api/lol"

    def getHeroInfo(self, HName):
        try:
            rImg = HTTPClient.get(f"{self.url}/heroImg/{HName}").content
            return rImg
        except Exception as e:
            logger.error(e)
    
    def getHeroRank(self, HName, SPosi):
        try:
            rImg = HTTPClient.get(f"{self.url}/heroRank/{HName}?posi={SPosi}").content
            # 该 URL 请求过慢
            # 可自行编写绘图脚本 API 参考 https://api-docs.shadow403.cn/docs/LOL/%E8%8B%B1%E9%9B%84%E6%8E%92%E4%BD%8D.html
            # 如果可以的话最好提交个 PR 😘
            return rImg
        except Exception as e:
            logger.error(e)
