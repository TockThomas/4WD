import cv2
from multiprocessing import Process


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.frame_byte = None
        self.process = Process(target=self.frame)
        print("Kamera ist hochgefahren.")

    def frame(self):
        ret, frame = self.capture.read()
        ret, buffer = cv2.imencode(".jpg", frame)
        self.frame_byte = buffer.tobytes()
