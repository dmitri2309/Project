from PIL import Image
from PIL import ImageOps
import numpy as np
import pandas as pd

red = np.zeros((600, 600))
# # green = np.zeros((600, 600))
blue = np.zeros((600, 600))
red[150:350, 150:350] = 255
# # green[200:400, 200:400] = 255
blue[350:450, 350:450] = 255
#
red_img = Image.fromarray(red).convert("L")
# # green_img = Image.fromarray(green).convert("L")
blue_img = Image.fromarray(blue).convert("L")
#
# #square_img = Image.merge("RGB", (red_img, green_img, blue_img))

inverted_img_red = ImageOps.invert(red_img)
inverted_img_blue = ImageOps.invert(blue_img)
red_img_array = np.array(red_img)
print(red_img_array.sum())
blue_img_array = np.array(blue_img)
print(blue_img_array.sum())
total_arr = red_img_array + blue_img_array
print(total_arr.sum())
#
# df = pd.DataFrame(square_array)
# df.to_csv('pd_square.csv')
#
#red_img.show()
inverted_img_red.show()
inverted_img_blue.show()

inverted_img_red_array = np.array(inverted_img_red)
print(inverted_img_red_array.sum())
inverted_img_blue_array = np.array(inverted_img_blue)
print(inverted_img_blue_array.sum())

diff = inverted_img_blue_array + inverted_img_red_array
print(diff.sum())
diff_img = Image.fromarray(diff)
inv_diff_img = ImageOps.invert((diff_img))
inv_diff_arr = np.array(inv_diff_img)
print(inv_diff_arr.sum())

inv_diff_arr[inv_diff_arr == 1] = 0
print(inv_diff_arr.sum())

# df = pd.DataFrame(inv_diff_arr)
# df.to_csv('pd_test1.csv')
#
# arr_test = np.full((600, 600), 255)
# print(arr_test.sum())

diff_img.show()
inv_diff_img.show()

# # square_img.save('square_img.png')
#
# red_img.show()

#img = Image.open('anilox_no_white_V4.png').convert('L')
#
# print(img.getbands())
#
# img_array = np.array(img)
#
# df = pd.DataFrame(img_array)
# df.to_csv('anilox_no_white.csv')
#
# img.show

# print(img.size)
#
# cropped_img = img.crop((4300, 0, 4500, 7100))
# print(cropped_img.size)
#
# img_invert = ImageOps.invert(cropped_img)
#
# cropped_img_array = np.array(cropped_img)
# img_invert_array = np.array(img_invert)
#
# df = pd.DataFrame(img_invert_array)
# df.to_csv('img_invert.csv')
# #
#
# #img.show()
# cropped_img.show()
# img_invert.show()