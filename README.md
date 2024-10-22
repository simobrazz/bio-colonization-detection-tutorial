# Cultural Arts SaaS API: Bio-Colonization Defects Detection in Artworks

## Overview

Welcome to the **Cultural Arts SaaS API** tutorial! This repository contains a complete guide for detecting bio-colonization defects in artworks using Python. The **Cultural Arts SaaS API** marks a significant milestone for our organization as we unveil a cutting-edge development in the realm of art preservation and restoration.

**Our AI system** detects bio-contamination defects in artworks, such as:
- Alga
- Lichen
- Mould
- Moss
- Plant

By leveraging artificial intelligence, the API allows us to detect subtle bio-contamination defects that could compromise the longevity and beauty of cultural treasures. This initiative is a major step forward in the preservation of cultural heritage.

The API is built upon an extensive database, which now spans all Italian regions with more than **80,000 entries**.

## Features

- **Bio-Colonization Defects Detection**: Detect bio-contamination in artworks, including algae, moss, mould, and more.
- **GPS Location Metadata**: Integrate mandatory GPS coordinates into the API request to improve accuracy.
- **EXIF Data**: Automatically extract EXIF metadata (image dimensions, etc.) from the uploaded image.

## Prerequisites

You need to have the following packages installed in your Python environment before using the API:

```bash
pip install requests Pillow geopy
```

------------------------------------------------------------------

# Tutorial

Follow these steps to detect bio-colonization defects using the Cultural Arts SaaS API.

### Step 1: Load and Prepare the Image
You need to load an image from your local filesystem and encode it as Base64 (required for sending it to the API).

```bash
import base64
from PIL import Image
from io import BytesIO

# Load image using Pillow
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        img = Image.open(img_file)
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        return img, img_base64

# Example usage
image_path = 'path_to_your_image.jpg'
image, base64_image = load_image(image_path)
```

### Step 2: Extract EXIF Data

You can extract the image’s EXIF metadata (e.g., dimensions) to be sent along with the image data. This step is optional but useful for ensuring accurate analysis.

```bash
def get_exif_data(image):
    exif_data = {}
    width, height = image.size
    exif_data['ImageWidth'] = str(width)
    exif_data['ImageLength'] = str(height)
    return exif_data

# Extract EXIF data from the image
exif_data = get_exif_data(image)
```

### Step 3: Get Mandatory GPS Coordinates

You need to provide mandatory GPS coordinates for the API to work. The following code uses the Geopy library to get the coordinates based on a location.

```bash
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Fetch GPS coordinates using Geopy
def get_gps_coordinates():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode("Your address or location")  # Replace with actual location
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError("Unable to fetch GPS coordinates.")
    except GeocoderTimedOut:
        raise ValueError("Geocoder service timed out.")

# Example usage
latitude, longitude = get_gps_coordinates()
exif_data['GPSLatitude'] = str(latitude)
exif_data['GPSLongitude'] = str(longitude)
```

### Step 4: Send Image and Data to the API

Now that you have the image, EXIF data, and GPS coordinates ready, you can send them to the Cultural Arts SaaS API for defect detection.

```bash
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
```

### Step 5: Display the Processed Image

After receiving the processed image from the API, you can display it using the Pillow library.

```bash
def display_processed_image(response_data):
    if 'image' in response_data:
        # Decode the Base64 processed image
        processed_image_data = base64.b64decode(response_data['image'])
        processed_image = Image.open(BytesIO(processed_image_data))
        processed_image.show()

# Display the processed image
if response_data:
    display_processed_image(response_data)
```

## Contributing
We welcome contributions to improve this repository. Please feel free to submit pull requests or open issues.
