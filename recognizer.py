class FaceRecognizer:
    def __init__(self, model_path):
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.model.read(model_path)
        self.face_cascade = cv2.CascadeClassifier('src/models/haarcascade_frontalface_default.xml')

    def recognize(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        recognized_faces = []
        for (x, y, w, h) in faces:
            id_, confidence = self.model.predict(gray_frame[y:y+h, x:x+w])
            recognized_faces.append((id_, confidence, (x, y, w, h)))

        return recognized_faces

    def draw_recognitions(self, frame, recognized_faces):
        for (id_, confidence, (x, y, w, h)) in recognized_faces:
            label = f'ID: {id_}, Conf: {confidence:.2f}'
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        return frame