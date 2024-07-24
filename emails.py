import pandas as pd

# Load the spreadsheet
file_path = 'C:\\Users\\20-se\\Downloads\\sheet.xlsx'  # Replace with the path to your spreadsheet
sheet_name = 'sheet1'  # Replace with your sheet name if it's different

# Read the spreadsheet
df = pd.read_excel(file_path, sheet_name=sheet_name)
print(df.columns)

# Filter the rows where the interest is 'full stack developer'
full_stack_devs = df[df['Department '] == 'Full Stack Developer']

# Extract the emails
emails = full_stack_devs['Email:']

#specify path to the file where you want to save your data.
output_path = 'C:\\Users\\20-se\\Desktop\\fsdemails.txt'

#saving all emails on your specified files
with open(output_path, 'w') as file:
    for email in emails:
        file.write(email + '\n')

# Print the confirmation msg
print(f'Emails saved to {output_path}')
