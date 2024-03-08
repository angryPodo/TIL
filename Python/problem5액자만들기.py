from cs1media import *
#100점


img = load_picture("./sejong.jpg")
img.show()
w, h = img.size()
hi =int(w+20)
wei = int(h+20)

new=create_picture(hi,wei,"RED")
for y in range(h):  
 for x in range(w):
  orgin =img.get(x,y)
  w_ten=x+10
  h_ten=y+10
  new.set(w_ten, h_ten,orgin)
new.show()