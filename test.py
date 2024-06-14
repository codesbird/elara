import os


#this is for image
images = os.listdir("img")
i = len(os.listdir("image"))

for item in images:
    i+=1
    os.rename(os.path.join('img',item),os.path.join('image',f"image_{i}.png"))


#this is for videos 
videos = os.listdir("vid")
i = len(os.listdir("video"))

for item in videos:
    i+=1
    os.rename(os.path.join('vid',item),os.path.join('video',f"video_{i}.mp4"))


