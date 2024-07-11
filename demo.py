from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys

logging.info("Welcome to our custom log")
try:
    a = 1 / "10"
except Exception as e:
    raise USVisaException(e, sys) from e