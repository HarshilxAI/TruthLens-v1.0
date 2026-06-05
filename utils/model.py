import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("fake_image_model.h5")

def predict_image(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        label = "Real"
        confidence = prediction
    else:
        label = "Fake"
        confidence = 1 - prediction

    return label, float(confidence)

# Needed for Grad-CAM
def get_model():
    return model