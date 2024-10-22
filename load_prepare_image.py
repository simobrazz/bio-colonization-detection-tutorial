import base64
from PIL import Image
from io import BytesIO

# Load image using Pillow and convert to Base64
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        img = Image.open(img_file)
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        return img, img_base64

# Example usage
image_path = 'path_to_your_image.jpg'
image, base64_image = load_image(image_path)
