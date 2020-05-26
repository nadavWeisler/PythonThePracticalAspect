from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np

class MyImage(object):
    """
    MyImage class
    """

    # Black RGB array
    _BLACK_RGB = [0, 0, 0]

    def __init__(self, img_array):
        """
        Class constructor
        :param img_array:   Image numpy array
        """
        self.img = img_array

    def turn_area_black(self, upper_left, bottom_right):
        """
        Turn certain section of image in black
        :param upper_left:      Upper left section
        :param bottom_right:    Bottom right section
        :return:                Pic numpy array paint in black in the given section
        """
        newImg = self.img.copy()
        newImg[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]] = self._BLACK_RGB
        return newImg

    def adding_cage(self, upper_left, bottom_right, cage_color):
        """
        Adding cage to certain section in our pic
        :param upper_left:      Upper left section
        :param bottom_right:    Bottom right section
        :param cage_color:      Cage color
        :return:                Pic numpy array with added cage in the given section
        """
        newImg = self.img.copy()
        newImg[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]] = \
            newImg[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]] + cage_color
        return newImg

    def blur_certain_area(self, upper_left, bottom_right):
        """
        Blur certain section in our pic
        :param upper_left:      Upper left section
        :param bottom_right:    Bottom right section
        :return:                Pic numpy array with blur in the given section
        """
        newImg = self.img.copy()
        blurPart = ndimage.gaussian_filter(
            newImg[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]],
            sigma=5)
        newImg[upper_left[0]:bottom_right[0], upper_left[1]:bottom_right[1]] = blurPart
        return newImg


def image_hist(img_array):
    """
    Create histogram of color distribution
    :param img_array:   Image numpy array
    :return:    Histogram
    """
    plt.hist(img_array[:, :, 0].ravel(), color='red', alpha=0.5)
    plt.hist(img_array[:, :, 1].ravel(), color='Green', alpha=0.5)
    plt.hist(img_array[:, :, 2].ravel(), color='Blue', alpha=0.5)
    plt.xlabel('Color Strength')
    plt.ylabel('Color Count')
    plt.legend(['Red', 'Green', 'Blue'])
    plt.title("Color Distribution")
    plt.show()