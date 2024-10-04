# AttendanceChecker2

## Overview

AttendanceChecker2 is a web application designed to match signatures and determine if they belong to the same person. Users can upload signature images and receive feedback on whether the signatures are similar, along with a similarity percentage. 

## Live Demo

You can access the live application here: [AttendanceChecker2](https://signmatcher.onrender.com)

## Features

- Upload two signature images.
- Real-time comparison of uploaded signatures.
- Display similarity percentage between the signatures.
- User-friendly interface for easy interaction.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: OpenCV, NumPy
- **Deployment**: Render

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sgindeed/AttendanceChecker2.git
   cd AttendanceChecker2
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask Server**:

   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

1. Click on the "Choose File" buttons to upload two signature images.
2. After both files are uploaded, click the "Compare Signatures" button.
3. The application will display the similarity percentage between the two signatures.

## Deployment

The application is deployed on Render. You can check the live version [here](https://signmatcher.onrender.com).

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-YourFeature`).
5. Open a pull request.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

