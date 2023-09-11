from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import cv2
np.set_printoptions(suppress=True)


class CameraDetector(object):
    def __init__(self):
        model = load_model("converted_keras/keras_Model.h5", compile=False)
        class_names = open("converted_keras/labels.txt", "r").readlines()
        self.model = model
        self.class_names = class_names

    def get_image_of_camera(self):
        camera = cv2.VideoCapture(0)
        ret, image = camera.read()
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        alpha = 10  # Điều chỉnh giá trị này để tăng hoặc giảm độ sáng
        beta = 50  # Điều chỉnh giá trị này để tăng hoặc giảm độ tương phản

        image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

        return image

    def detect(self):
        image = self.get_image_of_camera()
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        print("Class:", class_name[2:], end="")
        print("Confidence Score:", confidence_score)
        return image,class_name[2:],  confidence_score
