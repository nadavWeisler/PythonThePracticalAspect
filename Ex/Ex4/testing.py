import ex4a
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import matplotlib.image
from ex4b import MyImage, image_hist

# arr = np.array([1, 2, 3, 5, 1, 3, 4])
# print(ex4a.find_largest_n(arr, 2))
#
# arr2 = np.array([1, 2, 3, 4, 5, 6])
# print(ex4a.find_even_larger_than(arr2, 4))
#
# arr3 = np.array(['a', 'b', 'c'])
# print(ex4a.add_prefix(arr3, "d"))
#
# arr4 = np.array(['Count', 'me', 'please'])
# st = 'e'
# print(ex4a.count_string_with_substring(arr4, st))

img1_path = "img\IMG_5438.JPG"
img2_path = "img\mindset-3536805_1280.jpg"
img3_path = "img\herman.jpeg"
img1_arr = plt.imread(img3_path)
imgObject = MyImage(img1_arr)
black_image = imgObject.turn_area_black([2,2], [100,100])
# blur_image = imgObject.blur_certain_area([2,2], [1000,1000])
# cage_image = imgObject.adding_cage([2,2], [1000,1000], [0, 50, 32])
# 
# plt.imsave("newImg.jpg", cage_image)

image_hist(black_image)
