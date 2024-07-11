import logging
import os

from from_root import from_root
from datetime import datetime

# Generate a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Directory to store log files
log_dir = "logs"

# Create the full path for the log file within the log directory
logs_path = os.path.join(from_root(),log_dir,LOG_FILE)

# Create the log directory if it does not exist
os.makedirs(log_dir,exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    filename=logs_path, # Set the filename for the log file
    # Set the logging format to include timestamp, logger name, log level, and message
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # Set the logging level to INFO
)