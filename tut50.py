from PIL import Image
from PIL import ImageFilter
from _struct import *

# stores bites as data
packed_data = pack('iif', 2, 3, 4.5)
print(packed_data)

income = [2, 6, 8]


def doppel(euro):
    return euro * 2


new_income = list(map(doppel, income))
print(new_income)

elmo = Image.open("original.jpg")
blur = elmo.filter(ImageFilter.BLUR)
detail = elmo.filter(ImageFilter.DETAIL)

print(calcsize('iif'))

orig_data = unpack('iif', packed_data)

print(orig_data)

a = 50
b = 25
c = a & b

print(c)

x = 300
y = x >> 2
print(y)
