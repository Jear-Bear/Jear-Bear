from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import os

# Set up the Chrome driver options
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

# Set up the Chrome driver service
chrome_service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the GitHub profile page
driver.get("https://github.com/Jear-Bear")

# Wait for the page to load
time.sleep(5)

# Extract the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the contributions block
contributions = soup.find_all(text="contributions")
for i in range(len(contributions)):
    if "contributions" in contributions[i]:
        if i + 1 < len(contributions) and "in the last year" in contributions[i + 1]:
            # Get the number of contributions
            number_line = contributions[i - 1]  # This should be the number line
            contribution_number = number_line.strip()  # Clean up spaces
            print("Contributions in the last year:", contribution_number)

            # Save the number to a file
            with open("commits.txt", "w") as file:
                file.write(contribution_number)

# Close the driver
driver.quit()

# Git configuration and commit
os.system("git config user.name 'Automated'")
os.system("git config user.email 'actions@users.noreply.github.com'")
os.system("git add commits.txt")
os.system("git commit -m 'Update commits.txt with latest contributions'")
os.system("git push")
