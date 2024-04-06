# Signature Similarity Detector

Signature Similarity Detector is a web application built with Flask and JavaScript that allows users to upload two images of signatures and compare their similarity using a machine learning algorithm.

## Features

- Upload two signature images from your computer.
- Compare the similarity percentage between the uploaded images.
- Receive the comparison result in a pop-up message.

## Technologies Used

- Flask: Python web framework used for the backend.
- JavaScript: Used for client-side scripting to handle image uploads and comparisons.
- Tailwind CSS: Utility-first CSS framework used for styling the frontend.
- OpenCV: Python library used for image processing.
- scikit-image: Python library used for calculating image similarity metrics.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- OpenCV
- scikit-image

### Installation

1. Clone the repository:

    bash
    git clone https://github.com/Aishee06/ai_signaturedetection.git
    

2. Install dependencies:

    bash
    pip install -r requirements.txt
    

### Usage

1. Run the Flask app:

    bash
    python app.py
    

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).
3. Upload two signature images using the provided buttons.
4. Click the "Compare" button to initiate the comparison process.
5. View the similarity percentage result in a pop-up message.
