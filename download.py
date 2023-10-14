import requests
import json

def download_json(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()

            # Save the JSON data to a file
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

            print(f"JSON data downloaded and saved to {output_file}")
        else:
            print(f"Failed to download JSON data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")