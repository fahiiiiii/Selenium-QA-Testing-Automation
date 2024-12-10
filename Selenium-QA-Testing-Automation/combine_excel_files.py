import pandas as pd
import os

# Directory where the report Excel files are stored
reports_dir = "reports"
output_file = "centralized_test_reports.xlsx"

# Create a Pandas Excel writer object
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    # Loop through all files in the reports directory
    for file_name in os.listdir(reports_dir):
        if file_name.endswith(".xlsx"):  # Check if the file is an Excel file
            # Construct the full file path
            file_path = os.path.join(reports_dir, file_name)
            
            # Read the Excel file into a DataFrame
            try:
                df = pd.read_excel(file_path)
                # Add it as a new sheet in the centralized workbook
                sheet_name = os.path.splitext(file_name)[0]  # Use file name as sheet name
                df.to_excel(writer, index=False, sheet_name=sheet_name)
                print(f"Added {file_name} as sheet {sheet_name}")
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")

print(f"Centralized report saved to {output_file}")
