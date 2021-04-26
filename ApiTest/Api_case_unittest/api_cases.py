import json
import unittest

import pytest
from ddt import ddt,file_data
import yaml

from common.RequestUtils import post, get_text, doNormalPost
from common.RequestUtilsClass import KeyRequests


@ddt
class ApiCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.access_token = None

    @file_data('../data/login.yaml')
    def test_login(self,**kwargs):
        print('1')
        kq = KeyRequests()
        data = json.dumps(kwargs['data1'])
        url = kwargs['path']
        res = post(url, data)
        #print(url,'00000')
        value = get_text(res.text,'rtnCode')
        #print(value)
        ApiCases.access_token = get_text(res.text,'access_token')
        ApiCases.refresh_token = get_text(res.text,'refresh_token')
        #print('access_token:',self.access_token,'---','refresh_token:',self.refresh_token)
        self.assertEquals(first='200',second= value,msg= '成功')
        return res

    @file_data('../data/MyModule.yaml')
    def test_ruleCenter(self,**kwargs):
        print('2')
        url = kwargs['RuleCenter_path']
        data = json.dumps(kwargs['data1'])
        token = self.access_token
        res = post(url,data,token)
        value = get_text(res.text, 'rtnCode')
        self.assertEquals(first='200',second= value,msg='成功')
        return res


    @file_data('../data/MyModule.yaml')
    def test_pactInfo(self, **kwargs):
        print('3')
        url = kwargs['path']
        data = json.dumps(kwargs['data1'])
        token = self.access_token
        res = post(url, data, token)
        value = get_text(res.text, 'rtnCode')
        self.assertEquals(first='200', second=value, msg='成功')
        return res


if __name__ == '__main__':
    unittest.main()