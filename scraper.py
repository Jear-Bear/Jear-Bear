from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

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

# Find the contributions block
contribution_block = None
for line in soup.find_all(string=True):
    if "contributions" in line and "in the last year" in line.next_element:
        contribution_block = line.previous_element.strip()
        break

# Check if contribution_block has a valid value
if contribution_block:
    # Clean up the number by removing spaces/newlines
    contribution_count = contribution_block.replace(" ", "").strip()

    # Print the result
    print(f"Total contributions: {contribution_count}")

    # Save the contribution count to a file
    with open("commits.txt", "w") as file:
        file.write(contribution_count)
else:
    print("No contributions found")

# Close the driver
driver.quit()
