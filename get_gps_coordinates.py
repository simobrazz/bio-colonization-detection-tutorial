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
