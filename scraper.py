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

# Extract all the text from the page as a list of lines
page_text = soup.get_text().splitlines()

# Loop through each line to find the desired pattern
for i in range(len(page_text) - 2):
    if "contributions" in page_text[i + 1] and "in the last year" in page_text[i + 2]:
        # Save the number to a file
        with open("commits.txt", "w") as file:
            file.write({page_text[i]})
        break
        
# Close the driver
driver.quit()

# Git configuration and commit
os.system("git config user.name 'Automated'")
os.system("git config user.email 'actions@users.noreply.github.com'")
os.system("git add commits.txt")
os.system("git commit -m 'Update commits.txt with latest contributions'")
os.system("git push")
