from PIL import Image, ImageChops, ImageEnhance
import os

def perform_ela(image_path, output_path, quality=90):
    original = Image.open(image_path).convert('RGB')

    temp_path = "temp.jpg"
    original.save(temp_path, 'JPEG', quality=quality)

    compressed = Image.open(temp_path)

    diff = ImageChops.difference(original, compressed)

    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])

    scale = 255.0 / max_diff if max_diff != 0 else 1

    diff = ImageEnhance.Brightness(diff).enhance(scale)

    diff.save(output_path)

    os.remove(temp_path)

    return output_path