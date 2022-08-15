import cv2
import matplotlib.pyplot as plt

def main():
    foldpath = "C:\\Users\\joser\\Pictures\\Saved Pictures\\DeepL\\Originales\\"
    img1path = foldpath + "Imagen1.jfif"    
    img1 = cv2.imread(img1path,0)

    img2path = foldpath + "Imagen2.jpg"
    img2 = cv2.imread(img2path,0)

    plt.subplot(1,2,1)
    plt.imshow(img1, cmap='Reds')
    plt.title('Imagen 1')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title('Imagen 2')
    plt.yticks([])
    plt.xticks([])

    plt.show()

    # # con ciclo for
    # titulos=['Imagen1','Imagen2']
    # imagenes=[img1, img2]
    # for i in range(2):
    #     plt.subplot(1,2,i+1)
    #     plt.imshow(imagenes[i])
    #     plt.title(titulos[i])
    #     plt.xticks([])
    #     plt.yticks([])
    # plt.show()
    
if __name__=="__main__":
    main()