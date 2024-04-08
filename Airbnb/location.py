import requests

def get_location(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            address = data['display_name']
            return address
        else:
            return [lat, lon]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# # Example latitude and longitude (replace with your values)
# latitude = 13.03741
# longitude= 77.62936

# # longitude = -74.0060

# # Get the location of the place
# location = get_location(latitude, longitude)
# print("Location:", location)
