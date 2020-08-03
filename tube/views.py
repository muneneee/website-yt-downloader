from django.shortcuts import render,redirect
from pytube import YouTube
import os

url = ''

def youtube(request):
    return render(request, 'index.html')


def download(request):
    global url

    url = request.GET.get('url')
    
     
    obj = YouTube(url)
    resolutions = []
    strm_all = obj.streams.filter(progressive=True, file_extension='mp4').all()

    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))

    embed_link = url.replace("watch?v=", "embed/")
    path = 'D:\\'


    return render(request, 'download.html', {'rsl': resolutions, 'embd': embed_link, 'url': url})



def downloaded(request, res):  
    global url

    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'

    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(res).download(homedir + '/Downloads')
        return render(request, 'downloaded.html')
    else:
        return render(request, 'error.html')
    
    return redirect('home')