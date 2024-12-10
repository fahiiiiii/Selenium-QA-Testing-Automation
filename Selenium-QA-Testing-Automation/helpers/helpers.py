# helpers/helpers.py:
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function to initialize the WebDriver
def init_driver():
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service('/home/w3e37/Downloads/chromedriver-linux64/chromedriver'), options=options)
    return driver

# Function to write test results to Excel
# def write_to_excel(report_data, filename):
#     df = pd.DataFrame(report_data)
#     df.to_excel(filename, index=False)
def write_to_excel(report_data, filename):
    """Writes data to an Excel file and overwrites if the file exists."""
    df = pd.DataFrame(report_data)
    df.to_excel(filename, index=False, engine='openpyxl')  # No 'mode' argument, just engine='openpyxl'
    print(f"Report written to {filename}")


# Function to log the test result for a specific test case
def log_result(page_url, test_case, passed, comments):
    return {
        "page_url": page_url,
        "testcase": test_case,
        "passed": passed,
        "comments": comments
    }
