# 登录
# url = "/s-authbiz/oauth/token?grant_type=password"
# data1 = {"data": {"password": "c1234567", "accountNo": "13555555555"},
#          "common": {"appName": "3", "mobileSystem": 1, "mobileEquip": "d6bfdea785d0df20"}}

# 签约信息
# url = "/s-shopbiz/private/v1/shop/getSubscriptionInfo"
# data1 = {"common": {"appName":"3","appVersion":1,"latitude":"39.9488072463536","longitude":"116.450868738107","mobileEquip":"d6bfdea785d0df20","mobileSystem":1},"data":{}}

# 我的合同
# url="/s-shopbiz/private/v1/shop/getPactInfo"
# data1={"common": {"appName":"3","appVersion":1,"latitude":"39.9488072463536","longitude":"116.450868738107","mobileEquip":"d6bfdea785d0df20","mobileSystem":1},"data":{}}

# 规则中心
# url = "/s-shopbiz/private/v1/shop/getRuleInfo"
# data1 = {"common": {"appName": "3", "appVersion": 1, "latitude": "39.9488072463536", "longitude": "116.450868738107","mobileEquip": "d6bfdea785d0df20", "mobileSystem": 1}, "data": {}}

# 业务经理
# url = "/s-shopbiz/private/v1/shop/getServiceManagerInfo"
# data1 = {"common": {"appName": "3", "appVersion": 1, "latitude": "39.9488072463536", "longitude": "116.450868738107","mobileEquip": "d6bfdea785d0df20", "mobileSystem": 1}, "data": {}}

# 常见问题
# url = "/s-shopbiz/private/v1/shop/getServiceManual"
# data1 = {"common": {"appName": "3", "appVersion": 1, "latitude": "39.9488072463536", "longitude": "116.450868738107","mobileEquip": "d6bfdea785d0df20", "mobileSystem": 1}, "data": {}}

# 获取日历信息 showDate
# url="/a-mobileapp/private/v1/buying/getReserveCalender"
# data1={"data":{"poiId":"78465967"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取用餐时段 ruleTime
# url="/a-mobileapp/private/v1/buying/getReserveTimes"
# data1={"data":{"date":"2020-12-03","poiId":"78465967"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取可预订用餐人数范围 minNumber
# url="/a-mobileapp/private/v1/buying/getSupportCustomerNumber"
# data1={"data":{"poiId":"78465967"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取商家预订座位类型状态 seatType 判断：free:true
# url="/a-mobileapp/private/v1/buying/getSeatTypeState"
# data1={"data":{"poiId":"78465967","customerNumber":1,"date":"2020-12-03","time":"09:00|14:00|2020-12-03 09:30:00"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 检查可预订桌位资源
# url="/a-mobileapp/private/v1/buying/validateReserveableSeats"
# data1={"data":{"poiId":"78465967","customerNumber":1,"reserveTime":"09:00|14:00|2020-12-03 09:30:00","seatType":"\u5927\u5385"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取商户楼层信息 floorIdx
# url="/a-mobileapp/public/v1/buying/getFloorsAndZones"
# data1={"data":{"poiId":"78465967"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 根据座位类型获取可用座位
# url="/a-mobileapp/private/v1/buying/getSeatListOfAvailableBySeatType"
# data1={"data":{"poiId":"78465967","customerNumber":1,"date":"2020-12-03","floor":1,"seatType":"\u5927\u5385","time":"09:00|14:00|2020-12-03 09:30:00"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取楼层、区域的可用座位 seatId seatInfoId
# url="/a-mobileapp/private/v1/buying/getSeatListOfAvailableByZoneType"
# data1={"data":{"poiId":"78465967","zoneId":"2000000002755","customerNumber":"1","date":"2020-12-03","floor":1,"time":"09:00|14:00|2020-12-03 09:30:00"},"common":{"mobileSystem":"ios","mobileEquip":"0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取座位详情
# url="/a-mobileapp/private/v1/buying/getSeatDetail"
# data1 = {"data": {"poiId": "78465967","seatId":"2000000001701"}, "common": {"mobileSystem":"ios","mobileEquip": "0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 生成预订单
# url="/a-mobileapp/private/v1/buying/reserveSeat"
# data1={"data": {"poiId": "78465967","seatType":"大厅","customerNumber":1,"reserveDate":"2020-12-03","reserveSeatType":1,"reserveTime":"09:00|14:00|2020-12-03 09:30:00","seatId":2000000001701,"seatType":"大厅","seatInfoId":"78465967-20201203-09:00-14:00-2000000001701","shopDiscount":""}, "common": {"mobileSystem":"ios","mobileEquip": "0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取预订单详情
# url="/a-mobileapp/private/v1/buying/getReserveInfo"
# data1={"data": {"poiId": "78465967"}, "common": {"mobileSystem":"ios","mobileEquip": "0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}

# 获取菜品列表 dishId
# url="/a-mobileapp/private/v1/buying/getCartInfo"
# data1={"data": {"poiId": "47049885"}, "common": {"mobileSystem":"ios","mobileEquip": "0bec12e8676b626a3633ea58c2a4f93c7e46b3ef","latitude":"39.9488072463536","longitude":"116.450868738107"}}

# 添加或删除菜品
# url="/a-mobileapp/private/v1/buying/updateCartDishNum"
# data1={"data": {"poiId": "47049885","dishId":"100000009793","updateInfo":"add"}, "common": {"mobileSystem":"ios","mobileEquip": "0bec12e8676b626a3633ea58c2a4f93c7e46b3ef"}}
