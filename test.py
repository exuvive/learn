import requests
from zyte_api import ZyteAPI
import random

# Create a ZyteClient instance
client = ZyteAPI(api_key = "3f2342881ea14436acb497b845399074")

# Define a list of allowed country codes
allowed_countries = ["US", "CA", "MX"] 

# Read URLs from CSV file
with open("urls.csv", "r") as f:
    urls = f.read().splitlines()

# Shuffle the list of URLs randomly
random.shuffle(urls)


# Iterate through URLs and take screenshots
for url in urls:
    try:
        # Select a random country from the allowed list
        country_code = random.choice(allowed_countries) 

        # Render the page with the specified country code
        response = client.get({"url": url, "httpResponseBody": True, "screenshot": True, "geolocation":country_code})

        # Save the screenshot to a file
        # with open(f"{url.replace('/', '-')}_{country_code}.png", "wb") as f:
        #    f.write(screenshot_data)

        print("Screenshot saved for {url} from {country_code}")

    except Exception as e:
        print("Error processing {url}: {e}")
