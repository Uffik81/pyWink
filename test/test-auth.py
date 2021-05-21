import sys
sys.path.append('D:/github/Uffik81/pyWink/')

from pywinkapi import pyWinkConnect, pyWinkApi

#ss = pyWinkSession()
#ss.update_session_id()
channels = pyWinkApi()

channels.load_channels()