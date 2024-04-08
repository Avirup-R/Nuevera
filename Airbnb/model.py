import google.generativeai as genai
import pandas as pd
def main_model(data):
    genai.configure(api_key="AIzaSyDtEXiVnxfJxrkmGP5vxn12_kpeBgylGAQ")
    # model = genai.GenerativeModel('gemini-pro')

    df=data
    inp=''
    prompt = f"Analyze the data of the given data. It contains various listing for houses anlong with feaures and price. The various columns are 'url', 'link', 'position', 'name', 'no_of_bathrooms', 'no_of_bedrooms','no_of_beds', 'images', 'location_of_the_house', 'no_of_persons_allowed', 'rating', 'type', 'ammenities', 'price_in_rupees' respectively. The prices are in Rupees '{df}'"
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    if response:
        print('Data successfully read')
    while(1):
        inp=input("")
        if inp==-1:
            break
        response= chat.send_message(inp, stream=True)
        for chunk in response:
            print(chunk.text)
            print("_"*80)

# response = model.generate_content("Write a story about a magic backpack.")