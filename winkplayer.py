#import ffmpeg
#from kivy.app import App
#from kivy.uix.widget import Widget
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.videoplayer import VideoPlayer
import ffmpeg_streaming
from ffpyplayer.player import MediaPlayer
import numpy as np
from http.client import HTTPSConnection
import os
import sys
import tkinter
import time
from ssplayer import readSSLStream

url='https://a787201483-s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/bw3000000/playlist.m3u8?useseq=t'

#class myApp(App):
#    def build(self):
#        url='https://a787201483-s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/bw3000000/playlist.m3u8?useseq=t'
#        self.player = VideoPlayer(source=url, state='play', options={'eos': 'loop'})
#        return (self.player)

resolute = 'RESOLUTION=1280x720'
url = "https://s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/variant.m3u8"
conn = HTTPSConnection('s72169.cdn.ngenix.net')
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
conn.request("GET","/hls/CH_VSETVHD_HLS/variant.m3u8", headers=header)
res = conn.getresponse()
print(res.getheaders())
print(res.read().decode('utf-8'))
url='https://a787201483-s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/bw3000000/playlist.m3u8?useseq=t'
conn = HTTPSConnection('a787201483-s72169.cdn.ngenix.net')
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
conn.request("GET","/hls/CH_VSETVHD_HLS/bw3000000/playlist.m3u8?useseq=t", headers=header)
res = conn.getresponse()
print(res.getheaders())
print(res.read().decode('utf-8'))

window = tkinter.Tk()
window.geometry('1280x720')

url='https://a787201483-s72169.cdn.ngenix.net/hls/CH_VSETVHD_HLS/bw3000000/1617300000/1617301800.ets/13843192-15779216.ts'
video1 = ffmpeg_streaming.input(url)

#conn = HTTPSConnection('a787201483-s72169.cdn.ngenix.net')
#header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
#conn.request("GET","/hls/CH_VSETVHD_HLS/bw3000000/1617300000/1617301800.ets/13843192-15779216.ts", headers=header)
#res = conn.getresponse()
#print(res.getheaders())
#print(res.read())
video = tkinter.Frame(window, bg='#000000')
video.pack(side=tkinter.BOTTOM,anchor=tkinter.S,expand=tkinter.YES,fill=tkinter.BOTH)
window_id = video.winfo_id()
ffmpeg_streaming.
ssplayer = readSSLStream(server='a787201483-s72169.cdn.ngenix.net',\
    url='/hls/CH_VSETVHD_HLS/bw3000000/1617307200/1617308100.ets/17177184-18770296.ts',\
    header='user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')
mp = MediaPlayer(url)
ssplayer.start()
window.mainloop()
#app1  = myApp()
#app1.run()
#while(cap.isOpened()):
#    ret, frame = cap.read()
#    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('frame',frame)
#    #if cv2.waitKey(1) & 0xFF == ord('q'):
#    #    break
#cap.release()
#cv2.destroyAllWindows()
