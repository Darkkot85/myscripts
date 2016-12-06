import os
from PIL import Image




listOfFiles = os.listdir()
listOfImage = list(filter(lambda x:x.endswith('.jpg'), listOfFiles))

width = 700
for i in range(len(listOfImage)):
    img = Image.open(listOfImage[i])
    ratio = (img. / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
     img = img.resize((basewidth, height), PIL.Image.ANTIALIAS)
    img.save()







    # os.rename(listOfImage[i], str(i+1) + '.jpg')


