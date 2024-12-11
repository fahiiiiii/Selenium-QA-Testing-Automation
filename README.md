
# Selenium QA Testing Automation

This repository contains a Selenium-based QA testing automation framework for testing various aspects of a website. It includes scripts for testing filters, tags, sequences, data scraping, and URL status checks. Additionally, test reports are generated in Excel format, and a centralized report file is created for easier analysis.

## Project Structure

```
Project Root
├── helpers/                    # Helper modules for shared functionality
│   ├── __pycache__/            # Cached Python files
│   ├── helpers.py              # Helper functionalities for reuse the codebase 
│
├── reports/                    # Directory containing individual test reports
│   ├── currency_filter_test_report.xlsx
│   ├── h1_tag_test_report.xlsx
│   ├── html_tag_sequence_test_report.xlsx
│   ├── image_alt_test_report.xlsx
│   ├── scrape_data_test_report.xlsx
│   ├── url_status_test_report.xlsx
│
├── seleniumenv/                # Selenium virtual environment (if applicable)
│
├── tests/                      # Test scripts for specific functionalities
│   ├── currency_filter_test.py
│   ├── h1_tag_test.py
│   ├── html_tag_sequence_test.py
│   ├── image_alt_test.py
│   ├── scraped_data.py
│   ├── url_status_test.py
│
├── .gitignore                    # Git ignore file
├── centralized_test_reports.xlsx # Consolidated report of all test cases
├── combine_excel_files.py        # Script to combine individual test reports
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies for the project
```

## Features

### Automated Testing:
* Verifies website functionality such as currency filters, tag structures, image alt text, HTML tag sequences,presence of H1 tag and more.

### Test Reports:
* Each test generates an individual Excel report located in the `reports` directory.
* All reports are combined into a single centralized Excel file for convenient analysis.

### Modular Design:
* Each test is implemented as a separate Python script in the `tests` folder.

### Reusable Components:
* Helper functions stored in the `helpers` directory.

## Prerequisites

1. **Python**: Make sure Python 3.8+ is installed.
2. **Virtual Environment**:
   * It is recommended to use a virtual environment to manage dependencies.
3. **Selenium WebDriver**:
   * Download the appropriate driver for your browser (e.g., ChromeDriver for Chrome).
   * Add it to your system's PATH or the project directory.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fahiiiiii/Selenium-QA-Testing-Automation.git
   cd Selenium-QA-Testing-Automation
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv seleniumenv
   source seleniumenv/bin/activate  # On Windows: seleniumenv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure your Selenium WebDriver is configured correctly.


## Usage

### Running Tests

Navigate to the `tests` folder and execute the desired test script:

```bash
python tests/<test_script_name>.py
```

For example, to run the `currency_filter_test.py`:

```bash
python tests/currency_filter_test.py
```

### Generating Combined Report

Run the `combine_excel_files.py` script to consolidate all test reports into a single Excel file:

```bash
python combine_excel_files.py
```

The centralized report will be saved as `centralized_test_reports.xlsx` in the project root.

### Individual Reports

After running a test, an individual Excel report will be generated in the `reports` directory. Each report is named based on the test script, e.g., `currency_filter_test_report.xlsx`.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/fix:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Description of your changes"
   ```

4. Push the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
