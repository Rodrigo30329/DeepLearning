# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

def main():
    imgpath = "Actividad1\\Imagenes\\Imagen1.jfif"
    savpath = "Actividad1\\Imagenes\\Imagen1Edit.jpg"
    img = cv2.imread(imgpath)
    # escala de grises
    # img = cv2.imread(imgpath, 0) 
    cv2.namedWindow('imagen', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('imagen',img)
    cv2.imwrite(savpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('imagen')
    
if __name__=="__main__":
    main()