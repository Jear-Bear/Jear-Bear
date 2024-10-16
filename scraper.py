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
contribution_activity = None
for line in soup.find_all(string=True):
    if line.startswith("Created"):
        contribution_activity = line
        break

if contribution_activity:
    # Split the line and extract the number of commits
    commit_count = contribution_activity.split()[1]

    # Read the README.md file
    with open("README.md", "r") as file:
        lines = file.readlines()

    # Update the specific line
    for i, line in enumerate(lines):
        if "![Total Commits](https://img.shields.io/badge/Total_Commits-" in line:
            # Replace the number with the actual commit count
            lines[i] = line.split("Total_Commits-")[0] + f"Total_Commits-{commit_count}-green)" + "\n"
            break

    # Write the updated lines back to the README.md file
    with open("README.md", "w") as file:
        file.writelines(lines)

# Close the driver
driver.quit()
