import requests 
import logging 
from dotenv import load_dotenv 
import os 
import json 

load_dotenv()

logging.basicConfig(filename='endato.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def endato(user, password, address_line1, address_line2):
    url = "https://devapi.endato.com/address/id"
    headers = {
        "galaxy-ap-name": "8656891d-63fb-4973-9653-f2b48035d7f9",
        "galaxy-ap-password": "8942b932e6984ca5bd0f387dfd16aabe",
        "galaxy-search-type": "DevAPIAddressID",
        "content-type": "application/json"
    }
    data = {
        "addressLine1": address_line1,
        "addressLine2": address_line2
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10) 
        response.raise_for_status()
    
        with open("endato.json", "w") as f:
            json.dump(response.json(), f, indent=4)
        return response.json()

    except requests.RequestException as e:
        print("Error in fetching address data: ", e)
        logging.error(f"Error in fetching address data: {e}")
        return {}
    
if __name__ == "__main__":
    endatoUser = os.environ.get("ENDATO_USER")
    endatoPass = os.environ.get("ENDATO_PASS")
    addressLine1 = "1112 Meyers St"
    addressLine2 = "Clute, Tx 77531"

    result = endato(endatoUser, endatoPass, addressLine1, addressLine2)
    print(result)
    logging.info(result)
