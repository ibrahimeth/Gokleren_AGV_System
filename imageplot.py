
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random 

img = mpimg.imread("deniyoz.jpg")
print(img)
# plt.axis("off")
plt.imshow(img)

qrx = random.randint(0,800)
qry = random.randint(0,800)
plt.xlim(0,1000)
plt.ylim(0,800)  
x = [qrx]
y = [qry]

plt.scatter(x,y,s =250,marker = "^")
plt.show()