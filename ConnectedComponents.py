import numpy as np
from skimage import io, exposure

class ConnectedComponents():
    def __init__(self, imgFile) -> None:
        self.img = self.readImage(imgFile)

        # if file read succesfully then run connected components
        if self.img is not None:
            # convert file to grayscale
            self.img = self.convertToGrayscale(self.img)
            self.img = self.convertToBlackAndWhite(self.img)

            

    def readImage(self, imgFile):
        try:
            file = io.imread(imgFile)
            return file
        except:
            print("Error reading image")
            return None
        
    def convertToGrayscale(self, img):
        arr = []

        for i in img:
            line = []
            for j in i:
                line.append((j[0] * 0.21) + (j[1] * 0.72) + (j[2] * 0.07))
                
            arr.append(line)

        io.imsave("./images/grayscale.jpg", np.array(arr, dtype=int))

        return arr

    def convertToBlackAndWhite(self, img):
        arr = []

        for i in img:
            line = []
            for j in i:
                if j > 135:
                    line.append(255)
                else:
                    line.append(0)
                
            arr.append(line)

        io.imsave("./images/b+w.jpg", np.array(arr, dtype=int))


    def findConnectedComponents(self, img):
        for i in range(0, len(img)):
            for j in range(0, len(img[i])):
                pass
    
if __name__ == "__main__":
    imgFile = "/home/wiktor/Desktop/python/ImageTextNetwork/images/receipt.jpg"
    connectedComponents = ConnectedComponents(imgFile)