from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
chrome_options = Options()
options = [
    "--headless",  # Run in headless mode for CI
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

# Initialize the WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to your desired URL
driver.get('http://nytimes.com')

# Print the page title
print(driver.title)

# Close the driver
driver.quit()
