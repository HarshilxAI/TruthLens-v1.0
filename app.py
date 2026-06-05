from flask import Flask, render_template, request
import os

from utils.ela import perform_ela
from utils.fft import perform_fft
from utils.model import predict_image, get_model
from utils.gradcam import generate_gradcam

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ✅ HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')

# ✅ UPLOAD ROUTE
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No selected file"

    # Save uploaded image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # ----- ELA -----
    ela_path = os.path.join(app.config['OUTPUT_FOLDER'], "ela_" + file.filename)
    perform_ela(filepath, ela_path)

    # ----- FFT -----
    fft_path = os.path.join(app.config['OUTPUT_FOLDER'], "fft_" + file.filename)
    perform_fft(filepath, fft_path)

    # ----- PREDICTION -----
    label, confidence = predict_image(filepath)
    confidence_percent = round(confidence * 100, 2)
    if label == "Fake":
        risk_score = min(100, int(confidence_percent + 5))
    else:
        risk_score = max(0, int(100 - confidence_percent))
    print("Prediction:", label, confidence)

    # ----- GRAD-CAM -----
    gradcam_filename = "gradcam_" + file.filename
    gradcam_path = os.path.join(app.config['OUTPUT_FOLDER'], gradcam_filename)

    model = get_model()
    generate_gradcam(model, filepath, gradcam_path)

    return render_template(
    'index.html',
    uploaded_image=filepath,
    ela_image=ela_path,
    fft_image=fft_path,
    gradcam_image=gradcam_path,
    prediction=label,
    confidence=confidence_percent,
    risk_score=risk_score
)

# Run App
if __name__ == '__main__':
    app.run(debug=True)