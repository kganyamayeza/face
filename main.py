import cv2
from camera import Camera
from recognizer import FaceRecognizer

def main():
    # Initialize the camera
    camera = Camera()
    
    # Load the trained model
    recognizer = FaceRecognizer()
    recognizer.load_model('path/to/trained_model.xml')  # Update with the actual model path

    # Start the face recognition process
    while True:
        frame = camera.get_frame()
        if frame is None:
            break
        
        # Recognize faces in the frame
        recognized_frame = recognizer.recognize_faces(frame)
        
        # Display the resulting frame
        cv2.imshow('Face Recognition', recognized_frame)
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()