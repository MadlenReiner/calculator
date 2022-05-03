import numpy as np

from std_operations import add, substract
from linalg import ScalProd

a=-1
b=3.14

c=add(a,b)
d=substract(a,b)

print("{}+{}={}".format(a,b,c))
print("{}-{}={}".format(a,b,d))

u = np.array([1, 0.5, -3.14])
v = np.array([-4, 0, 6.73])

udotv = ScalProd(u,v)

print("{} dot {} = {}".format(u,v,udotv))
