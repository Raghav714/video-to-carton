import sys
import os
from glob import glob
import datetime
try:
    os.mkdir("test_images")
    os.mkdir("cartoonized_images")
except:
    pass
try:
   var=os.system(f'ffmpeg -i "./input_video.mp4" "test_images/%03d.png"')
   if var==0:
      print("Frame extract successful")
   else:
      print("Can't extract any frame")
except Exception as e:
   print(str(e))

root_path=os.getcwd()
var1=os.system("python cartoonize.py")
if var1==0:
   print("cartoonized complete")
else:
   print("cartoonize failed")

print("Upscaling")
os.system("python upscale.py")
   
os.chdir("./cartoonized_images")
#print(os.getcwd())
var3=os.system(f"ffmpeg -framerate 30 -i %03d.png cartoon.mp4")
if var3==0:
    print("We successfully make the cartoonized video.")
else:
    print("We can't make the cartoonized video.")
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
#print(os.getcwd())
try:
    os.mkdir("input_video")
except:
    pass
remove_list=["./input_video/input_video.mp4","./input_video/cartoon.mp4","./input_video/input_video.mkv","./input_video/cartoon.mkv"]
for i in remove_list:
      try:
         os.remove(i)
      except:
         pass

shutil.move(f"input_video.mp4","./input_video/")
shutil.move(f"./cartoonized_images/cartoon.png","./input_video/")


os.chdir("./input_video")

var4=os.system(f"ffmpeg -i input_video.mp4 audio.wav")
if var4==0:
    print("Successfully export audio")
else:
    print("Failed to export audio")
var5=os.system(f"ffmpeg -i cartoon.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 cartoon_audio.mp4")
if var5==0:
    print("Successfully replace audio in output file")
else:
    print("Failed to replace audio in output file")
path_parent1 = os.path.dirname(os.getcwd())
os.chdir(path_parent1)
