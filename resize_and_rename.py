

from PIL import Image
import os

width_finnaly = 650
files = os.listdir()
images =[]
for i in {'.JPG', '.jpg', '.jpeg', '.png', '.PNG'}:
    images = filter(lambda x: x.endswith(i), files)
    a = 1
    for image in images:
        im =Image.open(image)
        width, height = im.size
        new_size_file = im.resize((width_finnaly, int(width_finnaly*height/width)))
        name = str(a) + str(i)
        new_size_file.save(name)
        im.close()
        new_size_file.close()
        a += 1


