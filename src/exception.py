#sys is a built-in Python module that provides information about the Python interpreter and the running program.
import sys

# # This function receives two arguments:
# - error: The actual error message or exception.
# - error_detail: The sys module, which provides exception information.
# The purpose of this function is to create a more informative error message.
# Example - Error occurred in file [train.py]
#           line number [25]
#           error message [invalid value]
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

#     The .format() method inserts values into the placeholders.
#     {0}	file_name
#     {1}	exc_tb.tb_lineno
#     {2}	str(error)
    error_message = 'Error occured python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message,error_detail = error_detail
        ) 

    def __str__(self):
        return self.error_message


# error_detail.exc_info()
    #     This retrieves information about the current exception when called inside an active exception handler.
    # It returns three values:
    # 1. Exception type
    # 2. Exception object
    # 3. Traceback object
    # The traceback tells us where the error occurred.

# exc_info() returns three values:
# exception_type, exception_value, traceback = sys.exc_info()
# Your code uses underscores (_) for the first two values because you don't need them.
# means: ignore the exception type and exception object, and store the traceback in exc_tb.
# Important: This works when an exception is currently being handled. If there is no active exception, the returned values   will be None.

# exc_tb	Contains traceback information
# tb_frame	Gives access to the execution frame where the error occurred
# f_code	Contains information about the executing code
# co_filename	Gives the Python file name or path

# exc_tb.tb_lineno
# This gives the line number associated with the traceback frame.


# class CustomException(Exception):
# This creates a class called CustomException.
# It inherits from Python's built-in Exception class.
# Why inherit from Exception? Because you want your custom error to behave like a normal Python exception while adding your own details.
# For example, you can raise it using:
# raise CustomException("Something went wrong")