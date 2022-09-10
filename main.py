from pytube import YouTube
import ffmpeg

#ask for the link from user

link = input(" Please enter the youtube video link ")
#Saved_path = str(input(" please choose your prefered download location "))
Saved_path= "C:\\Users\\BISHER\\Videos\\music using python"
resolution = str(input(" please choose the prefered video resolution 144p/240p/360p/720p "))

yt = YouTube(str(link))
#Showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
#print("Description: ", yt.description)

print("downloading")
#print(yt.streams)
try:
    # download audio only
    yt.streams.filter(file_extension='mp3', progressive=False).first().download(output_path=Saved_path, filename="audio.mp3")
    audio = ffmpeg.input("audio.mp3")
    #download video only
    yt.streams.filter(file_extension='mp4', res=resolution, progressive=False).first().download(output_path=Saved_path, filename="video.mp4")
    video = ffmpeg.input("video.mp4")
    ffmpeg.output(audio,video,yt.title,format='mp4').run(overwrite_output=True)
except:
    yt.streams.filter(file_extension='mp4', res=resolution, progressive=True).first().download(output_path=Saved_path)
finally:
    print("download has been completed")
