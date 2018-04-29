from PIL import Image

img = Image.open("friends.jpg")
res_img = img.resize((1280, 960))
area = ( 100, 200,300,375)
cropped_img = img.crop(area)
original = Image.open("original.jpg")
moment = Image.open("moment.jpg")
coord = (300,300,600,600)

moment.paste(original, coord)
moment.show()
print(original.mode)

r1, g1, b1 = moment.split()
r2, g2, b2 = res_img.split()

new_img = Image.merge("RGB", (r1, b1, r1))
cool_img = Image.merge("RGB", (r2, b1, g2))


elmo = original.transpose(Image.FLIP_TOP_BOTTOM)
elmo_round = original.transpose (Image.ROTATE_180)
elmo.show()


new_img.show()
cool_img.show()


print(img.size)
print(img.format)


