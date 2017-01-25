# a = '<img src="/sites/default/files/images/veterans2016/'
# for i in range (1, 14):
#     print (a + str(i) + '.jpg">')

from PIL import Image
import os

files = os.listdir()
images =[]
for i in {'.JPG', '.jpg', '.jpeg', '.png', '.PNG'}:
    images = filter(lambda x: x.endswith(i), files)
    a = 1
    for image in images:
        im =Image.open(image)
        width, height = im.size
        new_size_file = im.resize((950, int(950*height/width)))
        name = str(a) + str(i)
        new_size_file.save(name)
        im.close()
        new_size_file.close()
        a += 1


