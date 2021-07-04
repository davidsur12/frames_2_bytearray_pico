# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:29:14 2021

@author: USUARIO
"""
import cv2 as cv
import numpy as np
from PIL import Image
import os
import errno



        
def areglo(imagen , file):
   
    print("ancho de imagen " , imagen.shape);
    btarray="";
    #las imagenes con opencv shape[0] regresa las filas y shape[1] regresa las columnas
    cont=0;#contador de bits
    cadena="";#cadena donde se agregan los bit
    contf=0;#contador de filas
    contc=0;#contador de columnas
    umbral=100;
    for i in range(0 , imagen.shape[0]):#filas
        for j in range(0 , imagen.shape[1]):#columnas
            contc = contc + 1;
            if(imagen[i,j]>umbral):#se remplaza por un igual a 0 o 255 
                cadena +="1";#se agrega 1 si el valor es mayor el umbral osea es igual a 255
            else:
                cadena +="0";#se agrega 0 si el valor del pixel es menor que el umbral o igual a 0
                
            cont=cont+1;
            if(cont==8):#cuando llegan a los 8 bits
             
              # cadena= str(int(cadena , 2)) + ",";#comvierto el valor a decimal y luego a cadena luego agrego una ","
               if(i == imagen.shape[0]-1  and  j == imagen.shape[1]-1):
                   cadena= str(int(cadena , 2))
               else:
                   cadena= str(int(cadena , 2)) + ","
               btarray = btarray + cadena;  #agrego el valor a la cadena y un bytearray
               cadena="";#limpio la cadena
               cont=0;#reinicio el contador a cero
        contf = contf + 1; 
        contc = 0;        
    print("total filas " , contf);
        
   # print(btarray);  #imprimo el  bytearray  
   # print("largo de la cadena " , len(btarray));  
    file.write(btarray);#guardo la imagen en la ruta especificada
    file.close();
    

     


def main():
    try:
        
        num_Imagenes=40;
        ruta_Imagenes="imagenes";#las imagenes deben tener un nombre ascendente en digitos comenzando de 1 hasta el total de imagenes
        pixel_with=128;
        pixel_high=68;
        ruta_bitmap="bitmapssdsas"#direccion donde se guardara los bitmap
        os.mkdir(ruta_bitmap)#creo una carpeta

        for i in range(1,num_Imagenes):
            
            #creo un  archico .txt para guardar en byearray
            file=open(ruta_bitmap + "/bitearray%s.txt"% str(i) , "w");
            #ruta de la imagen
            imgPath = ruta_Imagenes + "/%s.png" % str(i)
            #leo la imagen
            imagen=cv.imread(imgPath);
            #redimenciono la  imagen
            imagen1 = cv.resize(imagen , (pixel_with , pixel_high) , interpolation = cv.INTER_AREA);
            #aplico el filtro escala de grises
            gray = cv.cvtColor(imagen1, cv.COLOR_BGR2GRAY)
            # Imagen binaria
            ret, imagen2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
            """ 
            cv.imshow("imagen" , imagen2);
            cv.waitKey(0)
            cv.destroyAllWindows()
            """
            areglo(imagen2 , file);#los parametros son la imagen y el path donde se guardara mi imagen

    except OSError as e:
        print("algo salio mal");
        if e.errno != errno.EEXIST:
            
            raise
            
            
            
if __name__== '__main__':
    main();
