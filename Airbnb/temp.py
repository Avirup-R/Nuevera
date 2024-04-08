import requests

def get_location(lat, lon):
    api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                return data['results'][0]['formatted_address']
            else:
                return 'Location not found'
        else:
            return 'Failed to retrieve data'
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example latitude and longitude (replace with your values)
latitude = 40.7128
longitude = -74.0060

# Get the location of the place
location = get_location(latitude, longitude)
print("Location:", location)
