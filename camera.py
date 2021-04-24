import cv2


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture()

    def frame(self):
        ret, frame = self.capture.read()
        ret, buffer = cv2.imencode(".jpg", frame)
        return buffer.tobytes()
