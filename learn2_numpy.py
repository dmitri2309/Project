from PIL import Image
from PIL import ImageOps
import numpy as np
import pandas as pd


#with Image.open('3802B_1777C.png') as img1:
img1 = Image.open('replicated_image1.png').convert('L')
    #img1.load()


#with Image.open('anilox_holst.png') as img2:
img2 = Image.open('anilox_no_white_no_border1.png').convert('L')
    #img2.load()

# img1.convert('L')
# img2.convert('L')
new_width = img2.size[0]
new_height = img1.size[1]
new_size = (new_width, new_height)
img_new = Image.new('L', new_size)
img_new.paste(img1, (500, 0))
img2_new = img2.resize(img_new.size)

img_new.convert('L')
img2_new.convert('L')


print(img_new.getbands())
print(img2_new.getbands())

dsg_array = np.array(img_new, dtype=np.uint8)
dsg_array[dsg_array != 0] = 255
# print(dsg_array.shape)
# print(dsg_array.dtype)
print(dsg_array.sum())
#anlx_array = np.array(img2_new)
anlx_array = np.array(img2_new, dtype=np.uint8)
anlx_array[anlx_array != 0] = 255
print(anlx_array.sum())

# df = pd.DataFrame(dsg_array)
# df.to_csv('pd.csv')

# print(dsg_array.shape)
# print(anlx_array.shape)

diff_array = anlx_array + dsg_array
#diff_array[diff_array > 255] = 255
print(diff_array.shape)
print(diff_array.sum())
print(diff_array.dtype)
x , y = diff_array.shape
print(x)
print(y)
sum_white = (x) * (y) * 255
print(sum_white)
print(diff_array.sum())


# invert_img2_new = ImageOps.invert(img2_new)
#
# invert_img2_new_array = np.array(invert_img2_new)
# print(invert_img2_new_array.sum())
#diff_array2 = dsg_array + diff_array
#diff_array2 = dsg_array - diff_array
#diff_array1 = diff_array + anlx_array
#diff_array2 = anlx_array - diff_array
# print(diff_array.shape)
# print(anlx_array.sum())
# print(dsg_array.sum())
#print(diff_array.sum())

#if anlx_array.any() == dsg_array.any():
if np.array_equal(anlx_array, diff_array):

    print('Нет пересечения')
else:
    print('Есть пересечение')

diff = Image.fromarray(diff_array)
invert_diff = ImageOps.invert(diff)
invert_diff_array = np.array(invert_diff, dtype=np.uint8)
#invert_diff_array[invert_diff_array == 1] = 0
print(invert_diff_array.sum())

# dsg = Image.fromarray(dsg_array)
# anlx = Image.fromarray(anlx_array)

#img_new.show()
#img2.show()
#diff.show()
invert_diff.show()
#invert_img2_new.show()
#img2_new.save('img2_new.png')
# dsg.show()
# anlx.show()
