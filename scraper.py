from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Chrome WebDriver with options
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Start the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the GitHub profile page
driver.get("https://github.com/Jear-Bear")

# Wait for the page to fully load
time.sleep(5)

# Extract the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all text lines that contain "Created"
contributions = soup.find_all(string=lambda text: text and "Created" in text)

# Check if there are any contributions
if contributions:
    # Get the first line that starts with "Created"
    first_line = next((line.strip() for line in contributions if line.startswith("Created")), None)

    if first_line:
        # Print the first line
        print(first_line)

        # Save the first line to commits.txt
        with open("commits.txt", "w") as file:
            file.write(first_line)
else:
    print("No contributions found.")

# Close the driver
driver.quit()
