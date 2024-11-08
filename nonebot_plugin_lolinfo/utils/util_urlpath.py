from ..config import config


def _f_parse_item(data: dict):
    _url = []
    _len0 = len(data)
    if _len0 > 3:
        _len0 = 3
    for i0 in range(_len0):
        _v0 = data[str(i0 + 1)].get("itemid")
        if "&" not in _v0:
            _v1 = f"{config.lol_html_str}{config.lol_img_url}/{_v0}{config.lol_img_minetype}{config.lol_html_end}"
            _url.append(_v1)
        _url0 = ""
        _v0 = _v0.split("&")
        _len1 = len(_v0)
        if _len1 > 3:
            _len1 = 3
        for i1 in range(_len1):
            _v1 = f"{config.lol_html_str}{config.lol_img_url}/{_v0[i1]}{config.lol_img_minetype}{config.lol_html_end}"
            _url0 += _v1
        _url.append(_url0)
    return _url


def _f_parse_rune(data: dict):
    _url0 = []
    _url1 = []
    _rune_list1 = data["RUNE_DEATIL_LIST"]["1"]["1"]["perk"].split("&")
    _rune_list2 = data["RUNE_DEATIL_LIST"]["2"]["1"]["perk"].split("&")
    _rune_list = _rune_list1 + _rune_list2
    for v0 in _rune_list:
        v1 = f"{config.lol_html_str}{data["RUNE_ORIGIN_LIST"][v0]["icon"]}{config.lol_html_end}"
        _url0.append(v1)
    for i in range(0, len(_url0), 9):
        v2 = ""
        v2 += "".join(_url0[i : i + 9])
        _url1.append(v2)
    return _url1


def _f_parse_spell(data: dict):
    _url0 = []
    _url1 = []
    _spell_list = data["SPELL_EQUIP"]
    _len = len(_spell_list)
    if _len > 2:
        _len = 2
    for i0 in range(_len):
        v0 = _spell_list[str(i0 + 1)]["spellid"].split("&")
        for v1 in v0:
            v0 = f"{config.lol_html_str}{data["SPELL_ORIGIN_LIST"][v1]["icon"]}{config.lol_html_end}"
            _url0.append(v0)
    for i in range(0, len(_url0), 2):
        v2 = ""
        v2 += "".join(_url0[i : i + 2])
        _url1.append(v2)
    return _url1


def Func_parseDict(data: dict):
    _CE_ = data["R_DETAIL_DICT"]

    _CE_Boots = _f_parse_item(_CE_["R_EQUIP"]["BOOTS_EQUIP"])
    _CE_Core = _f_parse_item(_CE_["R_EQUIP"]["CORE_EQUIP"])
    _CE_Out = _f_parse_item(_CE_["R_EQUIP"]["OUT_EQUIP"])
    _CE_rune = _f_parse_rune(_CE_["R_RUNE"])
    _CE_Spell = _f_parse_spell(_CE_["R_EQUIP"]["SPELL_INFO"])

    _dict_list = [_CE_Boots, _CE_Core, _CE_Out, _CE_rune, _CE_Spell]

    return _dict_list
