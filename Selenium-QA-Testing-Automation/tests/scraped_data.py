# # tests/scraped_data.py
# import sys
# import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))
# from helpers import init_driver, write_to_excel, log_result
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Define constants
# URL = "https://www.alojamiento.io/"

# # Initialize WebDriver
# driver = init_driver()

# try:
#     # Open the target website
#     driver.get(URL)

#     # Wait for the page to load
#     wait = WebDriverWait(driver, 10)

#     # Extract data from script or HTML
#     data = {}
#     try:
#         # Locate the script tag or specific elements containing data
#         data["SiteName"] = "alo"  # Replace with actual scraping logic
#         data["SiteUrl"] = URL
#         data["Browser"] = (
#             "Chrome"  # Replace with actual browser detection logic if needed
#         )
#         data["CountryCode"] = "BD"  # Replace with scraped value
#         data["IP"] = "182.160.106.203"  # Replace with scraped value
#         data["CampaignId"] = "ALOJAMIENTO"
#     except Exception as e:
#         print(f"Error extracting data: {e}")

#     # Log result
#     report_data = [log_result(URL, "Data Extraction Test", True, data)]

#     # Save to Excel
#     output_file = "scraped_data.xlsx"
#     write_to_excel(report_data, output_file)
#     print(f"Data saved to {output_file}")

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     # Close the WebDriver
#     driver.quit()
import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to initialize the WebDriver
def init_driver():
    options = Options()
    # Uncomment for headless mode
    # options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service("/home/w3e37/Downloads/chromedriver-linux64/chromedriver"),
        options=options,
    )
    return driver


# Function to write test results to Excel
def write_to_excel(report_data, filename):
    df = pd.DataFrame(report_data)
    df.to_excel(filename, index=False)


# Function to log the test result for a specific test case
def log_result(site_url, test_case, passed, comments):
    return {
        "SiteURL": site_url,
        "TestCase": test_case,
        "Passed": passed,
        "Comments": comments,
    }


# Function to scrape data from window.ScriptData
def scrape_data_from_script():
    driver = init_driver()
    driver.get("https://www.alojamiento.io/")  # Replace with the target URL

    # Wait for the page content to load (adjust waiting conditions if needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "script"))
    )

    test_results = []

    try:
        # Access window.ScriptData using JavaScript execution
        script_data = driver.execute_script("return window.ScriptData;")

        if script_data:
            # Extract relevant data from window.ScriptData
            config = script_data.get("config", {})
            site_info = config.get(
                "SiteInfo", {}
            )  # If needed, you can still access SiteInfo, but SiteUrl and SiteName are in config
            user_info = script_data.get("userInfo", {})
            page_data = script_data.get("pageData", {})

            # Extract the correct values directly from config
            site_url = config.get("SiteUrl", "N/A")
            site_name = config.get("SiteName", "N/A")

            # Extract CampaignId from pageData
            campaign_id = page_data.get("CampaignId", "N/A")

            # Prepare the data to record in the report
            data = {
                "SiteURL": site_url,
                "CampaignID": campaign_id,
                "SiteName": site_name,
                "Browser": user_info.get("Browser", "N/A"),
                "CountryCode": user_info.get("CountryCode", "N/A"),
                "IP": user_info.get("IP", "N/A"),
            }

            # Use the SiteURL as the page URL for the report
            test_results.append(
                log_result(site_url, "ScriptData Extraction", "Passed", str(data))
            )
        else:
            test_results.append(
                log_result(
                    "N/A", "ScriptData Extraction", "Failed", "No ScriptData found."
                )
            )

    except Exception as e:
        test_results.append(
            log_result("N/A", "ScriptData Extraction", "Failed", str(e))
        )

    # Write results to Excel
    write_to_excel(test_results, "reports/scrape_data_test_report.xlsx")

    driver.quit()


if __name__ == "__main__":
    scrape_data_from_script()
