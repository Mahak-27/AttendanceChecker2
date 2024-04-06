from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import cv2
from skimage.metrics import structural_similarity as ssim
import base64
from io import BytesIO
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)

# Match Threshold
THRESHOLD = 85

# Compare signature images
def compare_signatures(image1_data, image2_data):
    try:
        # Decode base64 image data
        image1_bytes = base64.b64decode(image1_data.split(',')[1])
        image2_bytes = base64.b64decode(image2_data.split(',')[1])

        image1 = Image.open(BytesIO(image1_bytes)).convert('L')  # Convert to grayscale
        image2 = Image.open(BytesIO(image2_bytes)).convert('L')  # Convert to grayscale

        # Resize images to the same dimensions
        max_width = max(image1.size[0], image2.size[0])
        max_height = max(image1.size[1], image2.size[1])
        image1 = image1.resize((max_width, max_height))
        image2 = image2.resize((max_width, max_height))

        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Calculate similarity
        similarity = ssim(image1_np, image2_np) * 100
        return similarity

    except Exception as e:
        print("Error:", e)
        return None

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to compare signatures
@app.route('/compare', methods=['POST'])
def compare():
    try:
        data = request.get_json()
        image1_data = data.get('image1')
        image2_data = data.get('image2')

        if image1_data and image2_data:
            similarity = compare_signatures(image1_data, image2_data)

            if similarity is not None:
                return jsonify({'result': f'Signature similarity: {similarity:.2f}%'})
            else:
                return jsonify({'error': 'Error processing images.'}), 500
        else:
            return jsonify({'error': 'Image data missing.'}), 400
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app