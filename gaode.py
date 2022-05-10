from audioop import add
import json
import requests as rq

Header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}


def getAddressInfo(address):
    """根据地址获取经纬度

    Args:
        address (str): 地址描述

    Returns:
        str: 高德地址解码api返回的地址相关信息
    """
    qkey = "高德开放平台申请的key"
    city = "郑州"
    params = {"key": qkey, "city": city, "address": address}
    result = rq.get("https://restapi.amap.com/v3/geocode/geo",
                    headers=Header, params=params)

    return result.text


def getPos(address):
    """根据地址获取经纬度

    Args:
        address (str): 地址描述

    Returns:
        list: 地址的经纬度
    """
    print("address=======>:"+address)
    addressInfo = getAddressInfo(address=address)
    j = json.loads(addressInfo)
    print(j)
    pos = j['geocodes'][0]['location'].split(',')
    poslist = [float(pos[0]), float(pos[1])]
    return poslist


print(getPos("中孚大厦10楼(黄河路26号)"))
