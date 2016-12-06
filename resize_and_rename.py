import os
from PIL import Image




listOfFiles = os.listdir()
listOfImage = list(filter(lambda x:x.endswith('.jpg'), listOfFiles)) + list(filter(lambda x:x.endswith('.JPG'), listOfFiles))

width = 700
for i in range(len(listOfImage)):
    img = Image.open(listOfImage[i])
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    image_resized =  img.resize((width, height), Image.ANTIALIAS)
    image_resized.save(listOfImage[i])
    os.renames(listOfImage[i], str(i+1) + '.jpg')








    # os.rename(listOfImage[i], str(i+1) + '.jpg')


