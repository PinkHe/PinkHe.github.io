import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt



image = cv.imread("E:\\PythonProject\\PinkHe.github.io\\TestProtest\\imageDemo\\file\\dgb03.png") #原图像
target = cv.imread("E:\\PythonProject\\PinkHe.github.io\\TestProtest\\imageDemo\\file\\dgbt03.png")#模板
methods = [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED]
th, tw = target.shape[:2]
for meth in methods:    
    result = cv.matchTemplate(image, target, meth)    
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)    
    if meth == cv.TM_SQDIFF_NORMED:        
        tl = min_loc    
    else:        
        tl = max_loc    
    br = (tl[0]+tw, tl[1]+th);    
    cv.rectangle(image, tl, br, 255, 2)    
    plt.subplot(121),plt.imshow(result)    
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])   
    plt.subplot(122),plt.imshow(image)    
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])    
    plt.suptitle(meth)    
    plt.show()
