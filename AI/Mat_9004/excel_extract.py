import pandas as pd

def excel_to_dict(file_path, sheet_name):
    try:
        # Read data from Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Convert DataFrame to dictionary
        data_dict = df.to_dict(orient='records')

        return data_dict

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
file_path = 'your_excel_file.xlsx'
sheet_name = 'Sheet1'  # Replace with the actual sheet name in your Excel file

result = excel_to_dict(file_path, sheet_name)

if result:
    print("Data successfully converted to dictionary:")
    print(result)
else:
    print("Error occurred while processing the Excel file.")
