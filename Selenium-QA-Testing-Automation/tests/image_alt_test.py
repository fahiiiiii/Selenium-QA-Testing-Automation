# tests/image_alt_test.py:
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))
from helpers import init_driver, write_to_excel, log_result
from selenium.webdriver.common.by import By
import time


def test_image_alt():
    page_url = "https://www.alojamiento.io/"
    driver = init_driver()
    driver.get(page_url)

    test_results = []
    try:
        # Check for image alt attributes
        images = driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            alt_text = img.get_attribute("alt")
            if not alt_text:
                test_results.append(
                    log_result(
                        page_url,
                        "Image Alt Attribute",
                        "Failed",
                        "Image alt attribute is missing",
                    )
                )

        # If all images have alt attributes
        test_results.append(
            log_result(
                page_url,
                "Image Alt Attribute",
                "Passed",
                "All images have alt attributes",
            )
        )

    except Exception as e:
        test_results.append(
            log_result(page_url, "Image Alt Attribute", "Failed", str(e))
        )

    # Generate Excel report
    write_to_excel(test_results, "reports/image_alt_test_report.xlsx")

    driver.quit()


if __name__ == "__main__":
    test_image_alt()
