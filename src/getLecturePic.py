import requests
import re
import hashlib

jwkUrl = 'http://jwk.njfu.edu.cn/'
jwkLoginUrl = 'http://jwk.njfu.edu.cn/_data/login_home.aspx'
userid = ''
pwd = '3021STOP'

loginSession = requests.session()

# Get sessionID
res = loginSession.get(jwkUrl).text
sessionID = loginSession.cookies["ASP.NET_SessionId"]

# Get __VIEWSTATE, __VIEWSTATEGENERATOR, __EVENTVALIDATION
res = loginSession.get(jwkLoginUrl).text
VIEWSTATE = re.findall(r'''name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)"''', res)[0]
VIEWSTATEGENERATOR = re.findall(r'''name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)"''', res)[0]
EVENTVALIDATION = re.findall(r'''name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)"''', res)[0]

print(VIEWSTATE)
print(VIEWSTATEGENERATOR)
print(EVENTVALIDATION)

# Convert userid, pwd and university code by md5
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()
dsdsdsdsdxcxdfgfg = md5(userid + md5(pwd)[:30].upper() + "10298")[:30].upper()
print(dsdsdsdsdxcxdfgfg)

data = {
    "__VIEWSTATE": VIEWSTATE,
    "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
    "__EVENTVALIDATION": EVENTVALIDATION,
    "pcInfo": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36undefined5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 SN:NULL",
    "txt_mm_expression": "",
    "txt_mm_length": "",
    "txt_mm_userzh": "",
    "typeName": "学生".encode('gb2312'),
    "dsdsdsdsdxcxdfgfg": dsdsdsdsdxcxdfgfg,
    "fgfggfdgtyuuyyuuckjg": "",
    "validcodestate": "0",
    "Sel_Type": "STU",
    "txt_asmcdefsddsd": userid,
    "txt_pewerwedsdfsdff": "",
    "txt_psasas": "请输入密码".encode('gb2312')
}

loginSession.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://jwk.njfu.edu.cn/_data/login_home.aspx'
})

# Loginto njfu jwk
res = loginSession.post(jwkLoginUrl, data=data)

# Get lecture from jwk
res = loginSession.get(url='http://jwk.njfu.edu.cn/wsxk/stu_zxjg_rpt.aspx?param_xh=')
#with open("res.html", "w") as html:
#    html.write(res.text)
res = loginSession.get(url='http://jwk.njfu.edu.cn/znpk/DrawKbimg.aspx?w=1153&h=300&xn=2021&xq=1&zfx=0&type=xzxjg')
#print(res.text)
with open("lecture.jpg", "wb") as pic:
    pic.write(res.content)
