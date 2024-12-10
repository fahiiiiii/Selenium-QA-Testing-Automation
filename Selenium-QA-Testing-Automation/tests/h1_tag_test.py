# tests/h1_tag_test.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))
from helpers import init_driver, write_to_excel, log_result
from selenium.webdriver.common.by import By
import time


def test_h1_tag():
    page_url = "https://www.alojamiento.io/"
    driver = init_driver()
    driver.get(page_url)

    test_results = []
    try:
        # Check for H1 tag existence
        h1_tag = driver.find_element(By.TAG_NAME, "h1")
        if h1_tag:
            test_results.append(
                log_result(page_url, "H1 Tag Existence", "Passed", "H1 tag exists")
            )
        else:
            test_results.append(
                log_result(page_url, "H1 Tag Existence", "Failed", "H1 tag is missing")
            )
    except Exception as e:
        test_results.append(log_result(page_url, "H1 Tag Existence", "Failed", str(e)))

    # Generate Excel report
    write_to_excel(test_results, "reports/h1_tag_test_report.xlsx")

    driver.quit()


if __name__ == "__main__":
    test_h1_tag()
