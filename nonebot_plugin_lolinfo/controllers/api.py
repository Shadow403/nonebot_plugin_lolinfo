import httpx
from nonebot import logger
from ..config import config, _PLUGINVER_

Client = httpx.Client(
    verify=False, timeout=config.lol_httpx_timeout, headers=config.lol_httpx_headers
)

AsyncClient = httpx.AsyncClient(
    verify=False, timeout=config.lol_httpx_timeout, headers=config.lol_httpx_headers
)

class LOLAPI:
    """
    [https://api-dev.shadow403.cn](https://api-dev.shadow403.cn)
    """

    def __init__(self):
        rootDict = Client.get(config.lol_api_url).json()
        self.root = rootDict["root"]
        self.paths = rootDict["paths"]
        self.parms = rootDict["parms"]
        self.version = rootDict["version"]

        if self.version != _PLUGINVER_:
            logger.error(f"\n===LOLINFO===\n插件版本与API版本不匹配\n插件版本: {_PLUGINVER_}\nAPI版本: {self.version}")

        else:
            logger.success(f"\n===LOLINFO===\n当前版本 {_PLUGINVER_}")

    async def _get_Hinfo(self, HName: str):
        path = "hero_info"
        try:
            rURL = f"{self.root}/{self.paths[path]}/{HName}{self.parms[path]}true"
            logger.info(f"开始获取数据 {rURL}")
            rDict = (await AsyncClient.get(rURL)).json()
            logger.success(f"获取数据成功 {rURL}")
            return rDict
        except Exception as e:
            logger.error(f"获取数据失败 {e}")
            return {"code": 401, "message": e}

    async def _get_Rinfo(self, HName: str, SPosi: str = "false"):
        path = "hero_rank"
        try:
            rURL = f"{self.root}/{self.paths[path]}/{HName}{self.parms[path]}{SPosi}"
            logger.info(f"开始获取数据 {rURL}")
            rDict = (await AsyncClient.get(rURL)).json()
            logger.success(f"获取数据成功 {rURL}")
            return rDict
        except Exception as e:
            logger.error(f"获取数据失败 {e}")
            return {"code": 401, "message": e}

    async def _get_DList(self):
        path = "originlist"
        try:
            rURL = f"{self.root}/{self.paths[path]}"
            logger.info(f"开始获取数据 {rURL}")
            rDict = (await AsyncClient.get(rURL)).json()
            logger.success(f"获取数据成功 {rURL}")
            return rDict
        except Exception as e:
            logger.error(f"获取数据失败 {e}")
            return {"code": 401, "message": e}


API = LOLAPI()
