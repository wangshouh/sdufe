import requests
import io
import json
import base64
from PIL import Image


def ocrapi(imagestream, API_KEY, SECRET_KEY):
    '''
    调用百度云OCR API进行验证码破解    
    '''
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(API_KEY, SECRET_KEY)
    response = requests.get(host)
    if response:
        access_token = response.json()['access_token']
    params = {"image":imagestream}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()

def getverify(cookies):
    '''
    获取验证码
    '''
    imagetest = requests.get('http://bcfl.sdufe.edu.cn/index.php?g=api&m=checkcode&a=index', cookies=cookies)
    imagebody = imagetest.content
    imagestream = base64.b64encode(imagebody)
    try:
        verify = ocrapi(imagestream, API_KEY, SECRET_KEY)['words_result'][0]['words']
    except:
        verify = 0000
    return verify

def getcookie(headers):
    '''
    获取Cookie
    '''
    url = 'http://bcfl.sdufe.edu.cn/index/login'
    with requests.Session() as s:
        r = s.post(url,headers=headers)
        cookies = {'PHPSESSID': requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']}
    return cookies


def login(cookies,headers,number,card):
    '''
    进行登录
    '''
    loopcount = 0
    logincode = 201
    loginurl = 'http://bcfl.sdufe.edu.cn/Student/handle_login'
    while logincode == 201:
        try:
            verify = getverify(cookies)
            data = 'number={}&card={}&verify={}'.format(number, card, verify)
            response = requests.post(url=loginurl,headers=headers,data=data,cookies=cookies)
            logincode = response.json()['code']
        except:
            logincode = 201
        loopcount += 1
        print('{} is {}'.format(loopcount, logincode))
    
    
    print('finish login...')

def register(cookies,headers, basicinfo):
    '''
    进行打卡操作
    '''
    loopcount = 0
    registercode = 201
    registerurl = 'http://bcfl.sdufe.edu.cn/Student/handle_ext_do'
    while registercode == 201:
        try:
            verify = getverify(cookies)
            info =  basicinfo + 'verify={}'.format(verify)
            response = requests.post(url=registerurl,headers=headers,data=info,cookies=cookies)
            registercode = response.json()['code']
        except:
            verifycode = 201
        loopcount += 1
        print('{} is {}'.format(loopcount, registercode))
        
    print('finish register!')



headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0','Referer':'http://bcfl.sdufe.edu.cn/index/login.html', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With':'XMLHttpRequest','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host':'bcfl.sdufe.edu.cn','Accept': '*/*'}
#cookies = {'cookies':'4BBnnC_think_language=en;PHPSESSID=b120725ab5eb12b9969ea32e0c9428c5'}

#以下内容请自行修改
number =  #学号
card =  #密码

#打卡基础信息，请自行查阅JS代码填写
basicinfo = 

#以下内容请自行查阅百度智慧云控制台
API_KEY = 
SECRET_KEY = 




cookies = getcookie(headers)
login(cookies,headers, number, card)
register(cookies,headers, basicinfo)