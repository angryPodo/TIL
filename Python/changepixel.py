from cs1media import*

threshold_1= 170
threshold_2= 50
yellow=255,255,0
green=0,255,0
blue=0,0,255

img = load_picture("./krw.png")

w, h = img.size()
for y in range(h):  
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r+g+b)//3
        if v>threshold_1:
            img.set(x,y,yellow)
        elif threshold_2<v<=threshold_1:
            img.set(x,y,green)
        else:
            img.set(x,y,blue)
    
img.show()