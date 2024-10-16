from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os

# Set up Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Set up the Chrome driver service using ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())

# Initialize the Chrome driver with the service and options
driver = webdriver.Chrome(service=service, options=options)

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
            number_line = contributions[i - 1].strip()  # Clean up spaces
            print("Contributions in the last year:", number_line)

            # Save the number to a file
            with open("commits.txt", "w") as file:
                file.write(number_line)

# Close the driver
driver.quit()

# Git configuration and commit
os.system("git config user.name 'Automated'")
os.system("git config user.email 'actions@users.noreply.github.com'")
os.system("git add commits.txt")
os.system("git commit -m 'Update commits.txt with latest contributions'")
os.system("git push")
