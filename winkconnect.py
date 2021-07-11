import ssl
from http.client import *
from html.parser import HTMLParser
from urllib.parse import urlparse
import json
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'



class ParseJS(HTMLParser):
    def __init__(self):
        self._data = []
        self._current_tag = ''
        super().__init__()   

    def handle_starttag(self,tag,attrs):
        self._current_tag = tag
        if tag == 'script':
            #print(attrs)
            pass
        pass
    def handle_endtag(self,tag):
        self._current_tag = ''
        pass
    def handle_data(self,data):
        if self._current_tag == 'script':
            
            arr_data = data.split('\n')
            for arr in arr_data:
                arr = arr.replace('      ', '').replace(' =','=').replace(' = ','=').replace('= ','=')
                if arr.find('window.__ENVIRONMENT__') != -1:
                    value = arr.replace('window.__ENVIRONMENT__="','').replace('";','')
                    self._data.append({'__ENVIRONMENT__':value})
                elif arr.find('window.__GTM_ID__=') != -1:
                    value = arr.replace('window.__GTM_ID__="','').replace('";','')
                    self._data.append({'__GTM_ID__':value})
                elif arr.find('window.__SENTRY_DSN_BROWSER__=') != -1:
                    value = arr.replace('window.__SENTRY_DSN_BROWSER__="','').replace('";','')
                    self._data.append({'__SENTRY_DSN_BROWSER__':value})
                elif arr.find('window.__BALANCER_ENDPOINT__=') != -1:
                    value = arr.replace('window.__BALANCER_ENDPOINT__="','').replace('";','')
                    self._data.append({'__BALANCER_ENDPOINT__':value})
                elif arr.find('window.__REVISION__=') != -1:
                    value = arr.replace('window.__REVISION__="','').replace('";','')
                    self._data.append({'__REVISION__':value})
                elif arr.find('window.__IMAGES_URL__=') != -1:
                    value = arr.replace('window.__IMAGES_URL__="','').replace('";','')
                    self._data.append({'__IMAGES_URL__':value})
                elif arr.find('window.__ALICE_ID__=') != -1:
                    value = arr.replace('window.__ALICE_ID__="','').replace('";','')
                    self._data.append({'__ALICE_ID__':value})
                elif arr.find('window.__REQUEST_ID__=') != -1:
                    value = arr.replace('window.__REQUEST_ID__="','').replace('";','')
                    self._data.append({'__REQUEST_ID__':value})
                elif arr.find('window.__RECAPTCHA_CLIENT__=') != -1:
                    value = arr.replace('window.__RECAPTCHA_CLIENT__="','').replace('";','')
                    self._data.append({'__RECAPTCHA_CLIENT__':value})
                elif arr.find('window.__INITIAL_PAGE__=') != -1:
                    value = arr.replace('window.__INITIAL_PAGE__=','').replace(';','')
                    self._data.append({'__INITIAL_PAGE__':value})
                elif arr.find('window.__MOBX_STATE__=') != -1:
                    value = arr.replace('window.__MOBX_STATE__=','').replace(';','')
                    self._data.append({'__MOBX_STATE__':value})

                #else:
                #    print(arr)
        pass


class WinkParams:
    __ENVIRONMENT__ = ''
    __GTM_ID__ = ''
    __SENTRY_DSN_BROWSER__ = ''
    __BALANCER_ENDPOINT__ = ''
    __MOBX_STATE__ = None
    __INITIAL_PAGE__ = None
    __REVISION__ = ''
    __IMAGES_URL__ = ''
    __ALICE_ID__ = ''
    __REQUEST_ID__ = ''
    __OMNICHAT__ = ''
    __PUBLIC_KEY_CAPTCHA__ = ''
    __webpack_public_path__ = ''
    _ready_list = []
    _api_params = []
    def __init__(self,url_service, last_cookie=''):
        self._url = url_service
        self.__last_cookie = last_cookie
        self.load_index_page()
        pass

    def get_param_api(self,ind,level=0):
        el = len([x for x in self._ready_list if ind == x])
        vvv = '>'
        for i in range(level):
            vvv += '>'
        #if el != 0 :
        #    print('===== Err {0} ====='.format(ind))
        #    return self.__MOBX_STATE__[ind], True
        try:
            list_item = self.__MOBX_STATE__[ind]
        except:
            print('Error {0}'.format(ind))
            return '', True
        #print('{3} {0} : {2} {1}'.format(ind, list_item, str(type(list_item)),vvv))
        self._ready_list += [ind]
        res = []
        if isinstance(list_item, dict) and len(list_item) != 0:
            param_api_1 = {}
            for item_d in list_item:  
                value_p = list_item[item_d]
                    
                if isinstance(value_p, bool) :
                    param_api_1[item_d] = value_p 
                elif isinstance(value_p, int) :
                    param_api_1[item_d] = value_p
                elif isinstance(value_p, str) :

                    #print(item_d + ' : ' + str(type(value_p)) + str(type(self.__MOBX_STATE__[int(value_p)])))  
                    if item_d == 'id' or  item_d == 'root' or  item_d == 'api' or item_d == 'tstv_valid_until' :
                        param_api_1[item_d] = value_p
                    elif value_p.isdigit() :
                        res_a , err = self.get_param_api(int(value_p),level+1)
                        param_api_1[item_d] = res_a
                    else:
                        param_api_1[item_d] = list_item[item_d]
                else:
                    param_api_1[item_d] = list_item[item_d]
            res += [param_api_1]
            #print('Append params {0}: {1}'.format(ind, param_api_1))
                
            return param_api_1, False
        elif isinstance(list_item, list) :
            res_a = []
            for item_d_1 in list_item:
                if isinstance(item_d_1,str) and item_d_1.isdigit():
                    res_b, err = self.get_param_api(int(item_d_1),level+1)
                    res_a += [res_b]
                else:
                    res_a += [item_d_1]
            return res_a , False
        elif isinstance(list_item, str):
            return self.__MOBX_STATE__[ind], False
        else:
            #print('Set {0} {1} '.format(ind, self.__MOBX_STATE__[ind]))
            return self.__MOBX_STATE__[ind], False
        

    def load_index_page(self):
        conn = HTTPSConnection(urlparse(self._url).netloc)
        conn.set_debuglevel(5)
        header = {'user-agent':USER_AGENT}
        if len(self.__last_cookie ) != 0:
            header['cookie'] = self.__last_cookie 
        conn.request("GET",urlparse(self._url).path, headers=header)
        resp = conn.getresponse()
        data = resp.read().decode('utf-8')
        parser = ParseJS()
        parser.feed(data)
        for item in parser._data:
            for key in item:
                if key == '__ENVIRONMENT__':
                    self.__ENVIRONMENT__ = item[key]
                elif key == '__GTM_ID__':
                    self.__GTM_ID__ = item[key]
                elif key == '__SENTRY_DSN_BROWSER__':
                    self.__SENTRY_DSN_BROWSER__ = item[key]
                elif key == '__IMAGES_URL__':
                    self.__IMAGES_URL__ = item[key]
                elif key == '__REVISION__':
                    self.__REVISION__ = item[key]
                elif key == '__PUBLIC_KEY_CAPTCHA__':
                    self.__PUBLIC_KEY_CAPTCHA__ = item[key]
                elif key == '__MOBX_STATE__':
                    self.__MOBX_STATE__ = json.loads( item[key])
                elif key == '__INITIAL_PAGE__':
                    self.__INITIAL_PAGE__ = json.loads( item[key])
        #print(self.__MOBX_STATE__)                                
        #print('=========================================================')
        for _ind_ in range(len(self.__MOBX_STATE__)):
            
            el = len([x for x in self._ready_list if _ind_ == x])
            
            if el != 0 :
                #print('===== Continue =====')
                continue
            list_item = self.__MOBX_STATE__[_ind_]
            #print('================= ELEM    :{0} =  {1} ============='.format(el,_ind_))
            if isinstance(list_item, dict):
                #print(str(_ind_) + ' : ' +str( list_item))
                _list_item = {}
                for item_d in list_item:
                    if item_d != 'id' and item_d != 'root' and item_d != 'tstv_valid_until' and item_d != 'api': 
                        err = False
                        #print(item_d)            
                        if isinstance(list_item[item_d], str) and list_item[item_d].isdigit():           
                            res1, err = self.get_param_api(int(list_item[item_d]))
                        else:
                            res1 = list_item[item_d]
                        if err :
                            #print('ERROR : ' + item_d)
                            break
                    else:
                        res1 = list_item[item_d]
                    _list_item[item_d]  = res1
                    
                #print('RESULT: {0}'.format(_list_item))
                self._api_params += [_list_item]                     
            else:
                pass        
            
            self._ready_list += [_ind_]
        #print(self._api_params)
        print('================= END =============')    
##############################################################################

class WincClientConnection:
    __last_cookie = ''
    _params_api = []
    _tv = []
    _request_id = ''
    _preauthorization = ''
    _current_channel = {}

    def __init__(self, params = None, tv = None):
        if params is None:
            self._params_api = WinkParams('https://wink.rt.ru')
        else:
            self._params_api = params
        if tv is None:
            self._tv = WinkParams('https://wink.rt.ru/tv')
        else:
            self._tv = params
        self._api_endpoint = self._params_api._api_params[0]['balancerStore']['urls']['api_url']
        self._api_endpoint_img = self._params_api._api_params[0]['balancerStore']['urls']['img_url']

        self._request_id = self._params_api._api_params[0]['apiService']['requestId']
        self._fairplay_license_server_urls = self._params_api._api_params[0]['applicationStore']['drmSettingsStore']['drmSettings']['license_server_urls']['fairplay']
        self._fairplay_cert_url = self._params_api._api_params[0]['applicationStore']['drmSettingsStore']['drmSettings']['fairplay_cert_url']
        self._session_id = self._params_api._api_params[0]['sessionsStore']['currentSession']['session_id']
        self._cert_bin = self.get_service_bin(self._fairplay_cert_url)
        self._license_bin = self.get_service_bin(self._fairplay_license_server_urls)
        
        pass
    
    def get_tv_playlist(self):
        res = []
        for el in self._tv._api_params:
            if not el.get('id') is None:
                res += [el]
        return res

        pass
    def get_token_key(self, channel_id):
        #https://yug-rndn-itv02.svc.iptv.rt.ru/api/v2/portal/content_drm_token?content_type=channel&content_id=1131048
        tmp_url = self._api_endpoint+'api/v2/portal/content_drm_token?content_type=channel&content_id='+str(channel_id)
        print(tmp_url)
        tmp_token = json.loads( self.get_service(tmp_url))        
        self._preauthorization = tmp_token.get('token')
        return self._preauthorization
        pass
    def load_cert_ott(self, key_url):
        # post https://s95951.cdn.ngenix.net/license
        tmp_token = self.get_service_bin(key_url)

        token = self.get_token_key(self._current_channel['id'])

    def get_image_url(self, path_image):
        return '{0}{0}'.format(self._params_ap.__IMAGES_URL__, path_image)

    def get_list_channels(self):
        #url = 'https://yug-rndn-itv02.svc.iptv.rt.ru/api/v2/portal/channels?limit=30&offset=90&with_epg=true&epg_limit=3'
        tmp_url = self._api_endpoint+'api/v2/portal/channels?with_epg=true&epg_limit=3'
        tmp_ch_list = json.loads( self.get_service(tmp_url))
        ch_list = tmp_ch_list['items']
        ch_list.sort(key = lambda x : x['nc_channel_id'])
        for item in ch_list:
            print('{0} {1}'.format(item['nc_channel_id'], item['name']))
        return ch_list

    def get_channel_url(self, url):
        #https://s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/variant.m3u8
        tmp_url = self._api_endpoint+'api/v2/portal/channels/nc/'+url
        print(tmp_url)
        ch_params = json.loads( self.get_service(tmp_url))
        print(ch_params)
        self._current_channel = ch_params
        if isinstance(ch_params,dict) :
            if ch_params.get( 'error_code') is None:
                #print(ch_params)
                print(ch_params['preview_duration'])        
                print(ch_params['name'])
                print(ch_params['description'])
                print(ch_params['logo'])
                #print(ch_params['sources'])    
                if ch_params.get('is_crypted')  :
                    self.load_cert_ott('https://s40757.cdn.ngenix.net/certificates/8BA6D7AC942DE15E1B375DEF7FA20918757A6533')             
                if ch_params.get('sources') is None:
                    return ch_params['description'] , True
                else:
                    self._current_channel = ch_params
                    return ch_params['sources'][0]['url'] , False

            else:
                return ch_params['description'] , True

    def get_service(self, url):
        #options
        conn = HTTPSConnection(urlparse(url).netloc)
        conn.set_debuglevel(5)
        header = {'user-agent':USER_AGENT}
        conn.request('OPTIONS',urlparse(url).path,  headers=header)
        resp = conn.getresponse()
        data = resp.read().decode('utf-8')
        secur_header = resp.getheader('Access-Control-Allow-Headers')
        header['origin'] = 'https://wink.rt.ru'
        header['referer'] = 'https://wink.rt.ru/'
        #print(dir(self._params_api))
        if secur_header.find('X-Wink-Version') != -1:
            header['x-wink-version'] = self._params_api.__REVISION__
        if secur_header.find('X-Wink-Version') != -1:
            header['session_id'] = self._session_id
        if secur_header.find('PreAuthorization') != -1:
            header['preauthorization'] = self._preauthorization
        print(header)      
        conn = HTTPSConnection(urlparse(url).netloc)
        conn.set_debuglevel(5)
        conn.request('GET',urlparse(url).path,  headers=header)
        resp = conn.getresponse()
        data = resp.read().decode('utf-8')
        print(data) 
        return data       
        pass

    def get_service_bin(self, url):
        #options
        conn = HTTPSConnection(urlparse(url).netloc)
        conn.set_debuglevel(5)
        header = {'user-agent':USER_AGENT}
        conn.request('OPTIONS',urlparse(url).path,  headers=header)
        resp = conn.getresponse()
        data = resp.read().decode('utf-8')
        secur_header = resp.getheader('Access-Control-Allow-Headers')
        header['origin'] = 'https://wink.rt.ru'
        header['referer'] = 'https://wink.rt.ru/'
        #print(dir(self._params_api))
        if secur_header.find('X-Wink-Version') != -1:
            header['x-wink-version'] = self._params_api.__REVISION__
        if secur_header.find('X-Wink-Version') != -1:
            header['session_id'] = self._session_id
        if secur_header.find('PreAuthorization') != -1:
            header['preauthorization'] = self._preauthorization
        print(header)      
        conn = HTTPSConnection(urlparse(url).netloc)
        conn.set_debuglevel(5)
        conn.request('GET',urlparse(url).path,  headers=header)
        resp = conn.getresponse()
        data = resp.read()
        print(data) 
        return data       
        pass
##############################################################################


if __name__ == "__main__":
    conn = WinkParams('https://wink.rt.ru')
    ind = 0
    print(conn.__INITIAL_PAGE__)
    for item in conn._api_params:        
        print(item)
