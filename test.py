import os

for i,item in enumerate(os.listdir("image")):
    os.rename(os.path.join('image',item),os.path.join('image',f"image_{i+1}.png"))

