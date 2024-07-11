import os
import sys

def error_message_details(error, error_detail:sys):
    """
    Function to extract detailed error message information.

    Args:
    error (Exception): The exception object.
    error_detail (sys): The sys module to get exception information.

    Returns:
    str: Formatted error message with script name, line number, and error message.
    """
    # Extract traceback information
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format the error message with filename, line number, and error message
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class USVisaException (Exception):

    def __init__(self, error_message, error_detail):
        
        # Call the base class constructor
        super().__init__(error_message)
        # Store the detailed error message
        self.error_message = error_message_details(
            error_message,error_detail
        )

    def __str__(self):
        """
        Return the error message when the exception is converted to a string.
        """
        return self.error_message
