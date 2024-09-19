from PIL import Image
import os
import numpy as np

def anlx_dsg(anlx_dir, repl_dsg_nr):
    anilox_list = []
    with Image.open(repl_dsg_nr) as img1:
        img1.load()
    for root, dirs, files in os.walk(anlx_dir):
        for file in files:
            path = os.path.join(root, file)
            #print("Opening image: {}".format(path))
            try:
                with Image.open(path) as img2:
                    img2.load()
                # with Image.open(repl_dsg_nr) as design:
                #     design.load()
                new_width = img2.size[0]
                new_height = img1.size[1]
                new_size = (new_width, new_height)
                img_new = Image.new('L', new_size)
                img_new.paste(img1, (500, 0))
                img2_new = img2.resize(img_new.size)

                img_new.convert('L')
                img2_new.convert('L')

                dsg_array = np.array(img_new, dtype=np.uint8)
                # dsg_array[dsg_array != 0] = 255
                anlx_array = np.array(img2_new, dtype=np.uint8)
                # anlx_array[anlx_array != 0] = 255

                diff_array = anlx_array + dsg_array
                diff_array[diff_array != 0] = 255
                diff_array_sum = diff_array.sum()
                print(diff_array_sum)

                x, y = diff_array.shape
                sum_white = x * y * 255
                sum_white_fill = np.full((x, y), 255)
                print(sum_white_fill.sum())
                print(sum_white)
                print(diff_array.sum())

                if sum_white == diff_array_sum:
                    # if np.array_equal(sum_white_fill, diff_array_sum):
                    print('Нет пересечения')
                    anilox_list.append(file)
                else:
                    print('Есть пересечение')


                diff = Image.fromarray(diff_array)
                diff.show()

                diff2_array = dsg_array - anlx_array
                diff2_array[diff2_array != 0] = 255  # для получения визульного контроля пересечения
                diff2 = Image.fromarray(diff2_array)
                diff2.show()
            except OSError:
                print('Файл не является изображением') # Handle exception if needed
    return anilox_list

#aniloxes = anlx_dsg('C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout\\Anilox_140', 'replicated_image1.png')
aniloxes = anlx_dsg('Anilox_140', 'replicated_image1.png')
print(aniloxes)
