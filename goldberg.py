import logging
import datetime
import os
from scripts.ERECON import enhanced_reconnaissance
from display.ui import GOLDBERG
from display.print import displayText

import pathlib
pathlib.Path(__file__).parent.resolve()

# Function to find the next log file name based on existing files
def logger():
    log_directory = './resources/logs'  # Change this to your log files directory if different
    log_prefix = 'recon'
    log_suffix = '.log'
    existing_logs = [filename for filename in os.listdir(log_directory) if filename.startswith(log_prefix) and filename.endswith(log_suffix)]
    highest_num = 0
    for log in existing_logs:
        num_part = log[len(log_prefix):-len(log_suffix)]
        if num_part.isdigit():
            highest_num = max(highest_num, int(num_part))
    new_log_filename = f"{log_prefix}{highest_num + 1}{log_suffix}"
    return os.path.join(log_directory, new_log_filename)

# Determine the filename for the new log and setup logging
logging_sys = logger()
logging.basicConfig(filename=logging_sys, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# GREETING & TARGET LOCATION INPUT
GOLDBERG()
current_time = datetime.datetime.now()
greeting = "\nGood Morning" if current_time.hour < 12 else "Good Afternoon" if current_time.hour < 18 else "Good Evening"
displayText(greeting)
target_location = input("Enter the target location \n" + "e.g 1600 Amphitheatre Parkway, Mountain View, CA\nEnter here: ")

# MAIN FUNCTION TO RUN RECONNAISSANCE
if __name__ == "__main__":
    logging.info("Starting enhanced reconnaissance...")
    result = enhanced_reconnaissance(target_location)
    if result != "Error occurred during enhanced reconnaissance.":
        displayText("Reconnaissance has been logged, please view " + logging_sys + " for more information.")
    else:
        print("Reconnaissance failed. Check logs for details.")
    logging.info("Enhanced reconnaissance completed.")
