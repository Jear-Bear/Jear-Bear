from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

# Set up Chrome driver with service and options
service = Service(executable_path=r'/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the GitHub profile page
driver.get("https://github.com/Jear-Bear")

# Wait for the page to load
time.sleep(5)

# Extract the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all the text on the page
all_text = soup.find_all(string=True)

# Print each line of text found
if all_text:
    for line in all_text:
        print(line.strip())
else:
    print("No text found on the page.")

# Close the driver
driver.quit()
