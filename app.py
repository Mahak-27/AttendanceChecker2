from flask import Flask, request, render_template
import os
import cv2 
import numpy as np

app = Flask(__name__)

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

    signature_path = os.path.join('uploads', signature_file.filename)
    reference_path = os.path.join('uploads', reference_file.filename)

    signature_file.save(signature_path)
    reference_file.save(reference_path)

    score, similarity_percentage = compare_signatures(signature_path, reference_path)
    
    threshold = 0.7  
    match_status = "The signatures are from the same person." if similarity_percentage >= threshold * 100 else "The signatures are NOT from the same person."
    
    return f"Match Score: {score:.2f} ({similarity_percentage:.2f}%)<br>{match_status}"

def compare_signatures(signature_path, reference_path):
    signature = cv2.imread(signature_path, cv2.IMREAD_GRAYSCALE)
    reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

    signature = cv2.resize(signature, (300, 300))
    reference = cv2.resize(reference, (300, 300))

    score = cv2.matchTemplate(signature, reference, cv2.TM_CCOEFF_NORMED)
    
    similarity_percentage = score[0][0] * 100
    
    return score[0][0], similarity_percentage

if __name__ == '__main__':
    app.run(debug=True)
