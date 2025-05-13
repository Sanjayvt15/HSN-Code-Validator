from google.adk.agents import Agent

import pandas as pd
import os

# Get the current file's directory
BASE_DIR = os.path.dirname(__file__)

# Build the full path to the Excel file
excel_path = os.path.join(BASE_DIR, 'HSN_SAC (1).xlsx')

# Read the Excel file
df = pd.read_excel(excel_path, dtype={'\nHSNCode': str})  # Force HSN codes to be strings



# Convert to dictionary
HSN_DATA = {}

for _, row in df.iterrows():
    code = str(row['\nHSNCode']).zfill(2)  # ensure code stays as string (e.g. '01')
    HSN_DATA[code] = {
        'description': row['Description']
    }

# Example: Access the dictionary
#print(HSN_DATA)


def get_hsn_info(hsn_code: str) -> dict:
    """Returns the description and GST rate for a given HSN code."""
    info = HSN_DATA.get(hsn_code)
    if info:
        return {
            "status": "success",
            "report": (
                f"HSN Code {hsn_code}: {info['description']}. "
    
            )
        }
    else:
        return {
            "status": "error",
            "error_message": f"No data found for HSN code '{hsn_code}'."
        }

root_agent = Agent(
    name="hsn_lookup_agent",
    model="gemini-2.0-flash",
    description="Agent to provide information about HSN codes and tax rates.",
    instruction="You are a helpful assistant who provides GST details for HSN codes.",
    tools=[get_hsn_info],
)
