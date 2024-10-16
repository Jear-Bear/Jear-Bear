from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless Chrome
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the GitHub profile page
url = "https://github.com/Jear-Bear"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time if necessary

# Get the page source and parse it
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all h2 elements with the specified class
h2_elements = soup.find_all('h2', class_='f4 text-normal mb-2')

# Output each found h2 element
for h2 in h2_elements:
    print(h2.text.strip())

# Close the browser
driver.quit()
