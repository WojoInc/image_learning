from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

# https://pythonprogramming.net/basic-image-recognition-testing/?completed=/saving-image-data/
def determineNum(filePath):
    # load example data for comparison
    matchedArr = []
    exampleData = open('numArEx.txt', 'r').read()
    exampleData = exampleData.split('\n')
    img = Image.open(filePath)
    imgArr = np.array(img)
    imgList = imgArr.tolist()
    inQuestion = str(imgList)

    for example in exampleData:
        try:
            splitEx = example.split('::')
            curNum = splitEx[0]
            curArr = splitEx[1]
            


def threshold(img_arr):
    balance_arr = []
    new_arr = img_arr
    from statistics import mean
    for row in img_arr:
        for pixel in row:
            balance_arr.append(mean(pixel[:3]))
    balance = mean(balance_arr)
    for row in new_arr:
        for pixel in row:
            # if pixel average is higher than the balance, consider it a white
            if mean(pixel[:3]) > balance:
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
                pixel[3] = 255
            else:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
                pixel[3] = 255
    return new_arr


def createExamples():
    num_arr_ex = open('numArEx.txt', 'a')
    for num in range(1,10):
        for decimal in range(1,10):
            print(str(num) + '.' + str(decimal))
            fpath = 'images/numbers/' + str(num) + '.' + str(decimal) + '.png'
            img = Image.open(fpath)
            img_arr = np.array(img)
            img_arr_list = str(img_arr.tolist())

            print(img_arr_list)
            lineToWrite = str(num) + '::' + img_arr_list + '\n'
            num_arr_ex.write(lineToWrite)

createExamples()

img = Image.open('images/numbers/0.1.png')
img_arr = np.array(img)

img2 = Image.open('images/numbers/y0.4.png')
img_arr2 = np.array(img2)

img3 = Image.open('images/numbers/y0.5.png')
img_arr3 = np.array(img3)

img4 = Image.open('images/sentdex.png')
img_arr4 = np.array(img4)

# apply threshold
img_arr = threshold(img_arr)
img_arr2 = threshold(img_arr2)
img_arr3 = threshold(img_arr3)
img_arr4 = threshold(img_arr4)

figure = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(img_arr)
ax2.imshow(img_arr2)
ax3.imshow(img_arr3)
ax4.imshow(img_arr4)

# figure.show()

print(img_arr)
plt.show()
