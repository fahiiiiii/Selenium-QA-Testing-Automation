# tests/currency_filter_test.py:
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "helpers"))
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import init_driver, write_to_excel, log_result

# Initialize WebDriver using the helper function
driver = init_driver()
test_url = "https://www.alojamiento.io/"
driver.get(test_url)

# Prepare data for the report
report_data = []

# Scroll the window to the bottom to ensure the footer is in view
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait to ensure the page is fully loaded and scrolled

# Wait for the footer to be visible
try:
    footer = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-wrapper"))
    )
    print("Footer is visible")
except Exception as e:
    print("Error while waiting for footer: ", e)

# Capture the "Property Price Before" before clicking on the currency dropdown
try:
    property_price_before_text = driver.find_element(
        By.CSS_SELECTOR, ".js-price-value"
    ).text
    print(f"Property Price Before: {property_price_before_text}")
except Exception as e:
    print("Error while capturing Property Price Before: ", e)

# Find the currency dropdown and open it
try:
    currency_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "js-currency-sort-footer"))
    )
    print("Currency dropdown is clickable")
    currency_dropdown.click()
except Exception as e:
    print("Error while clicking currency dropdown: ", e)

# Wait for the currency options to become visible
try:
    currency_options = WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "#js-currency-sort-footer .select-ul li")
        )
    )
    print(f"Found {len(currency_options)} currency options")
except Exception as e:
    print("Error while waiting for currency options: ", e)


# Extract numeric price values from the text (to handle cases like 'De $95' or 'De $184')
def extract_numeric_price(price_text):
    """Extracts the numeric price from a string like 'De $152'"""
    match = re.search(r"\d[\d,]*\.?\d*", price_text)
    if match:
        return float(
            match.group().replace(",", "")
        )  # Remove commas and return the price as float
    return 0.0


# Loop through all currency options and perform the test
for selected_currency in currency_options:
    # Capture the "Property Price Before"
    try:
        property_price_before_text = driver.find_element(
            By.CSS_SELECTOR, ".js-price-value"
        ).text
        print(
            f"Property Price Before for {selected_currency.text.strip()}: {property_price_before_text}"
        )
    except Exception as e:
        print(f"Error while capturing Property Price Before: {e}")

    # Ensure the currency option is scrolled into view
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", selected_currency)
        time.sleep(1)  # Ensure it’s fully in view
    except Exception as e:
        print("Error while scrolling the currency option into view:", e)

    # Try clicking the currency option
    try:
        print(f"Selecting currency: {selected_currency.text.strip()}")
        driver.execute_script("arguments[0].click();", selected_currency)
        time.sleep(2)  # Wait for the price to update
    except Exception as e:
        print(f"Error while selecting currency: {e}")

    # Capture the "Property Price After"
    try:
        property_price_after_text = driver.find_element(
            By.CSS_SELECTOR, ".js-price-value"
        ).text
        print(
            f"Property Price After for {selected_currency.text.strip()}: {property_price_after_text}"
        )
    except Exception as e:
        print(f"Error while capturing Property Price After: {e}")

    # Extract numeric price values
    property_price_before = extract_numeric_price(property_price_before_text)
    property_price_after = extract_numeric_price(property_price_after_text)

    # Determine if the test passed or failed
    
    status = "Passed" if property_price_before != property_price_after else "Failed"
    # comments = f"Currency changed successfully to {selected_currency.text.strip()}"
    # Print the outer HTML of the element to verify it
    currency_html = selected_currency.find_element(By.CSS_SELECTOR, '.option p').get_attribute('outerHTML')

    # Use regex to extract the currency code (e.g., "BDT")
    match = re.search(r'\((.*?)\)', currency_html)

    if match:
        currency_code = match.group(1)  # Extract the part inside the parentheses
        comments = f"Currency changed successfully to {currency_code}"
    # comments = f"Currency changed successfully to {selected_currency.find_element(By.CSS_SELECTOR, '.option p').get_attribute('outerHTML')}"

    # Log the result using the helper function
    report_data.append(log_result(test_url, "Currency Filter Test", status, comments))

# Write the report to an Excel file using the helper function
write_to_excel(report_data, "reports/currency_filter_test_report.xlsx")


# Close the browser
driver.quit()
