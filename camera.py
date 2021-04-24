import cv2


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture()

    def frame(self):
        frame = self.capture.read()[1]
        buffer = cv2.imencode(".jpg", frame)[1]
        return buffer.tobytes()
