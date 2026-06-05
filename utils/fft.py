import cv2
import numpy as np
import os

def perform_fft(image_path, output_path):
    # Read image in grayscale
    img = cv2.imread(image_path, 0)

    # Apply FFT
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # Compute magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

    # Normalize for display
    normalized = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)

    # Convert to uint8
    normalized = np.uint8(normalized)

    # Save output
    cv2.imwrite(output_path, normalized)

    return output_path