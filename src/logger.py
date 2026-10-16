#In a data science project, logging helps you record what your code is doing, when something happens, and where an error occurs. Think of it as a diary for your Python application.
# For example, suppose you build a machine learning model to predict IPL scores. If the model fails during training, logs can help you identify what happened without running the entire project again blindly.
import logging 

# Provides functionality for reading and writing to the file system 
import os
from datetime import datetime

# logs_path	- Path to the folder
# log_file	- Name of the file
# log_file_path - Full path to the file

log_file = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
logs_path = os.path.join(os.getcwd(),'logs') 

os.makedirs(logs_path, exist_ok = True)

log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# %(asctime)s - Date and time when the log record was created
# %(lineno)d - Line number where the logging call was made
# %(name)s - Logger name, often root when using the default logger
# %(levelname)s	- Severity level, such as INFO or ERROR
# %(message)s - The actual message you wrote

# Remember this for a data science interview: Logging is used to monitor an application's execution, track important events, diagnose errors, and make debugging easier. It is especially valuable when your project has multiple steps, such as data ingestion, preprocessing, feature engineering, model training, and prediction.