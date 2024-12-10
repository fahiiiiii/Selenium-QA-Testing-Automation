# tests/html_tag_sequence_test.py:
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))
from helpers import init_driver, write_to_excel, log_result
from selenium.webdriver.common.by import By
import time


def test_html_tag_sequence():
    page_url = "https://www.alojamiento.io/"
    driver = init_driver()
    driver.get(page_url)

    test_results = []
    try:
        # Check for the sequence of H1-H6 tags
        tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
        for tag in tags:
            try:
                driver.find_element(By.TAG_NAME, tag)
            except:
                test_results.append(
                    log_result(
                        page_url,
                        f"{tag.upper()} Tag Existence",
                        "Failed",
                        f"{tag.upper()} tag is missing",
                    )
                )

        # If all tags are found
        test_results.append(
            log_result(
                page_url, "HTML Tag Sequence", "Passed", "All tags found in sequence"
            )
        )

    except Exception as e:
        test_results.append(log_result(page_url, "HTML Tag Sequence", "Failed", str(e)))

    # Generate Excel report
    write_to_excel(test_results, "reports/html_tag_sequence_test_report.xlsx")

    driver.quit()


if __name__ == "__main__":
    test_html_tag_sequence()
