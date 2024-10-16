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

# Extract the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all text lines that start with "Created"
created_lines = soup.find_all(string=lambda text: text and text.lower().startswith("created"))

# Print each line that starts with "Created"
if created_lines:
    for line in created_lines:
        print(line.strip())
else:
    print("No lines starting with 'Created' found on the page.")

# Close the driver
driver.quit()
