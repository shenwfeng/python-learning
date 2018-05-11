import json
import requests
import time


class Dingtalk(object):
    def __init__(self,corip=None,corpsecret=None):
        self.url_dingtalk = "https://oapi.dingtalk.com/"
        self.corip = corip
        self.corpsecret = corpsecret
        self.ACCESS_TOKEN = None
        self.time = None

    def setDingtalk(self,corip,corpsecret):
        self.corip =corip
        self.corpsecret = corpsecret


    def getAccessToken(self):
        # url_Dingtalk = "https://oapi.dingtalk.com/"
        url_GetToken = "{}gettoken?corpid={}&corpsecret={}".format(self.url_dingtalk,self.corip,self.corpsecret)
        result = requests.get(url_GetToken).content.decode('utf-8')
        ACCESS_TOKEN = json.loads(result)
        if ACCESS_TOKEN['errcode'] == 0:
            access_token = ACCESS_TOKEN['access_token']
            self.ACCESS_TOKEN = access_token
            return access_token
        return None

    def getDepartment(self,department):
        if self.ACCESS_TOKEN is not None:
            url = "{}user/simplelist?access_token={}&department_id={}".format(self.url_dingtalk,self.ACCESS_TOKEN,department)
        result = requests.get(url).content.decode("utf-8")
        depar = json.loads(result)
        if depar['errcode'] == 0:
            return depar
        return None

    def getDepartList(self):
        if self.ACCESS_TOKEN is not None:
            url ="{}department/list?access_token={}".format(self.url_dingtalk,self.ACCESS_TOKEN)
        result = requests.get(url).content.decode("utf-8")
        departlist = json.loads(result)
        if departlist['errcode'] == 0:
            return departlist
        return None

    def getUser(self,user):
        if self.ACCESS_TOKEN is not None:
            url = "{}user/get?access_token={}&userid={}".format(self.url_dingtalk,self.ACCESS_TOKEN,user)
        result = requests.get(url).content.decode("utf-8")
        user = json.loads(result)
        if departlist['errcode'] == 0:
            return user
        return None




