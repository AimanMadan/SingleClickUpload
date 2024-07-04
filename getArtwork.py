import requests
import os

# List to store fetched image URLs
image_urls = []

# Function to fetch a random image from Unsplash based on the selected category
def fetch_images_from_unsplash(category, client_id):
    url = f"https://api.unsplash.com/photos/random?query={category}&client_id={client_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['urls']['regular']
    else:
        response.raise_for_status()

# Function to get the API key from a text file
def get_API(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) < 1:
            raise ValueError("The file should contain only the API key!")
        API = lines[0].strip()
    return API

# Function to fetch and store a new image URL
def fetch_and_store_image():
    filename = "UnsplashAPI.txt"
    client_id = get_API(filename)
    category = "Music"
    image_url = fetch_images_from_unsplash(category, client_id)
    image_urls.append(image_url)
    return image_url

if __name__ == "__main__":
    fetch_and_store_image()
    print("Fetched image URLs:", image_urls)
