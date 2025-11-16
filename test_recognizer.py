import unittest
from src.recognizer import FaceRecognizer

class TestFaceRecognizer(unittest.TestCase):

    def setUp(self):
        self.recognizer = FaceRecognizer()

    def test_recognize_face(self):
        # Assuming we have a method to load a test image
        test_image = self.recognizer.load_image('path/to/test/image.jpg')
        result = self.recognizer.recognize(test_image)
        self.assertIsNotNone(result)
        self.assertIn('name', result)  # Assuming the result contains a 'name' key

    def test_recognize_unknown_face(self):
        unknown_image = self.recognizer.load_image('path/to/unknown/image.jpg')
        result = self.recognizer.recognize(unknown_image)
        self.assertIsNone(result)  # Assuming unknown faces return None

if __name__ == '__main__':
    unittest.main()