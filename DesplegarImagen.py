# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    imgpath = "C:\\Users\\joser\\Pictures\\Saved Pictures\\Imagen1.jfif"
    img = cv2.imread(imgpath)
    cv2.namedWindow('perra', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('perra',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()