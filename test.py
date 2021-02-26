from __future__ import unicode_literals
import youtube_dl
import os
import sys
firstarg=sys.argv[1]

if os.path.exists("yiff.mp4"):
	os.remove("yiff.mp4") 

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'worst[ext=m4a]/mp4',       
    'outtmpl': 'yiff.mp4',        
    'noplaylist' : True,        
    'progress_hooks': [my_hook],  
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([firstarg])


print('hello world')

