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

# Extract the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find and print all lines containing "contributions"
found_contributions = False

for line in soup.find_all(string=True):
    if "contributions" in line:
        found_contributions = True
        print(f"Line with 'contributions': {line.strip()}")
        
        # Attempt to extract the number from the previous element
        if line.previous_element and line.previous_element.strip().isdigit():
            contribution_count = line.previous_element.strip()
            print(f"Total contributions: {contribution_count}")
            
            # Save the contribution count to a file
            with open("commits.txt", "w") as file:
                file.write(contribution_count)
        else:
            print("Unable to find a number for contributions.")

# If nothing was found, print a message
if not found_contributions:
    print("No contributions found")

# Close the driver
driver.quit()
