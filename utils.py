def load_image(image_path):
    """Load an image from the specified path."""
    import cv2
    image = cv2.imread(image_path)
    return image

def preprocess_image(image):
    """Convert the image to grayscale and resize it."""
    import cv2
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (200, 200))  # Resize to 200x200
    return resized_image

def save_image(image, save_path):
    """Save the processed image to the specified path."""
    import cv2
    cv2.imwrite(save_path, image)

def get_face_rectangles(detected_faces):
    """Extract rectangles from detected faces."""
    return [face for (x, y, w, h) in detected_faces]