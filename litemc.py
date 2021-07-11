# pip install --upgrade ipython
import kivy
kivy.require('1.9.1')
from winkconnect import WinkParams, WincClientConnection
import time
import datetime
import xmltodict

import json
from http.client import HTTPSConnection
import time
from urllib.parse import urlparse

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.video import Video
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top',  500)
Config.set('graphics', 'resizable', 'False')
#Config.set('graphics', 'borderless',  1)
Config.set('graphics', 'width', 1127)
Config.set('graphics', 'height', 636)

COOKIE = ''

class LitePlayer(App):
    video = None
    _wink_sdk_ver = ''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._wink_index = WinkParams('https://wink.rt.ru/',COOKIE)
        self._wink_tv = WinkParams('https://wink.rt.ru/tv',COOKIE)
        self._wink_client = WincClientConnection(params=self._wink_index, tv=self._wink_tv )
        self._playlist =  self._wink_client.get_tv_playlist()
        self._current_ch = 0


    def build(self):
        Window.bind(on_keyboard=self.on_keyboard)  # bind our handler
        self._list_channels = self._wink_client.get_list_channels()
        ch_url, err = self._wink_client.get_channel_url(str(self._list_channels[ self._current_ch]['nc_channel_id']))#self._wink_client._fairplay_cert_url)
        #url_key_1 = 'https://s40757.cdn.ngenix.net/certificates/8BA6D7AC942DE15E1B375DEF7FA20918757A6533'
        #self._wink_client.load_cert_ott(url_key_1)

        self.video = Video(source=ch_url)
        self.video.state='play'
        self.video.options = {'eos': 'loop'}
        self.video.allow_stretch=True
        #self.video.pos_hint = {'top': 1.0}
        self._grid_1 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        self._grid_menu = GridLayout(cols=8)
        self._grid_channels = GridLayout(cols=3)

        self.video.add_widget(self._grid_1)
        self.l = Label(text='Hello world', font_size='20sp', size_hint = (1, 0.17))
        #self.l.pos(
        print(self.l.pos)
        self.img1 = AsyncImage(source=self._wink_tv.__IMAGES_URL__ + '/sdp/nc-snapshot1569398092010.jpg', pos_hint = {'x': 0.0, 'y': 0.8})
        self.video.add_widget(self._grid_menu)
        self.video.add_widget(self.img1)
        self.video.add_widget(self.l)
        self._grid_1.add_widget(self._grid_channels)
        self.l_ch = []
        for i in range(5):
            lab1 = Label(text=self._list_channels[ i]['name'], font_size='20sp'  )
            self._grid_channels.add_widget(lab1)
            self.l_ch += [lab1]

        print(Window.size)
        return self.video

    def VideoDone(self, value, value2):
        print ("video done", value, value2)

    def _get_utc(self):
        return round((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()*1000) + 338055300

    def get_drm_parse(self):
        root = xmltodict.parse(self._drm_xml)        
        _mpd = root['MPD']
        print(_mpd)
        self._baseurl_drm = self._url_drm
        for adaptation_set in _mpd['Period']['AdaptationSet']:
            shab = adaptation_set['SegmentTemplate']
            #print (shab)
            self._drm_shablon = shab['@media']
            for key in adaptation_set['Representation']:
                for inkey in key:
                    if inkey == '@height' and key[inkey] == '1080':
                        self._video_1080 =  key['@id']
                    if inkey == '@bandwidth' and key[inkey] == '500000':
                        self._audio_1080 =  key['@id']
        _tmp_url = self._baseurl_drm.replace('/manifest.mpd?profile=web_auto', '/')
        _tmp_utc_str = str(self._get_utc())
        _tmp_url_video = ''.join([_tmp_url , self._drm_shablon.replace('$RepresentationID$',self._video_1080).replace('$Time$', _tmp_utc_str)])
        print(_tmp_url_video)
        _tmp_url_audio = ''.join([_tmp_url , self._drm_shablon.replace('$RepresentationID$',self._audio_1080).replace('$Time$', _tmp_utc_str)])

        print(_tmp_url_audio)

    def on_stop(self):
        # The Kivy event loop is about to stop, set a stop signal;
        # otherwise the app window will close, but the Python process will
        # keep running until all secondary threads exit.
        print ('stopping and closing kivy')
        #self.video.state='stop'

    def on_keyboard(self, window, key, scancode, codepoint, modifier):
        print (window, key, scancode, codepoint, modifier)
        if key == 13:
            pass
        elif codepoint == 'p':
            print ('pausing with p pressed')
            self.video.state='stop'
        elif codepoint == 's':
            print ('starting with s pressed')
            self.video.state='play'
        elif codepoint == 'r':
            #self.video.source=self._wink_client.get_channel_url('5')
            self.video.state='play'
            print ('re-starting with r pressed')
            self.video.seek(0, precise=True)
        if key == 280:
            self._current_ch += 1
            if self._current_ch > (len(self._list_channels)-1):
                self._current_ch = 0
            ch_url , err =self._wink_client.get_channel_url(str(self._list_channels[ self._current_ch]['nc_channel_id']))
            if not err :                
                self.img1.source = self._wink_tv.__IMAGES_URL__ + self._wink_client._current_channel['logo']
                self.img1.reload()
                self.video.source = ch_url
                self.video.state='play'
                print ('re-starting with r pressed')
                #self.video.seek(0, precise=True)         
            self.l.text = self._wink_client._current_channel['description']   
        if key == 281:
            self._current_ch -= 1
            if self._current_ch < 0:
                self._current_ch = len(self._list_channels)-1
            ch_url , err =self._wink_client.get_channel_url(str(self._list_channels[ self._current_ch]['nc_channel_id']))
            if not err :
                self.img1.source = self._wink_tv.__IMAGES_URL__ + self._wink_client._current_channel['logo']
                self.img1.reload()
                self.video.source = ch_url
                self.video.state='play'
                print ('re-starting with r pressed')
                #self.video.seek(0, precise=True)          
            self.l.text = self._wink_client._current_channel['description']
        else:
            print(key)

if __name__ == '__main__':
    Window.size=size = (1920, 1080)
    Window.fullscreen = True
    LitePlayer().run()