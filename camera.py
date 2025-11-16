import cv2

class Camera:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)

    def capture_frame(self):
        ret, frame = self.video_capture.read()
        if not ret:
            raise Exception("Could not read frame from camera.")
        return frame

    def release(self):
        self.video_capture.release()
        cv2.destroyAllWindows()