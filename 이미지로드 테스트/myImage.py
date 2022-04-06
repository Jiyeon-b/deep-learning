# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:50:13 2021

@author: Administrator
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('my.png')

plt.imshow(img)
plt.show()
