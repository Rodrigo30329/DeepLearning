
import matplotlib.pyplot as plt
import numpy as np

def main():
    t=np.arange(0,10,0.01)
    
    a=np.sin(t)
    b=np.cos(t)
    c=(0.2*np.sin(5*t))+(2*np.cos(t))
    d=2*(np.exp(t))
    e=(2*np.exp(-t))*(np.cos(2*t))

    titulos = ['Y=Sin(t)','Y=Cos(t)','Y=0.2*Sin(5t)+2*Cos(t)','Y=2e^t','y=(2e^-t)*Cos(2t)','Estrella de 5 Puntas']
    funciones = [a, b, c, d, e]

    for i in range(len(funciones)):
        plt.subplot(3,2,i+1)
        plt.plot(t,funciones[i], color='red')
        plt.title(titulos[i], fontweight="bold")
    plt.subplot(3,2,6)
    XEs1=[2, 4]
    XEs2=[4, 5]
    XEs3=[5, 6]
    XEs4=[6, 8]
    XEs5=[8, 7]
    XEs6=[7, 7]
    XEs7=[7, 5]
    XEs8=[5, 3]
    XEs9=[3, 3]
    XEs10=[3, 2]
    YEs1=[2, 2]
    YEs2=[2, 4]
    YEs3=[4, 2]
    YEs4=[2, 2]
    YEs5=[2, 0]
    YEs6=[0, -2]
    YEs7=[-2, -0.5]
    YEs8=[-0.5, -2]
    YEs9=[-2, 0]
    YEs10=[0, 2]

    plt.plot(XEs1, YEs1, color='red')
    plt.plot(XEs2, YEs2, color='red')
    plt.plot(XEs3, YEs3, color='red')
    plt.plot(XEs4, YEs4, color='red')
    plt.plot(XEs5, YEs5, color='red')
    plt.plot(XEs6, YEs6, color='red')
    plt.plot(XEs7, YEs7, color='red')
    plt.plot(XEs8, YEs8, color='red')
    plt.plot(XEs9, YEs9, color='red')
    plt.plot(XEs10, YEs10, color='red')
    plt.title(titulos[5], fontweight="bold")

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.subplots_adjust(top=0.8)    
    plt.tight_layout()
    plt.show()
        
if __name__=="__main__":
    main()