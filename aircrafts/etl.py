import requests
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import json_normalize

load_dotenv()

# RAPID API Credentials
baseUrl = os.getenv("aircraftUrl")

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

# Flattening the 'models' column
models = data.explode('models', ignore_index=True)

# Flatten the 'models' column
flattened = pd.json_normalize(models['models'])

# Concatenate the original DataFrame with the flattened DataFrame
data = pd.concat([models.drop('models', axis=1), flattened], axis=1)

print(data.head())

# Saving data
folder_path = os.getenv("AIRCRAFT_SAVE_PATH")
os.makedirs(folder_path, exist_ok=True)
save_path = os.path.join(folder_path, 'aircraft_lists.csv')

data.to_csv(save_path, index=False)

print("Aircrafts data saved successfully")