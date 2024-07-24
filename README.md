# Email Extractor Script

This script extracts the emails of students interested in full stack development from an Excel spreadsheet and saves them to a plain text file.

## Prerequisites

- Python 3.x
- pandas library
- openpyxl library

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries using pip:
    ```bash
    pip install pandas openpyxl
    ```

## Usage

1. Place your Excel file in the specified location (e.g., Downloads folder).
2. Update the `file_path` variable in the script with the path to your Excel file.
3. Update the `output_path` variable in the script with the desired path for the output text file.
4. Run the script.

### Example

```python
import pandas as pd

# Specify the path to your file
file_path = 'C:\\Users\\YourUsername\\Downloads\\your_spreadsheet.xlsx'  # For Windows
# file_path = '/Users/YourUsername/Downloads/your_spreadsheet.xlsx'  # For macOS or Linux

# Load the spreadsheet
sheet_name = 'Sheet1'  # Replace with your sheet name if it's different

# Read the spreadsheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Print the column names to verify
print(df.columns)

# Filter the rows where the interest is 'full stack developer'
full_stack_devs = df[df['Interest'] == 'full stack developer']

# Extract the emails
emails = full_stack_devs['Email']

# Specify the path to save the new file on your desktop
output_path = 'C:\\Users\\YourUsername\\Desktop\\full_stack_devs_emails.txt'  # For Windows
# output_path = '/Users/YourUsername/Desktop/full_stack_devs_emails.txt'  # For macOS or Linux

# Save the emails to a text file
with open(output_path, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f'Emails saved to {output_path}')
