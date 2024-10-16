from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Setup Chrome driver options
chrome_service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Launch Chrome browser
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the GitHub page
driver.get("https://github.com/Jear-Bear")

# Wait for the page to load completely
time.sleep(5)

# Extract the page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract all the text from the page as a list of lines
page_text = soup.get_text().splitlines()

# Loop through each line to find the desired pattern
for i in range(len(page_text) - 2):
    if "contributions" in page_text[i + 1] and "in the last year" in page_text[i + 2]:
        print(f"Line containing number: {page_text[i]}")
        print(f"Line with 'contributions': {page_text[i + 1]}")
        print(f"Line with 'in the last year': {page_text[i + 2]}")
        break

# Close the browser
driver.quit()
