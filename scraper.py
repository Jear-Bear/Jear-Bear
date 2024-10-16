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
contributions = [line.strip() for line in soup.find_all(string=lambda text: text and "Created" in text)]

# Check if there are at least two contributions
if len(contributions) >= 2:
    # Get the second line that starts with "Created"
    second_line = contributions[1]

    if second_line:
        # Print the second line
        print(second_line)

        # Save the second line to commits.txt
        with open("commits.txt", "w") as file:
            file.write(second_line)
else:
    print("Less than two contribution lines found.")

# Close the driver
driver.quit()
