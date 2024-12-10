import sys
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Add the helpers.py directory to the path for importing functions
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))

# Import the necessary helper functions
from helpers import init_driver, write_to_excel, log_result


# Function to simulate scrolling down the page
def scroll_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Function to check URL status from the page
def test_url_status_from_page():
    page_url = "https://www.alojamiento.io/"
    driver = init_driver()  # Using the helper function to initialize the driver
    driver.get(page_url)

    # Scroll to ensure all links are loaded
    scroll_page(driver)

    test_results = []

    try:
        # Extract all anchor elements (links)
        links = driver.find_elements(By.TAG_NAME, "a")
        urls = [
            link.get_attribute("href") for link in links if link.get_attribute("href")
        ]

        # Check the status of each URL
        for url in urls:
            try:
                response = requests.head(url, allow_redirects=True)
                status_code = response.status_code
                if status_code == 404:
                    test_results.append(
                        log_result(
                            url,
                            "URL Status Check",
                            "Failed",
                            f"Status code: {status_code} (Not Found)",
                        )
                    )
                else:
                    test_results.append(
                        log_result(
                            url,
                            "URL Status Check",
                            "Passed",
                            f"Status code: {status_code}",
                        )
                    )
            except Exception as e:
                test_results.append(
                    log_result(url, "URL Status Check", "Failed", f"Error: {str(e)}")
                )

    except Exception as e:
        test_results.append(
            log_result(page_url, "URL Extraction", "Failed", f"Error: {str(e)}")
        )
    finally:
        driver.quit()

    # Write the results to an Excel file using the helper function
    write_to_excel(test_results, "reports/url_status_test_report.xlsx")


if __name__ == "__main__":
    test_url_status_from_page()
