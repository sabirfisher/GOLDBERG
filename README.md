# GOLDBERG
![image](https://github.com/sabirfisher/GOLDBERG/assets/125846300/fe86b08e-c268-48c2-a083-03f654af02b5)

Features:

    Satellite Surveillance (sat_surveillance): Fetches and processes satellite images from multiple zoom levels for any given location.

    Street Surveillance (streetview): Gathers street-level imagery to provide ground perspectives and enhance the understanding of the physical environment.

    Enhanced Web Scraping (EWS): Aggregates online data and metadata related to the target location for digital reconnaissance.

    Reconnaissance Briefing (reconbrief): Compiles data from various modules into concise reports, offering clear and actionable intelligence.

How to Use:

    Verify and make sure you have the following API Keys:
        OpenCage - for geocoding services.
        OpenAI - for AI-powered analysis and data interpretation.
        Google Maps - for satellite and street-level imagery.

    Clone the repository and navigate into the GOLDBERG directory.

    Install dependencies using pip install -r requirements.txt.

    Set up your .env configurations with necessary API keys in the env_configs directory.

    Run goldberg.py in your terminal with your target location and briefing request to initiate the reconnaissance process. Example command:

    python goldberg.py "1600 Amphitheatre Parkway, Mountain View, CA"

Logs and Configurations:

    Logs are meticulously maintained for each session, stored sequentially in the resources/logs directory. Environment configurations are easily manageable via .env files in the env_configs directory.
    Dependencies:
    
    The suite leverages a stack of Python libraries and external APIs, detailed in the requirements.txt file. API keys for Google Maps and other services are required.


Notes to Consider:

    GOLDBERG is an open-source initiative and, as with many projects in their early release stages, there may be features that are still under development or require further testing. Your feedback and contributions are invaluable to us.
    
    Should you encounter any issues or have suggestions for improvement, please do not hesitate to reach out. Talk to me on Discord at "cxsmoswrld" to discuss, report bugs, or seek support.
