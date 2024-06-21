<h1>使用注意点</h1>
<h2>强调</h2>
本文使用的工具和方法仅限学习交流使用，请不要将文中使用的工具和渗透思路用于任何非法用途，对此产生的一切后果，本人不承担任何责任，也不对造成的任何误用或损害负责。
<h2>使用注意点</h2>
<ol>
<li>只要不删除、增加、修改poc的文件名，都不需要“-up”。</li>
<li>增加、删除poc,或者修改poc的文件名，都需要执行“-up”</li>
<li>可以在poc目录下移动poc至你认为合适的目录下，只要在移动后执行“-up”即可</li>
<li>由于个人精力有限，现有poc未一一验证，存在误报或poc错误的情况；</li>
</ol>
<h2>用法</h2>

<h3>一、准备工作</h3>

安装python模块</br>

`pip install -r requirements.txt`</br>

如网络异常可指定源安装</br>

`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`</br>

<h3>二、用法示例</h3>

1、安装完模块后一定要先进行poc初始化，否则脚本无法读取任何poc

`python xiaofeixia-sec.py -up`

2、对一个网站执行所有poc

`python xiaofeixia-sec.py -u http://www.tesssst.com -a`</br>

3、匹配某些poc进行扫描

`python xiaofeixia-sec.py -u http://www.tesssst.com -s `弱口令</br>

4、批量poc扫描(不支持同时匹配,目前只能匹配一个关键字，如：-s tomcat nginx是不支持的)

`python xiaofeixia-sec.py -f targets.txt -s tomcat`</br>

5、扫描到的漏洞会记录到log目录下的文件，按照日期命名;</br>

6、“-pl”列出当前所有的poc信息;

`python xiaofeixia-sec.py -pl`</br>

7、“debug”只能输出部分语法错误，这部分以后改进;</br>

`python xiaofeixia-sec.py -debug`</br>

8、需要配置邮箱和授权码，最好是qq邮箱，其他的没配置，发现漏洞后可以直接邮件通知，不需要一直盯着，配置文件在config目录下;</br>

9、邮件发送过快可能会被qq限制，导致收不到邮件;</br>

<h2>poc编写规范</h2>

例：

```
def msg():
  ret = {

     'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'HIKVISION 流媒体管理服务器 user.xml 账号密码泄漏',

      'level'     :   'critical',

      'FOFA'      :   '"杭州海康威视系统技术有限公司 版权所有" && title="流媒体管理服务器"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/26',
  	}
 	return ret
```
一般在弱口令poc中要获取location,
if res.status_code == 302 and '/out/out.ViewFolder.php' in res.headers['location']
需要指定allow_redirects=False，如下
res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)

```
##
如果需要dnslog，脚本里需要引入
import script.DnsLog as dnslog
dnslog.get_domain()#返回domain和cookie

用法：domain,cookie = dnslog.get_domain()
dnslog.get_result(domain,cookie)#传入domain和cookie两个参数，参数从get_domain()获取。返回True或False,True表示检测到回显，False表示未检测到回显
用法：
if dnslog.get_result(domain,cookie) == True:
	print('存在漏洞')#具体用法根据poc进行修改
##

如果需要获取网站IP，可以在脚本内任意poc导入
import script.getIP as getIP
def run():
	ip = getIP.main(url)
	if ip == None:#如果返回None,则代表未获取到IP地址，可以直接返回ret信息了。
	    return ret
	#继续检测



poc分类优先级
##
除OA、CMS外，其它均按照现有类型分类

##用法##
如果poc的数量或名称有变动，需要先执行`-up`更新配置文件
如果执行无任何输出则可能语法有误，可尝试执行`-debug`来调试

有漏洞的返回值里必须有url,无漏洞的可以没有，即
ret['url'] = url1

如有问题请与小飞侠联系，支持请点个star
请联系：3484762639#qq.com（所有数字减1并将#替换为@）
```
