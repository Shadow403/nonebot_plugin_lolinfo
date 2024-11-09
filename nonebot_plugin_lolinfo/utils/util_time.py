import time
from datetime import datetime


def Func_nowtime(
    info: bool = False,
    timestamp: bool = False,
    timestamp_str: bool = False,
    formate: str = "%Y-%m-%d %H:%M:%S",
):
    """
    **info (信息样式)**
        - `%Y-%m-%d %H:%M:%S [UTC+8]` | `str`
    **timestamp (时间戳)**
        - `1628600000` | `int`
    **timestamp_str (时间戳)**
        - `1628600000` | `str`
    **formate (时间格式)**
        - `%Y-%m-%d %H:%M:%S` | `str`
    """

    if timestamp:
        ts = int(time.time())
        return ts

    if timestamp_str:
        ts = str(int(time.time()))
        return ts

    now = datetime.now()
    formatTime = now.strftime(formate)

    if info:
        formatTime += " [UTC+8]"

    return formatTime
