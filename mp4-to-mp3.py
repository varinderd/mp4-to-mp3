'''

    By: Varinder
	

    Python3, ffmpeg, lame
    Convert mp4 video file to mp3 audio track using ffmpeg and lame

	Put this file in the drectory where you have all the mp4 videos and it will 
	generate mp3 files for all of them one at a time

	Example: 
	# python mp4-to-mp3.py

'''

import os
import fnmatch
import subprocess

mp4list = []

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.mp4'):
        mp4list.append(file)

for mp4 in mp4list:
	print("Processing", mp4)
	mp3 = mp4[0:-1] + '3'
	ffmpeg_cmd = 'ffmpeg -i "' + mp4 + '" -vn -acodec libmp3lame -ac 2 -qscale:a 4 -ar 48000 "' + mp3 + '"'
	print(ffmpeg_cmd)
	subprocess.call(ffmpeg_cmd)

