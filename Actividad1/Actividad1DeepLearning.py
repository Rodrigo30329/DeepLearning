import cv2
import matplotlib.pyplot as plt

def main():
    foldpath = ""
    
    img1path = foldpath + "Imagen1.jfif"    
    img1 = cv2.imread(img1path, 0)

    img2path = foldpath + "Imagen2.jpg"
    img2 = cv2.imread(img2path, 0)

    img3path = foldpath + "Imagen3.jpg"
    img3 = cv2.imread(img3path, 0)
    
    img4path = foldpath + "Imagen4.jpg"
    img4 = cv2.imread(img4path, 0)
    
    img5path = foldpath + "Imagen5.jpg"
    img5 = cv2.imread(img5path, 0)
    
    img6path = foldpath + "Imagen6.jfif"    
    img6 = cv2.imread(img6path, 0)

    img7path = foldpath + "Imagen7.jfif"
    img7 = cv2.imread(img7path, 0)

    img8path = foldpath + "Imagen8.jfif"
    img8 = cv2.imread(img8path, 0)
    
    img9path = foldpath + "Imagen9.jpg"
    img9 = cv2.imread(img9path, 0)

    img1 = cv2.resize(img1, (500,400))
    img2 = cv2.resize(img2, (500,400))
    img3 = cv2.resize(img3, (500,400))
    img4 = cv2.resize(img4, (500,400))
    img5 = cv2.resize(img5, (500,400))
    img6 = cv2.resize(img6, (500,400))
    img7 = cv2.resize(img7, (500,400))
    img8 = cv2.resize(img8, (500,400))
    img9 = cv2.resize(img9, (500,400))

    titulos = ['Imagen1','Imagen2','Imagen3','Imagen4','Imagen5','Imagen6','Imagen7','Imagen8','Imagen9']
    imagenes = [img1, img2, img3, img4, img5, img6, img7, img8, img9]
    mapa = ['twilight', 'Blues', 'Spectral', 'gray', 'Purples', 'Greens', 'Oranges', 'PuBu', 'Reds']
    
    for i in range(len(imagenes)):
        plt.subplot(3,3,i+1)
        plt.imshow(imagenes[i], cmap=mapa[i])
        plt.title(titulos[i]+" Usando "+mapa[i], fontweight="bold")
        plt.xticks([])
        plt.yticks([])
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.subplots_adjust(top=0.8)    
    plt.tight_layout()
    plt.show()
        
if __name__=="__main__":
    main()