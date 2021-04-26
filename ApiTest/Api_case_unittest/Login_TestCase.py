import json
import time

from common.RequestUtils import post, get_text
from common.SignUtils import getSignString
import requests


def login():
    url = "/s-authbiz/oauth/token?grant_type=password"
    data1 = {"data": {"password": "c1234567", "accountNo": "13555555555"},"common": {"appName": "3", "mobileSystem": 1, "mobileEquip": "d6bfdea785d0df20"}}
    data = json.dumps(data1)
    res = post(url,data)
    return res
print(login().text)

text = login().text
text_json = json.loads(text)
print(type(text_json))
token = get_text(text,'access_token')




url = "https://uat-shop.citylife.com/shop/api/s-shopbiz/private/v1/shopUser/getShopUserInfo"
data1 = {"data": {},
         "common": {"appName": "3", "mobileSystem": 1, "mobileEquip": "d6bfdea785d0df20"}}
headers = {'Content-Type': 'application/json'}
data = json.dumps(data1)
t = time.time()
timestamp = int(round(t * 1000))
headers["timestamp"] = str(timestamp)
signedStr = getSignString(timestamp,data)
headers["sign"] = signedStr
#headers["Authorization"] = "Basic dGVzdGNsaWVudDpwYXNzd29yZA=="
headers["Authorization"] = "bearer "+ token
headers["mobileEquip"] = "d6bfdea785d0df20"
res = requests.post(url=url,headers=headers,data=data)
print(res.text)
# {
# 	"common": {
# 		"appName": "com.citylife.business",
# 		"appVersion": "0.1.0",
# 		"mobileSystem": "iOS",
# 		"platform": "iOS",
# 		"mobileEquip": "0C78A3FD-1325-4C14-95F0-380F22FAA2F6"
# 	},
# 	"data": {}
# }
