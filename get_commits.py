from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the GitHub profile
url = "https://github.com/Jear-Bear"

# Open the URL
driver.get(url)

# Get the page source and parse it
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all h2 elements with the specific class
h2_elements = soup.find_all('h2', class_='f4 text-normal mb-2')

# Write the contributions to commits.md
with open('commits.md', 'w') as file:
    for h2 in h2_elements:
        file.write(h2.get_text(strip=True) + '\n')

# Close the driver
driver.quit()
