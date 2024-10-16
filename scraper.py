from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to your GitHub profile page
driver.get("https://github.com/Jear-Bear")

# Wait for the page to fully load
time.sleep(5)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all elements containing the word "contribution"
elements_with_contribution = soup.find_all(string=lambda text: "contribution" in text.lower())

# Print out all the elements containing the word "contribution"
for element in elements_with_contribution:
    print(element)

# Close the browser
driver.quit()
