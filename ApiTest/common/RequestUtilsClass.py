import json
import time

import jsonpath
import requests
import urllib3

from common.SignUtils import getSignString


class KeyRequests:
    def post(self,url,data):
        """
        做post请求，获取返回值
        :param url: 请求的全地址
        :param data: json格式数据，这里没考虑其他格式
        :return: 请求的返回值
        """
        print("do post" + data)
        t = time.time()
        timestamp = int(round(t * 1000))
        signedStr = getSignString(timestamp, data)
        # print(signedStr)
        # 设置header的内容
        headers = {'Content-Type': 'application/json'}
        headers["timestamp"] = str(timestamp)
        headers["sign"] = signedStr
        # headers["sign"] = "oOEEQGN8uWGSPf0beJnll0Mmg57m7C2kMKILyv2JnbqdqeVbPSUkNIo/Xo+/ViMHtaIk9MPKMzZ+WonYeAy65LOUkfqbiQVDTuArugEyHEmk2Uwr/4vZK3n5ud1PuHGxq5XSoAHr8pjS99sVkAi5JjSkoGgoh+gNeflkpJpeJZQ="
        # headers["Authorization"] = "Basic dGVzdGNsaWVudDpwYXNzd29yZA=="
        headers["Authorization"] = "Basic dGVzdGNsaWVudDpwYXNzd29yZA=="
        headers["mobileEquip"] = "d6bfdea785d0df20"
        # headers["mobileEquip"] = "d6bfdea785d0df20"
        urllib3.disable_warnings()
        # 用户
        # tempUrl="https://uat-app.citylife.com/mobile/api"
        # 商誉
        tempUrl = "https://uat-shop.citylife.com/shop/api"
        res = requests.post(tempUrl + url, headers=headers, data=data, verify=False)
        return res

    def get_text(self, res, key):
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