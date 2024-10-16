from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Initialize the Chrome driver
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

# Find the contributions line
commits_line = None
for line in soup.find_all(string=True):
    if line.startswith("Created"):
        commits_line = line.strip()
        break

# Check if commits_line has a valid value
if commits_line:
    # Split the line by spaces and extract the commit number
    commits_number = commits_line.split()[1]  # Extracting the second element
    print(f"Commit number extracted: {commits_number}")

    # Update README.md with the new commit number
    with open("README.md", "r") as file:
        content = file.readlines()

    # Replace the line with the commit number
    for index, line in enumerate(content):
        if "![Total Commits]" in line:
            content[index] = f"![Total Commits](https://img.shields.io/badge/Total_Commits-{commits_number}-green)\n"
            break

    # Write the updated content back to README.md
    with open("README.md", "w") as file:
        file.writelines(content)

else:
    print("No contributions found")

# Close the driver
driver.quit()
