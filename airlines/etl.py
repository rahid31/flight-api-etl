import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# RAPID API Credentials
baseUrl = os.getenv("airlineUrl")

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
}

# Fetching data
response = requests.get(baseUrl, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json().get('rows', [])
    print('Data fetched successfully')
else:
    print(f"Error: {response.status_code}")

# Creating dataframe
data = pd.DataFrame(data)
print(data.head())

# Saving data
folder_path = os.getenv("AIRLINE_SAVE_PATH")
os.makedirs(folder_path, exist_ok=True)
save_path = os.path.join(folder_path, 'airline_lists.csv')

data.to_csv(save_path, index=False)

print("Airlines data saved successfully")
