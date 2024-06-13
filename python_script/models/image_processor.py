import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass

    def preprocess_image(self, image):
        # Preprocess image
        image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray