import requests

# API URL and headers
API_URL = "https://www.cultural-arts.com/pedrocchi//bio-colonization-v0"
HEADERS = {"Content-Type": "application/json"}

# Payload with Base64 image and EXIF data
payload = {
    "image": base64_image,
    "exifData": exif_data
}

# Function to send image and metadata to the API
def send_image_to_api(api_url, payload):
    response = requests.post(api_url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Example usage
response_data = send_image_to_api(API_URL, payload)

def display_processed_image(response_data):
    if 'image' in response_data:
        # Decode the Base64 processed image
        processed_image_data = base64.b64decode(response_data['image'])
        processed_image = Image.open(BytesIO(processed_image_data))
        processed_image.show()

# Display the processed image
if response_data:
    display_processed_image(response_data)
