from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    url = 'https://github.com/Jear-Bear'
    driver.get(url)

    # Wait for the page to load (you might need to adjust the sleep time)
    time.sleep(3)

    # Get the page source
    html_content = driver.page_source

    # Print the HTML content (you can also write this to a file)
    print(html_content)
finally:
    driver.quit()
