import json
import httpx
from nonebot import logger
from ..config import PluginConfig

HTTPClient = httpx.Client(
        timeout=10,
        verify=False,
        headers=PluginConfig.httpx_headers
    )

class LOLAPI:
    """
    [https://api-dev.shadow403.cn/docs/LOL/](https://api-dev.shadow403.cn/docs/LOL/)
    """
    def __init__(self):
        self.url = PluginConfig.api_url

    async def _get_Hinfo(self, HName: str):
        try:
            rURL = f"{self.url}/heroImg/{HName}?min=true"
            logger.info(f"开始获取数据 {rURL}")
            rDict = json.loads(HTTPClient.get(rURL).text)
            logger.success(f"获取数据成功 {rURL}")
            return rDict
        except Exception as e:
            logger.error(f"获取数据失败 {e}")
            return {"code": 401, "message": e}
    
    async def _get_Rinfo(self, HName: str, SPosi: str = ""):
        try:
            rURL = f"{self.url}/heroRank/{HName}?posi={SPosi}"
            logger.info(f"开始获取数据 {rURL}")
            rDict = json.loads(HTTPClient.get(rURL).text)
            logger.success(f"获取数据成功 {rURL}")
            return rDict
        except Exception as e:
            logger.error(f"获取数据失败 {e}")
            return {"code": 401, "message": e}
