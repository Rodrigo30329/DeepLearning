import cv2
import matplotlib.pyplot as plt


def main():
    imgpath = "Actividad1\\Imagenes\\Imagen1.jfif"
    img = cv2.imread(imgpath, 0)

    plt.imshow(img)
    plt.title('Imagen por Defecto')
    plt.show()

    plt.imshow(img, cmap='Blues')
    plt.title('Imagen en Azules')
    plt.show()

    plt.imshow(img, cmap='Spectral')
    plt.title('Imagen en Espectral')
    plt.show()

    plt.imshow(img, cmap='gray')
    plt.title('Imagen en Grises')
    # Ocultar Ejes
    # plt.yticks([])
    # plt.xticks([])
    plt.show()
    
if __name__=="__main__":
    main()