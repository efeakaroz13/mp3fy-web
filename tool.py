
import urllib.request
import re
import time
from pytube import YouTube
import os
from colorama import Fore, Back, Style

def compress(basename):
        os.system(f"ffmpeg -y -i '{basename}.mp4' -vcodec libx265 -crf 28 '{basename}_C.mp4'")

class Downloader:
    def downloadvideo(search):
        search = search.lower().replace("ü","u").replace("$","s").replace("ö","").replace("ş","s").replace("ö","o").replace("İ","I").replace("ı","i")
        try:
            page = urllib.request.urlopen("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))
            videoids=  re.findall(r"watch\?v=(\S{11})",page.read().decode())
            theurl = "https://youtube.com/watch?v="+videoids[0]

            yt = YouTube(theurl)
            print(Fore.BLUE,"DOWNLOADING | {}".format(yt.title))
            
            video = yt.streams.filter(only_audio=True).first()
            
            
            out_file = video.download(output_path="./static")
            base, ext = os.path.splitext(out_file)
            compress(base)
            os.system(f"ffmpeg -y -i '{base}.mp4' -b:a 192K -vn '{base}.mp3'")
            os.system(f"rm '{base}.mp4'")
            os.system(f"rm '{base}_C.mp4'")
            print(Fore.GREEN,"COMPLETE | {}".format(yt.title))
            print(Style.RESET_ALL,"\n")
        except:
            print(Fore.RED,"NETWORK ERR - Retrying in 10 seconds")
            print(Style.RESET_ALL)
            time.sleep(10)
            page = urllib.request.urlopen("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))
            videoids=  re.findall(r"watch\?v=(\S{11})",page.read().decode())
            theurl = "https://youtube.com/watch?v="+videoids[0]
            
            yt = YouTube(theurl)
            print(Fore.BLUE,"DOWNLOADING | {}".format(yt.title))
            
            video = yt.streams.filter(only_audio=True).first()
            
            
            out_file = video.download(output_path="./static")
            base, ext = os.path.splitext(out_file)
            compress(base)
            os.system(f"ffmpeg -y -i '{base}.mp4' -b:a 192K -vn '{base}.mp3'")
            os.system(f"rm '{base}.mp4'")
            os.system(f"rm '{base}_C.mp4'")
            print(Fore.GREEN,"COMPLETE | {}".format(yt.title))
            print(Style.RESET_ALL,"\n")

        return f"{base}.mp3"




