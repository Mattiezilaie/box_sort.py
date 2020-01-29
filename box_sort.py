# Author: Mahtab Zilaie
# Date: January 28 2020
# Description: Box class whose init method is width, height, length and
# method named volume that returns the volume of the Box. A function called
# box_sort (that is not apart of the box class) uses insertion sort to sort a
# list of Boxes from greatest volume to least volume.


class Box:

    """class named box with three parameters length, width, and height """

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):

        """function that gets volume of box"""

        return self.length * self.width * self.height


def box_sort(boxes):

    """sorts boxes in descending order"""

    for i in range(1, len(boxes)):
        box = boxes[i]
        j = i - 1
        while j >= 0 and box.volume() > boxes[j].volume():
            boxes[j + 1] = boxes[j]
            j -= 1
        boxes[j + 1] = box


