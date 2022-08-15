# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    imgpath = "C:\\Users\\joser\\Pictures\\Saved Pictures\\DeepL\\Originales\\Imagen1.jfif"
    savpath = "C:\\Users\\joser\\Pictures\\Saved Pictures\\DeepL\\Cambiadas\\Imagen1Edit.jpg"
    img = cv2.imread(imgpath, 0)
    cv2.namedWindow('perra', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('perra',img)
    cv2.imwrite(savpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('perra')
    
if __name__=="__main__":
    main()