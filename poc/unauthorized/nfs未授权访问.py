#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.getIP as getIP
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'NFS未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  ip = getIP.main(url)
  url1 = ip
  ret['url'] = url1
  if ip == None:
    return ret
  try:
    nfs_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nfs_socket.settimeout(3)
    nfs_socket.connect((ip, 2049))
    nfs_socket.sendall(
                b'\x80\x00\x00\x28\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x20\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    response = nfs_socket.recv(1024)
    if b'\x80\x00\x00\x28\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x20\x00\x00\x02\x00\x00\x00\x01' in response:
      ret['ifbug'] = True
      ret['huixian'] = url
      return ret
    else:
      return ret
  except:
    return ret