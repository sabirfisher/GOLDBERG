import openai
import logging
from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import os 
from dotenv import load_dotenv
import time
import sys
from display.print import displayText
load_dotenv()
load_dotenv("resources/env_configs/.env")
OPENAI_API_KEY = os.environ.get("OPENAI")
openai.api_key = OPENAI_API_KEY
# OpenAI and Transformers setup
TF_ENABLE_ONEDNN_OPTS=0
# Load environment variables

sentiment_analyzer = pipeline("sentiment-analysis")
ner_model = "dbmdz/bert-large-cased-finetuned-conll03-english"
tokenizer = AutoTokenizer.from_pretrained(ner_model)
model = AutoModelForTokenClassification.from_pretrained(ner_model)
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Setup logging
logging.basicConfig(filename='recon.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def recon_brief(target_location, pois):
    """Generates a mission briefing based on the target location and points of interest."""
    logging.info(f"Generating mission briefing for {target_location}...")
    try:
        # Assuming the enhanced_web_scraping function returns a string of text about the location
        
        # Summarize the findings
        poi_summary = "\n".join([f"POI: {poi['name']} - Type: {poi['types'][0]}" for poi in pois])

        # Compile the briefing
        brief_input = displayText(input(str("Make me a recon that will... \n")))
        briefing = f"Tactical Reconnaissance Briefing for {target_location}:\n\n" \
                   f"Make a recon brief that will {brief_input} \n" \
                   f"Points of Interest:\n{poi_summary}"

        # Log and display the briefing
        logging.info(briefing)
        
        # Optionally, use OpenAI to further process or summarize the briefing
        response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=briefing, max_tokens=1024)
        processed_briefing = response.choices[0].text.strip()
        displayText(processed_briefing)
        
    except Exception as e:
        logging.error(f"Error during mission briefing generation: {e}")
        return "An error occurred while generating the mission briefing."

if __name__ == "__main__":
    target_location = input("Enter the target location \n" + 
                                "e.g 1600 Amphitheatre Parkway,"
                                "Mountain View, CA, \n Enter here: ")

    pois = []  # Example POI
    recon_brief(target_location, pois)