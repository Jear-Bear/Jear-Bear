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

# Find the element that contains "contributions in the last year"
contributions_section = soup.find_all(string="contributions")
if contributions_section:
    for contribution in contributions_section:
        # Find the parent of this string and extract the preceding number
        parent = contribution.find_parent('h2')  # 'h2' might change depending on GitHub's HTML structure
        if parent:
            number = parent.get_text(strip=True).split()[0]  # Extract the first number in the text
            print(f"Total contributions in the last year: {number}")
        else:
            print("Parent element containing contributions not found.")
else:
    print("Contributions section not found.")

# Close the browser
driver.quit()
