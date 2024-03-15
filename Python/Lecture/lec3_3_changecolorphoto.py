from cs1media import *

yellow = (255, 255, 0)

img = load_picture("./sejong.jpg")
#img.show()


w, h = img.size()
y = int(h+20)
for i in range(w):
  img.set(i, y-h, yellow)

img.show()