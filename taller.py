#JUAN DIEGO HERNANDEZ RODRIGUEZ C.C 1036964559
#JUAN ANDRES SAÑUDO GOMEZ C.C 1001234045

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio
import pydicom as dicom
import os

# #1-)
# img0=cv2.imread('cell.jpg')
# img=cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)

# imgR=img[:,:,0]
# imgG=img[:,:,1]
# imgB=img[:,:,2]

# img1= cv2.cvtColor(imgB,cv2.COLOR_BAYER_BG2GRAY)

# _,imgC= cv2.threshold(img1,150,255,cv2.THRESH_BINARY)

# kernel = np.ones((2,2),np.uint8)
# ima2 = cv2.dilate(imgC,kernel,iterations = 15)
# # ima2 = cv2.erode(ima2,kernel,iterations =3 )

# elem,mask=cv2.connectedComponents(ima2)
# plt.imshow(ima2)
# print (f"El numero de celulas es: {elem}")

# plt.imshow(mask)
# plt.show()


#2



def recopilar_imagenes(ruta_carpeta):

  imagenes_dicom = []
  for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith(".dcm"):
      ruta_imagen = os.path.join(ruta_carpeta, archivo)
      imagen_dicom = dicom.read_file(ruta_imagen)
      imagenes_dicom.append(imagen_dicom)
  return imagenes_dicom


def visualizar_imagenes(imagenes_dicom):

    for imagen_dicom in imagenes_dicom:
        plt.imshow(imagen_dicom.pixel_array, cmap=plt.cm.gray)
        plt.title(f"Imagen {imagen_dicom.InstanceNumber}")
        plt.axis('off')
        plt.show()

# cargar_imagenes_desde_carpeta("archivosDCM")

ruta_carpeta = "archivosDCM"
imagenes_dicom = recopilar_imagenes(ruta_carpeta)
visualizar_imagenes(imagenes_dicom)