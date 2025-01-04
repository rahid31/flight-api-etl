import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

url = os.getenv("baseUrl")

params = {"airline":"AXM"
}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    total = response.json().get('full_count', [])
    data = response.json().get('aircraft', [])
    print(f'Data fetched successfully. Total item:{total}')
else:
    print(f"Error: {response.status_code}")

data = pd.DataFrame(data)
print(data.head())

# Saving data
folder_path = os.getenv("SAVE_PATH")
os.makedirs(folder_path, exist_ok=True)
save_path = os.path.join(folder_path, 'flights_list.csv')

data.to_csv(save_path, index=False)

print("Flights data saved successfully")