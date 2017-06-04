# MP4 to MP3 Convertor

import os
import fnmatch
import subprocess

mp4list = []

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.mp4'):
        mp4list.append(file)

for mp4 in mp4list:
	# print("Processing", mp4, "...", end="")
	print("Processing", mp4 + "... ")
	mp3 = mp4[0:-1] + '3'
	ffmpeg_cmd = 'ffmpeg -i "' + mp4 + '" -vn -acodec libmp3lame -ac 2 -qscale:a 4 -ar 48000 "' + mp3 + '"'
	print(ffmpeg_cmd)
	subprocess.call(ffmpeg_cmd)
	# print(proc.communicate())

