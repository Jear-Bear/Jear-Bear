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

# Find and print all lines that contain the word 'contributions'
contributions_found = False
for line in soup.stripped_strings:
    if 'contributions' in line:
        contributions_found = True
        print(line)

# If no 'contributions' were found, print a message
if not contributions_found:
    print("No contributions found.")

# Close the WebDriver
driver.quit()
