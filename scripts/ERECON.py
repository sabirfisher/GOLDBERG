import logging
import requests 
from scripts.sat_surveillance import sat_surveillance
from scripts.reconbrief import recon_brief
from scripts.streetview import street_surveillance
from scripts.EWS import enhanced_web_scraping
import time

def enhanced_reconnaissance(target_location):
    try:
        # Call enhanced_web_scraping and handle its return value
        web_scraping_result = enhanced_web_scraping(target_location)
        logging.info(f"Enhanced web scraping complete for {target_location}. Result: {web_scraping_result}")
        # Proceed with other operations
        sat_images, pois = sat_surveillance(target_location) 
        logging.info(f"Satellite Surveillance complete for {target_location}. Satellite images: {sat_images}")
        street_images = street_surveillance(target_location)
        logging.info(f"Street Surveillance complete for {target_location}. Street images: {street_images}")
        # Call recon_brief and handle its return value
        briefing = recon_brief(target_location, pois)
        logging.info(f"Reconnaissance Briefing for {target_location}: {briefing}")
        ##########################################################################################
        return web_scraping_result, sat_images, street_images, briefing   
    except Exception as e:
        logging.error(f"Enhanced reconnaissance error: {e}")
        return "Error occurred during enhanced reconnaissance."
