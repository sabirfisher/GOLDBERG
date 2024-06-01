from PIL import Image
from io import BytesIO
import requests
import logging
import googlemaps
import time
import io
from dotenv import load_dotenv
import os
import sys
sys.path.append('c:/Users/Sabir/Documents/github clones/goldberg')
from display.print import displayText
load_dotenv()
load_dotenv("resources/env_configs/.env")

GEOCODE = os.environ.get("GEOCODE_API_KEY")
GOOGLE = os.environ.get("GOOGLE")

def street_surveillance(target_location, fov=90, pitch=0):
    gmaps = googlemaps.Client(key=GOOGLE)
    displayText("Initializing Street View surveillance...")

    try:
        displayText("Street View surveillance loaded.\nPlease Wait...")
        time.sleep(2)

        # Geocoding to get latitude and longitude
        geocode_result = gmaps.geocode(target_location)
        if not geocode_result:
            print("Geocoding failed. Unable to retrieve location coordinates.")
            return

        lat, lng = geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']
        print(f"Street Surveillance for {target_location} at coordinates ({lat}, {lng}), initiated\n")

        imgs = []
        for heading in range(0, 360, 90):
            time.sleep(1)
            street_view_url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{lng}&fov={fov}&heading={heading}&pitch={pitch}&key={GOOGLE}'
            response = requests.get(street_view_url)
            response.raise_for_status()

            imgs.append(Image.open(BytesIO(response.content)))

        total_width = sum(img.size[0] for img in imgs)
        max_height = max(img.size[1] for img in imgs)

        stitched_img = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for img in imgs:
            stitched_img.paste(img, (x_offset,0))
            x_offset += img.size[0]

        stitched_img.show()   

    except requests.RequestException as e:
        logging.error(f"Error in fetching Street View image: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in street surveillance: {e}")


if __name__ == "__main__":
    target_location = input("Enter the target location \n" + "e.g 1600 Amphitheatre Parkway, Mountain View, CA\nEnter here: ")
    street_surveillance(target_location)