import requests
from bs4 import BeautifulSoup
import csv
import logging
import random
from urllib.parse import urlparse, parse_qs
from transformers import pipeline
import os
import re
import time
from dotenv import load_dotenv
import sys
sys.path.append('c:/Users/Sabir/Documents/github clones/goldberg')
from display.print import displayText
load_dotenv()
load_dotenv("resources/env_configs/.env")

# Set up logging
logging.basicConfig(filename='recon.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize a text classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def is_relevant_link(url):
    irrelevant_keywords = ['google.com', 'login', 'signup', 'policy', 'terms', 'preferences', 'accounts.google.com']
    return not any(keyword in url for keyword in irrelevant_keywords)

def classify_link(link_text):
    labels = ["Article", "Image", "Video", "Blog", "News", "Research"]
    result = classifier(link_text, labels)
    return result['labels'][0]

def clean_text(text):
    # Remove newlines and extra spaces
    cleaned_text = re.sub(r'\s+', ' ', text)
    # Remove non-ASCII characters
    cleaned_text = cleaned_text.encode('ascii', 'ignore').decode('utf-8')
    # Remove URLs
    cleaned_text = re.sub(r'http\S+|www\S+', '', cleaned_text)
    # Remove email addresses
    cleaned_text = re.sub(r'\S+@\S+', '', cleaned_text)
    # Remove phone numbers
    cleaned_text = re.sub(r'\b\d{10}\b', '', cleaned_text)
    # Remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    # Remove extra spaces
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def format_text(text):
    words = text.split()
    formatted_text = ''
    for i in range(0, len(words), 14):
        line = ' '.join(words[i:i+14])
        formatted_text += line + '\n'
    return formatted_text

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        return clean_text(text)
    except Exception as e:
        logging.error(f"Error extracting text from {url}: {e}")
        return ""

# Function to call the Endato People Search API
def endato_people_search(api_key, address):
    url = 'https://api.endato.com/v1/people-search'
    params = {
        'key': api_key,
        'address': address
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Endato API error: {response.status_code} - {response.text}")
        return None

def enhanced_web_scraping(target_location, endato_api_key):
    search_query = f"{target_location}"
    search_url = f'https://www.google.com/search?q={search_query}'
    output_data = []

    try:
        displayText("\nStarting enhanced web scraping...")
        response = requests.get(search_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        found_links = []
        for a in soup.find_all('a', href=True):
            raw_url = a['href']
            if 'url?q=' in raw_url and is_relevant_link(raw_url):
                parsed_url = urlparse(raw_url)
                query_string = parse_qs(parsed_url.query)
                url = query_string.get('q', [None])[0]
                if url:
                    link_text = a.get_text(strip=True)
                    if link_text:
                        link_type = classify_link(link_text)
                        found_links.append([link_text, url, link_type])

        merged_text_file_name = f"{target_location.replace(' ', '_')}_merged_text.txt"
        with open(merged_text_file_name, 'w', encoding='utf-8') as merged_text_file:
            with open(f'{target_location.replace(" ", "_")}_data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Link Text", "URL", "Type"])

                for link in found_links:
                    link_text, url, link_type = link
                    extracted_text = extract_text_from_url(url)
                    merged_text_file.write(extracted_text + "\n\n")
                    writer.writerow([link_text, url, link_type])
                    print(f"Extracted text from {url}")
                    logging.info(f"Extracted text from {url}")

        print(f"Data saved to {target_location.replace(' ', '_')}_data.csv")
        print(f"All extracted text merged in {merged_text_file_name}")
        logging.info(f"All extracted text merged in {merged_text_file_name}")

        # Call Endato People Search API and handle its return value
        endato_result = endato_people_search(endato_api_key, target_location)
        if endato_result:
            logging.info(f"Endato People Search complete for {target_location}. Result: {endato_result}")
        else:
            logging.error(f"Failed to retrieve data from Endato for {target_location}")
        
        return f"Data and merged text saved, Endato search result: {endato_result}"
    except requests.RequestException as e:
        logging.error(f"Web scraping error: {e}")
        return "Error in web scraping"

# Example usage
endato_api_key = 'YOUR_API_KEY'
target_location = '1234 Main Street, Los Angeles, CA'
result = enhanced_web_scraping(target_location, endato_api_key)
print(result)
