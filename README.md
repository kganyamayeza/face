# Face Recognition Python Project

This project implements a facial recognition system using OpenCV. It captures video from a camera, detects faces, and recognizes them based on a trained model. The project is structured into several modules for better organization and maintainability.Created by kganya Mayeza

## Project Structure

```
face-recognition-python
├── src
│   ├── main.py               # Entry point of the application
│   ├── camera.py             # Handles camera operations
│   ├── recognizer.py         # Contains the FaceRecognizer class
│   ├── trainer.py            # Contains the ModelTrainer class
│   ├── utils.py              # Utility functions
│   └── models
│       └── haarcascade_frontalface_default.xml  # Pre-trained Haar Cascade model
├── web
│   └── index.html            # HTML interface for the project
├── data
│   ├── samples               # Directory for sample images
│   └── labels.csv            # Labels for the sample images
├── tests
│   └── test_recognizer.py    # Unit tests for the FaceRecognizer class
├── requirements.txt          # Project dependencies
├── .gitignore                # Files to ignore in version control
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd face-recognition-python
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your sample images and place them in the `data/samples` directory.
2. Update the `data/labels.csv` file to map each image to a specific identity.
3. Run the application:
   ```
   python src/main.py
   ```

4. Open `web/index.html` in a web browser to view the video feed and recognition results.

## Testing

To run the unit tests for the FaceRecognizer class, execute:
```
python -m unittest tests/test_recognizer.py
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.