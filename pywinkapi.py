# Класс авторизации в wink
# 

import json
from http.client import HTTPSConnection
import time

'''
index.html
      window.__ENVIRONMENT__ = "production";
      window.__GTM_ID__ = "GTM-PBF7T3T";
      window.__SENTRY_DSN_BROWSER__ = "https://a532fbe84193426890b2ea72583494e7@sentry.iptv.rt.ru/5";
      window.__BALANCER_ENDPOINT__ = "https://balancer.svc.iptv.rt.ru";
      
      window.__INITIAL_PAGE__ = {"status":200,"pathname":"/tv","search":"","match":{"path":"/tv","url":"/tv/","isExact":true,"params":{}},"name":"screen"};
      window.__REVISION__ = "v2021.05.20.1348";
      window.__IMAGES_URL__ = "https://s26037.cdn.ngenix.net";
      window.__ALICE_ID__ = "7ab25b6a-30ae-4a5a-a67c-7996068e89ba";
      window.__REQUEST_ID__ = "b5b2f41d1e4950ce0fc10438be953194";
      window.__OMNICHAT__ ="";
      window.__PUBLIC_KEY_CAPTCHA__ = '6Lfr_pkUAAAAAAotvpbJ1pUirS8vdXfmQczg4DYg';
      __webpack_public_path__ = "";

Request URL: https://sentry.iptv.rt.ru/api/5/envelope/?sentry_key=a532fbe84193426890b2ea72583494e7&sentry_version=7
Request Method: POST
Status Code: 200 
Remote Address: 188.254.0.59:443
Referrer Policy: origin
access-control-allow-origin: https://wink.rt.ru
access-control-expose-headers: x-sentry-error, x-sentry-rate-limits, retry-after
content-length: 2
content-type: application/json
date: Fri, 21 May 2021 14:14:42 GMT
server: nginx/1.14.1
strict-transport-security: max-age=31536000
vary: Origin

:authority: sentry.iptv.rt.ru
:method: POST
:path: /api/5/envelope/?sentry_key=a532fbe84193426890b2ea72583494e7&sentry_version=7
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
content-length: 353
content-type: text/plain;charset=UTF-8
origin: https://wink.rt.ru
referer: https://wink.rt.ru/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36

sentry_key: a532fbe84193426890b2ea72583494e7
sentry_version: 7
{"sent_at":"2021-05-21T14:14:42.009Z","sdk":{"name":"sentry.javascript.browser","version":"6.4.1"}}
{"type":"session"}
{"sid":"3aa08b91b1144b5eb43fac86521d750e","init":true,"started":"2021-05-21T14:14:42.008Z","timestamp":"2021-05-21T14:14:42.008Z","status":"ok","errors":0,"duration":0,"attrs":{"release":"v2021.05.20.1348","environment":"production"}}
'''

class pyWinkConnect(object):
    def __init__(self, login = 'demo', password = ''):
        self.server_wink = 'cnt-odcv-itv01.svc.iptv.rt.ru'
        self.folder_wink = '/api/v2/portal/'
        self.session_id = '198437ee-5694-11eb-9bfa-341e6b49f8b2:1951416:2237006:2'
        self.uid = 'mHJFymgafeiba0kVum6OJ' #'bVqye0S0Nfa_7S4VoEQtg' #'mHJFymgafeiba0kVum6OJ'
        self.origin = 'https://wink.rt.ru'
        self.referer = 'https://wink.rt.ru/'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        self.x_wink_version = 'v2021.05.20.1348'
        self.session_state = 'demo'

    def get_url_wink(self, _service = ''):
        return 'https://' + self.server_wink + self.folder_wink + _service

    def get_server_wink(self):
        return self.server_wink

    def get_header(self):
        _header = {
            'accept':'application/json, text/plain, */*',
            'origin': self.origin,
            'referer': self.referer,
            'User-agent': self.user_agent,
            'x-wink-version':self.x_wink_version,
            'session_id':self.session_id
            }
        print(_header)
        return _header

    def update_session_id(self):
        '''Получение свежего токена {"fingerprint":"N1O6paSBkElcapY6Nh5Yz"}'''
        '''https://cnt-odcv-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens'''
        print('==== update_session_id ===\n\r')
        header = self.get_header()
        conn = HTTPSConnection('cnt-odcv-itv01.svc.iptv.rt.ru')
        conn.debuglevel = 5
        _body = '{"fingerprint":"%s"}' % self.uid
        conn.request("POST","/api/v2/portal/session_tokens", headers = header, body = _body )
        res = conn.getresponse()
        resJson = json.loads(res.read().decode('utf-8'))
        print(res.status)
        print(res.getheaders())
        self.session_id = resJson['session_id']
        self.session_state = resJson['session_id']
        print(resJson)
        return resJson

    def set_collector(self):
        ''' POST https://cnt-lbrc-itv02.svc.iptv.rt.ru/event_collector '''
        print('==== set_collector ===\n\r')
        header = self.get_header()
        conn = HTTPSConnection('cnt-lbrc-itv02.svc.iptv.rt.ru')
        conn.debuglevel = 5
        '''
        {"events":[{"utc":1621623815597,"uid":"mHJFymgafeiba0kVum6OJ","session_id":"3e478943-ba67-11eb-a6e7-f063f976f300:1951416:2237006:2","san":"ct_nc_web_portal","auth_mode":"anonymous","is_test":0,"profile_id":590473,"session_type":"demo","sw_version":"v2021.05.20.1348","external_link":"/tv/","category":"Жизненный цикл продукта","action":"Запуск приложения","label":"Запуск","device_type":"NCWEB","user_value":5},{"utc":1621623815600,"uid":"mHJFymgafeiba0kVum6OJ","session_id":"3e478943-ba67-11eb-a6e7-f063f976f300:1951416:2237006:2","san":"ct_nc_web_portal","home_mrf":"ct","current_mrf":"sth","home_location":100001,"home_sub_location":100001,"cur_location":400008,"cur_sub_location":400008,"real_ip":"194.156.184.119","category":"Жизненный цикл продукта","action":"Геолокация устройства","user_value":2},{"utc":1621623815671,"uid":"mHJFymgafeiba0kVum6OJ","session_id":"3e478943-ba67-11eb-a6e7-f063f976f300:1951416:2237006:2","san":"ct_nc_web_portal","category":"Интерфейс","action":"Показ страницы","user_value":1,"label":"screen","title":"","path":"/tv"}]}
        '''
        utc_sec = int(time.time())
        event = {'utc':utc_sec,
            'uid':self.uid,
            'session_id':self.session_id,
            'san':'ct_nc_web_portal',
            'auth_mode':'anonymous',
            'is_test':0,
            'profile_id':590473,
            'session_type':'demo',
            'sw_version':self.x_wink_version,
            'external_link':'/tv/',
            'category':'Жизненный цикл продукта',
            'action':'Запуск приложения',
            'label':'Запуск',
            'device_type':'NCWEB',
            'user_value':5}
        
        _body = {"events":[event]}
        conn.request("POST","/event_collector", headers = header, body = json.dumps(_body) )
        res = conn.getresponse()
        print(res.status)
        print(res.getheaders())
        #self.session_id = resJson['session_id']
        #self.session_state = resJson['session_id']
        print(res.read().decode('utf-8'))
        return res.status == 200

class pyWinkApi(object):
    def __init__(self, _session = None):
        if _session is None:
            self.session = pyWinkConnect()
            self.session.update_session_id()
            self.session.set_collector()
        else:
            self.session = _session

    def get_channels(self):
        pass

    def set_event(self):
        pass

    def load_channels(self ):
        ''' Запрашивает список каналов '''
        ''' https://cnt-lbrc-itv01.svc.iptv.rt.ru/api/v2/portal/channels?limit=30&offset=0&with_epg=true&epg_limit=3 '''
        print('==== load channels ===\n\r')
        header = self.session.get_header()
        conn = HTTPSConnection('cnt-lbrc-itv01.svc.iptv.rt.ru' )
        conn.debuglevel= 5
        conn.request("GET","/api/v2/portal/channels?limit=30&offset=0&with_epg=true&epg_limit=3", headers = header )
        res = conn.getresponse()
        resJson = json.loads(res.read().decode('utf-8'))
        print(res.status)
        print(res.getheaders())
        print(resJson)
        return resJson