from flask import Flask, request, render_template
import os
import cv2  # Ensure you have OpenCV installed
import numpy as np

app = Flask(__name__)

# Create uploads directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'signature' not in request.files:
        return "No signature file part"

    if 'reference' not in request.files:
        return "No reference file part"

    signature_file = request.files['signature']
    reference_file = request.files['reference']

    if signature_file.filename == '':
        return "No selected signature file"

    if reference_file.filename == '':
        return "No selected reference file"

    # Save the uploaded files
    signature_path = os.path.join('uploads', signature_file.filename)
    reference_path = os.path.join('uploads', reference_file.filename)

    signature_file.save(signature_path)
    reference_file.save(reference_path)

    # Compare signatures
    score, similarity_percentage = compare_signatures(signature_path, reference_path)
    
    # Determine if they are from the same person (you can adjust the threshold)
    threshold = 0.7  # 70% similarity threshold for determining if signatures are from the same person
    match_status = "The signatures are from the same person." if similarity_percentage >= threshold * 100 else "The signatures are NOT from the same person."
    
    return f"Match Score: {score:.2f} ({similarity_percentage:.2f}%)<br>{match_status}"

def compare_signatures(signature_path, reference_path):
    # Load the images
    signature = cv2.imread(signature_path, cv2.IMREAD_GRAYSCALE)
    reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

    # Resize images to the same size (optional)
    signature = cv2.resize(signature, (300, 300))
    reference = cv2.resize(reference, (300, 300))

    # Use a simple method to compare images
    score = cv2.matchTemplate(signature, reference, cv2.TM_CCOEFF_NORMED)
    
    # The score is between 0 and 1, so convert it to percentage
    similarity_percentage = score[0][0] * 100
    
    return score[0][0], similarity_percentage

if __name__ == '__main__':
    app.run(debug=True)
