from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headlessly
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Replace with the desired GitHub URL
url = "https://github.com/Jear-Bear"
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)

# Get the contributions element
contributions_section = driver.find_element("css selector", "h2.f4.text-normal.mb-2")

# Output the contributions text
contributions_text = contributions_section.text.strip()
print(contributions_text)

# Clean up
driver.quit()
