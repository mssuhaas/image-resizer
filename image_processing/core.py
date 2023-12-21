from PIL import Image
import os

def resize_and_compress(input_path, output_path):
    original_image = Image.open(input_path)
    max_size_bytes = 100 * 1024  # 100 KB
    original_image.thumbnail((800, 800))
    initial_quality = 90
    temp_path = "temp_resized_image.jpg"
    original_image.save(temp_path, "JPEG", quality=initial_quality)

    while os.path.getsize(temp_path) > max_size_bytes:
        initial_quality -= 5
        original_image.save(temp_path, "JPEG", quality=initial_quality)

    os.rename(temp_path, output_path)
