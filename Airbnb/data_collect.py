from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Function to extract details using BeautifulSoup
def extract_details(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Modify this part according to the structure of the website to extract the required details
    details = soup.find_all('div', class_='m-srp-card__desc flex__item')
    for detail in details:
        print(detail.text.strip())
    print("Total {} details found.".format(len(details)))

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()

# Path to your ChromeDriver executable
# chrome_driver_path = "C:/Users/colle/OneDrive/Desktop/Internship/Nuevera/Various_models/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options)

# Open the Magicbricks website
city='bengaluru'
driver.get(f"https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=${city}")

# Wait for the website to load
# time.sleep(5)  # Adjust the waiting time according to the website's loading speed

# Find the search box and enter the city details
# clear_box = driver.find_element("xpath", '//*[@class="mb-search__tag-t"]')
# clear_box.send_keys('')
# search_box = driver.find_element("xpath", '//*[@class="mb-search__input"]')
# search_box.send_keys("Bengaluru")  # Replace "Enter City Name" with the desired city name
# search_box.send_keys(Keys.RETURN)
# Wait for the search results to load
time.sleep(10)  # Adjust the waiting time according to the website's loading speed

page_content = driver.page_source

# Print the whole content
print(page_content)

# Get the HTML content of the page
# html_content = driver.page_source

# # Extract details using BeautifulSoup
# extract_details(html_content)

# Close the WebDriver session
driver.quit()
