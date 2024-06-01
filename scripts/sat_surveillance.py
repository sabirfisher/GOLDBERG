from PIL import Image
from io import BytesIO
import requests
import time
import logging
import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()
load_dotenv("resources/env_configs/.env")

# Your API keys
GEOCODE = os.environ.get("GEOCODE_API_KEY")
GOOGLE = os.environ.get('GOOGLE') 
def sat_surveillance(target_location, num_images=3, radius=400):
    gmaps = googlemaps.Client(key=GOOGLE)
    print("Satellite Surveillance module loaded.\n")

    try:
        # Geocoding to get the latitude and longitude
        geocode_result = gmaps.geocode(target_location)
        poi_list = []
        if not geocode_result:
            logging.error("Geocoding failed. Unable to retrieve location coordinates.")
            return [], []

        lat, lng = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        print(f"Acquiring satellite images and POIs for {target_location}...")
        logging.info(f"Acquiring satellite images and POIs for {target_location}.")

        satellite_images = []
        for zoom in range(20, 20 - num_images, -1):
            image_url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom={zoom}&size=600x300&maptype=satellite&markers=color:red%7Clabel:S%7C{lat},{lng}&key={GOOGLE}'
            response = requests.get(image_url)
            if response.status_code == 200:
                satellite_images.append(image_url)
                sat_img = Image.open(BytesIO(response.content))
                print(f"Displaying satellite image with Zoom {zoom}.")
                sat_img.show()
                time.sleep(0.3)
                logging.info(f"Displayed satellite image with Zoom {zoom} for {target_location}.")

        places_result = gmaps.places_nearby(location=(lat, lng), radius=radius, open_now=False)
        for place in places_result.get('results', []):
            poi_info = {
                "name": place.get('name'),
                "types": place.get('types', []),
                "location": place.get('geometry', {}).get('location', {})
            }
            poi_list.append(poi_info)
            print(f"POI: {poi_info['name']} - Type: {', '.join(poi_info['types'])}")

        return satellite_images, poi_list  # Return satellite images URLs and POIs

    except requests.RequestException as e:
        logging.error(f"Satellite surveillance error: {e}")
        return [], []

    except Exception as e:
        logging.error(f"Unexpected error in satellite surveillance: {e}")
        return [], []



if __name__ == "__main__":
    target_location = "1234 Main Street, Los Angeles, CA 90001"
    sat_surveillance(target_location)