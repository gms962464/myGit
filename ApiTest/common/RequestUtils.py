import requests
import time
from common .SignUtils import getSignString
from requests .packages import urllib3
import jsonpath
import json


def post(url, data,token = None):
    """
    做post请求，获取返回值
    :param url: 请求的全地址
    :param data: json格式数据，这里没考虑其他格式
    :return: 请求的返回值
    """
    print("do post" + data)
    t = time.time()
    timestamp = int(round(t * 1000))
    signedStr = getSignString(timestamp,data)
    #print(signedStr)
    # 设置header的内容
    headers = {'Content-Type': 'application/json'}
    headers["timestamp"] = str(timestamp)
    headers["sign"] = signedStr
    # headers["sign"] = "oOEEQGN8uWGSPf0beJnll0Mmg57m7C2kMKILyv2JnbqdqeVbPSUkNIo/Xo+/ViMHtaIk9MPKMzZ+WonYeAy65LOUkfqbiQVDTuArugEyHEmk2Uwr/4vZK3n5ud1PuHGxq5XSoAHr8pjS99sVkAi5JjSkoGgoh+gNeflkpJpeJZQ="
    if token is not None:
        headers["Authorization"] = "bearer "+ token
    else:
        headers["Authorization"] = "Basic dGVzdGNsaWVudDpwYXNzd29yZA=="
    #headers["Authorization"] = "Basic dGVzdGNsaWVudDpwYXNzd29yZA=="
    headers["mobileEquip"] = "d6bfdea785d0df20"
    # headers["mobileEquip"] = "d6bfdea785d0df20"
    urllib3.disable_warnings()
    # 用户
    #tempUrl="https://uat-app.citylife.com/mobile/api"
    # 商誉
    tempUrl="https://uat-shop.citylife.com/shop/api"
    res = requests.post(tempUrl+url, headers=headers, data=data,verify=False)
    return res

def doNormalPost(url, data):
    """
    做不加密的请求
    :param url: 请求的全地址
    :param data: json格式数据，这里没考虑其他格式
    :return: 请求的返回值
    """
    print("do normal post" + data)
    # 设置header的内容
    headers = {'Content-Type': 'application/json'}
    res = requests.post("https://uat-app.citylife.com/mobile/api"+url, headers=headers, data=data)
    return res

def get(url, data):
    """
    做get请求
    :param url:
    :param data:
    :return:
    """
    print("do get" + data)
    res = requests.get("https://uat-app.citylife.com/mobile/api"+url, params=data)
    return res

def get_text(res, key):
    if res is not None:
        try:
            text = json.loads(res)
            value = jsonpath.jsonpath(text, '$..{0}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
            return value
        except Exception as e:
            return e
    else:
        return None