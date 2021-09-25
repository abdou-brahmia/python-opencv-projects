import numpy as np
import cv2
import matplotlib.pyplot as plt



def resise(img,scale_percent):    # resize image
      
    width = int(img.shape[1] * scale_percent )
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized


def colorer(image):
    imgcopy = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR )
    imgcopy = cv2.cvtColor(imgcopy, cv2.COLOR_BGR2HSV )
    for i in range(imgcopy.shape[0]):
        for j in range(imgcopy.shape[1]):
            if image[i,j]!=0:
                imgcopy[i,j]=(image[i,j],150,150)
    imgcopy = cv2.cvtColor(imgcopy, cv2.COLOR_HSV2BGR )

    return imgcopy
def methode(image):
    nmrobj=20
    val=nmrobj
    imgcopy = np.zeros((image.shape[0],image.shape[1]), dtype=np.uint8)
    [iMax,jMax] = image.shape
    for i in range(iMax):
        for j in range(jMax):
            if image[i,j]==255:
                state =True
                val=nmrobj
                if i+1<iMax:
                    if (imgcopy[i+1,j]<=val) and (imgcopy[i+1,j]!=0) and (image[i+1,j]!=0):
                        val=imgcopy[i+1,j]
                        state =False

                    if  (j+1<jMax):
                        if (imgcopy[i+1,j+1]<=val)and(imgcopy[i+1,j+1]!=0)and(image[i+1,j+1]!=0):
                            val=imgcopy[i+1,j+1]
                            state =False
                    if  (j-1>=0):
                        if (imgcopy[i+1,j-1]<=val)and(imgcopy[i+1,j-1]!=0)and(image[i+1,j-1]!=0):
                            val=imgcopy[i+1,j-1]
                            state =False

                if i-1>=0:
                    if (imgcopy[i-1,j]<=val)and(imgcopy[i-1,j]!=0)and(image[i-1,j]!=0):
                        val=imgcopy[i-1,j]
                        state =False
                    if  (j+1<jMax):
                        if (imgcopy[i-1,j+1]<=val)and(imgcopy[i-1,j+1]!=0)and(image[i-1,j+1]!=0):
                            val=imgcopy[i-1,j+1]
                            state =False
                    if  (j-1>=0):
                        if (imgcopy[i-1,j-1]<=val)and(imgcopy[i-1,j-1]!=0)and(image[i-1,j-1]!=0):
                            val=imgcopy[i-1,j-1]
                            state =False
               
                if j+1<jMax:
                    if (imgcopy[i,j+1]<=val)and(imgcopy[i,j+1]!=0)and(image[i,j+1]!=0):
                        val=imgcopy[i,j+1]
                        state =False
                if j-1>=0:
                    if (imgcopy[i,j-1]<=val)and(imgcopy[i,j-1]!=0)and(image[i,j-1]!=0):
                        val=imgcopy[i,j-1]
                        state =False
                if state==True:
                    nmrobj+=29
                    val=nmrobj
                    imgcopy[i,j]=val

                if i+1<iMax:
                    if  (image[i+1,j]!=0):
                        imgcopy[i+1,j]=val
                    if  (j+1<jMax):
                        if (image[i+1,j+1]!=0):
                            imgcopy[i+1,j+1]=val
                    if  (j-1>=0):
                        if (image[i+1,j-1]!=0):
                            imgcopy[i+1,j-1]=val

                if i-1>=0:
                    if (image[i-1,j]!=0):
                        imgcopy[i-1,j]=val
                    if  (j+1<jMax):
                        if (image[i-1,j+1]!=0):
                            imgcopy[i-1,j+1]=val
                    if  (j-1>=0):
                        if (image[i-1,j-1]!=0):
                            imgcopy[i-1,j-1]=val
                   
                if j+1<jMax:
                    if (image[i,j+1]!=0):
                        imgcopy[i,j+1]=val
                if j-1>=0:
                    if (image[i,j-1]!=0):
                        imgcopy[i,j-1]=val

    ######################################################################

    while True:
        imagetest=imgcopy.copy()
        for i in range(iMax-1,-1,-1):
            for j in range(jMax-1,-1,-1):
                if image[i,j]==255:

                    val=imgcopy[i,j]
                    if i+1<iMax:
                        if (imgcopy[i+1,j]<=val) and (imgcopy[i+1,j]!=0) and (image[i+1,j]!=0):
                            val=imgcopy[i+1,j]

                        if  (j+1<jMax):
                            if (imgcopy[i+1,j+1]<=val)and(imgcopy[i+1,j+1]!=0)and(image[i+1,j+1]!=0):
                                val=imgcopy[i+1,j+1]

                        if  (j-1>=0):
                            if (imgcopy[i+1,j-1]<=val)and(imgcopy[i+1,j-1]!=0)and(image[i+1,j-1]!=0):
                                val=imgcopy[i+1,j-1]

                    if i-1>=0:
                        if (imgcopy[i-1,j]<=val)and(imgcopy[i-1,j]!=0)and(image[i-1,j]!=0):
                            val=imgcopy[i-1,j]

                        if  (j+1<jMax):
                            if (imgcopy[i-1,j+1]<=val)and(imgcopy[i-1,j+1]!=0)and(image[i-1,j+1]!=0):
                                val=imgcopy[i-1,j+1]

                        if  (j-1>=0):
                            if (imgcopy[i-1,j-1]<=val)and(imgcopy[i-1,j-1]!=0)and(image[i-1,j-1]!=0):
                                val=imgcopy[i-1,j-1]

                    if j+1<jMax:
                        if (imgcopy[i,j+1]<=val)and(imgcopy[i,j+1]!=0)and(image[i,j+1]!=0):
                            val=imgcopy[i,j+1]

                    if j-1>=0:
                        if (imgcopy[i,j-1]<=val)and(imgcopy[i,j-1]!=0)and(image[i,j-1]!=0):
                            val=imgcopy[i,j-1]

                    if i+1<iMax:
                        if  (image[i+1,j]!=0):
                            imgcopy[i+1,j]=val
                        if  (j+1<jMax):
                            if (image[i+1,j+1]!=0):
                                imgcopy[i+1,j+1]=val
                        if  (j-1>=0):
                            if (image[i+1,j-1]!=0):
                                imgcopy[i+1,j-1]=val

                    if i-1>=0:
                        if (image[i-1,j]!=0):
                            imgcopy[i-1,j]=val
                        if  (j+1<jMax):
                            if (image[i-1,j+1]!=0):
                                imgcopy[i-1,j+1]=val
                        if  (j-1>=0):
                            if (image[i-1,j-1]!=0):
                                imgcopy[i-1,j-1]=val

                    if j+1<jMax:
                        if (image[i,j+1]!=0):
                            imgcopy[i,j+1]=val

                    if j-1>=0:
                        if (image[i,j-1]!=0):
                            imgcopy[i,j-1]=val

    

        ######################################################################################################
        for i in range(iMax):
            for j in range(jMax):
                if image[i,j]==255:

                    val=imgcopy[i,j]
                    if i+1<iMax:
                        if (imgcopy[i+1,j]<=val) and (imgcopy[i+1,j]!=0) and (image[i+1,j]!=0):
                            val=imgcopy[i+1,j]

                        if  (j+1<jMax):
                            if (imgcopy[i+1,j+1]<=val)and(imgcopy[i+1,j+1]!=0)and(image[i+1,j+1]!=0):
                                val=imgcopy[i+1,j+1]
                        if  (j-1>=0):
                            if (imgcopy[i+1,j-1]<=val)and(imgcopy[i+1,j-1]!=0)and(image[i+1,j-1]!=0):
                                val=imgcopy[i+1,j-1]

                    if i-1>=0:
                        if (imgcopy[i-1,j]<=val)and(imgcopy[i-1,j]!=0)and(image[i-1,j]!=0):
                            val=imgcopy[i-1,j]

                        if  (j+1<jMax):
                            if (imgcopy[i-1,j+1]<=val)and(imgcopy[i-1,j+1]!=0)and(image[i-1,j+1]!=0):
                                val=imgcopy[i-1,j+1]

                        if  (j-1>=0):
                            if (imgcopy[i-1,j-1]<=val)and(imgcopy[i-1,j-1]!=0)and(image[i-1,j-1]!=0):
                                val=imgcopy[i-1,j-1]

                    if j+1<jMax:
                        if (imgcopy[i,j+1]<=val)and(imgcopy[i,j+1]!=0)and(image[i,j+1]!=0):
                            val=imgcopy[i,j+1]

                    if j-1>=0:
                        if (imgcopy[i,j-1]<=val)and(imgcopy[i,j-1]!=0)and(image[i,j-1]!=0):
                            val=imgcopy[i,j-1]

                    if i+1<iMax:
                        if  (image[i+1,j]!=0):
                            imgcopy[i+1,j]=val
                        if  (j+1<jMax):
                            if (image[i+1,j+1]!=0):
                                imgcopy[i+1,j+1]=val
                        if  (j-1>=0):
                            if (image[i+1,j-1]!=0):
                                imgcopy[i+1,j-1]=val

                    if i-1>=0:
                        if (image[i-1,j]!=0):
                            imgcopy[i-1,j]=val
                        if  (j+1<jMax):
                            if (image[i-1,j+1]!=0):
                                imgcopy[i-1,j+1]=val
                        if  (j-1>=0):
                            if (image[i-1,j-1]!=0):
                                imgcopy[i-1,j-1]=val

                    if j+1<jMax:
                        if (image[i,j+1]!=0):
                            imgcopy[i,j+1]=val

                    if j-1>=0:
                        if (image[i,j-1]!=0):
                            imgcopy[i,j-1]=val


        difference1 = cv2.subtract(imgcopy,imagetest)    
        difference2 = cv2.subtract(imagetest, imgcopy)    
        
        result = (not np.any(difference1))and not np.any(difference2)
        if result:
            break

        
    return colorer( imgcopy)


if __name__ == "__main__":
    
    array= [[000,255,000,000,000,000,000],
            [000,255,255,255,000,255,255],
            [255,255,000,000,000,000,255],
            [000,000,000,255,255,255,255],
            [255,255,000,000,000,000,000]]
    img = np.array(array,dtype=np.uint8)
    resized=resise(img,50)
    imgcopy=methode(img)
    resized2=resise(imgcopy,50)
    print(img)
    print(imgcopy)



    plt.imshow(resized,'gray')
    plt.show()


    plt.imshow(resized2)
    plt.show()

