import requests
from datetime import datetime, timedelta
import pandas as pd
from location import get_location
from model import main_model

def data_parse(location):
    url = "https://airbnb13.p.rapidapi.com/search-location"
    today = datetime.now().date()

    # Format today's date as yyyy-mm-dd
    formatted_today = today.strftime('%Y-%m-%d')

    # Add 2 weeks to today's date
    two_weeks_extra = today + timedelta(weeks=2)

    # Format the date after adding 2 weeks as yyyy-mm-dd
    formatted_two_weeks_extra = two_weeks_extra.strftime('%Y-%m-%d')
    
    querystring = {"location":location,"checkin":formatted_today,"checkout":formatted_two_weeks_extra,"adults":"2","children":"0","infants":"0","pets":"0","page":"1","currency":"INR"}

    headers = {
        ##enter your api key here
        "X-RapidAPI-Key": "0ac90eb4dbmsh6f259e6d47e26fcp1f9fb7jsnef7585df94db",
        "X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
    }



    response = requests.get(url, headers=headers, params=querystring)
    t=response.json()
    h=t['headers']
    if h['response_id']:
        print('Data Fetched')
    return t


def convert_csv(data):
    values=data["results"]
    array=[]
    for option in values:
        new=[]
        try:
            r=option['rating']
        except:
            r=2.5
        try:
            new.append(option['url'])
        except:
            new.append('No URL Available')
        try:
            new.append(option['deeplink'])
        except:
            new.append("No link available")
        try: 
            new.append(option['position'])
        except:
            new.append(0)
        try:
            new.append(option['name'])
        except:
            new.append('No name available')
        try:
            new.append(option['bathrooms'])
        except:
            new.append(0)
        try:
            new.append(option['bedrooms'])
        except:
            new.append(0)
        try:
            new.append(option['beds'])
        except:
            new.append(0)
        try:
            new.append(option['images'])
        except:
            new.append('No image avalable')
        try:
            loc=get_location(option['lat'], option['lng'])
            location=[loc]
            new.append(location)
        except:
            new.append('No location availble')
        try:
            new.append(option['persons'])
        except:
            new.append(1)
        # new.append(option['rating'])
        new.append(r)
        new.append(option['type'])
        new.append(option['previewAmenities'])
        costings=option['price']
        new.append(int(costings['total'])/14)
        array.append(new)
        

    df=pd.DataFrame(array)
    columns_names=['url', 'link', 'position', 'name', 'bathrooms', 'bedrooms','beds', 'images', 'location', 'no_of_persons_allowed', 'rating', 'type', 'ammenities', 'price_in_rupees']
    df.columns=columns_names
    with open("content.txt", 'w') as file:
        file.write(str(df))
    return df

if __name__=="__main__":
    city=input("Enter the city to explore ")
    # date=str(input("Enter the date of arrival in yyyy-mm-dd "))
    # stay_period=int(input("No of days you want to stay "))
    data=data_parse(city)
    modified_data=convert_csv(data)
    main_model(modified_data)
# print(data)