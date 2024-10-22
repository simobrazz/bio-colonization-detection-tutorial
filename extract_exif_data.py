def get_exif_data(image):
    exif_data = {}
    width, height = image.size
    exif_data['ImageWidth'] = str(width)
    exif_data['ImageLength'] = str(height)
    return exif_data

# Extract EXIF data from the image
exif_data = get_exif_data(image)
