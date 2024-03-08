from cs1media import *
white = (255, 255, 255)
black = (0, 0, 0)

def blackwhite(img, threshold):
 w, h = img.size()
 for y in range(h):
  for x in range(w):
   r, g, b = img.get(x, y)
   v = (r + g + b) // 3 # average of r,g,b
   if v > threshold:
    img.set(x, y, white)
   else:
    img.set(x, y, black)
 


agu = load_picture("KKT.jpg")
blackwhite(agu,100)
agu.show()
