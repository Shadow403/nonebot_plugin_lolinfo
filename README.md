<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# nonebot-plugin-lolinfo

_✨ 基于 [NoneBot2](https://github.com/nonebot/nonebot2) & [ShadowAPI](https://api-dev.shadow403.cn/) 的一个 NoneBot 英雄联盟查询插件 ✨_

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/shadow403/nonebot_plugin_lolinfo.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_lolinfo">
  <img src="https://img.shields.io/pypi/v/nonebot_plugin_lolinfo.svg" alt="pypi">
</a>

</div>

## 📖 介绍
将英雄联盟的各种信息发送到QQ中 持续更新中 🚧

## 🎦 效果
<details>
<summary> 展开 </summary>

`/hinfo 塞拉斯`
![](preview/塞拉斯_信息.png)

`/rinfo 塞拉斯 上`
![](preview/塞拉斯_排位.png)

</details>

## 💿 安装
```python
pip install nonebot-plugin-lolinfo
```

```python
nb plugin install nonebot-plugin-lolinfo
```

## 🎁 使用
`Tips:  支持模糊搜索 🔍`
- /hinfo `<英雄名 | 英雄外号>`
- /rinfo `<英雄名 | 英雄外号>` `<分路(可选)>`

## 🛠️ 配置
|配置名|数据类型|默认值|
|-------------------|------|------------------------------------------------|
|`lol_api_url`      |`str` |`https://api-dev.shadow403.cn/api/lol`          |
|`lol_img_url`      |`str` |`https://game.gtimg.cn/images/lol/act/img/item` |
|`lol_httpx_headers`|`dict`|`{"User-Agent": "nonebot_plugin_lolinfo"}`      |
|`lol_httpx_timeout`|`int` |`40`                                            |

## 🍺 感谢
- 图片制作 [`nonebot-plugin-htmlrender`](https://github.com/kexue-z/nonebot-plugin-htmlrender)

<br>

<details>
<summary> 日志 </summary>

- `v0.1.0` 发布此项目
- `v0.1.1` 修改 README.md
- `v0.2.0` 整体更新 本地合成图片
- `v0.2.1` 更新依赖
- `v0.2.2` 更新 `PluginConfig`
- `v0.2.3` 更新 `PluginConfig` | 添加异步处理 `httpx.AsyncClient`
- `v0.2.4` 修复 `util_urlpath.py` 更新 `PluginConfig` | 添加超时配置 `httpx.timeout`
- `v0.2.5` 修复🐛 `SyntaxError` [`#2`](https://github.com/Shadow403/nonebot_plugin_lolinfo/issues/2)
- `v0.3.0` 修复🐛 [`#4`](https://github.com/Shadow403/nonebot_plugin_lolinfo/issues/4) [`#6`](https://github.com/Shadow403/nonebot_plugin_lolinfo/issues/6) | 更新API链接🔗
