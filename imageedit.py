from PIL import Image

img1=Image.open('green.jpg')
#img1.save('green.png')
#img1.show()
MAX_SIZE=(350,350)
img1.thumbnail(MAX_SIZE)
img1.save('greensamll.jpg')
