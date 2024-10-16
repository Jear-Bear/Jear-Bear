from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver options
chrome_options = Options()
options = [
    "--headless",
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

# Initialize the Chrome driver with service and options
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Your scraping logic goes here
driver.get("https://github.com/Jear-Bear")

# Wait for the page to load
time.sleep(5)

# Extract the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the contributions block
contribution_block = None
for line in soup.find_all(string=True):
    if "contributions" in line and "in the last year" in line.next_element:
        contribution_block = line.previous_element.strip()
        break

# Check if contribution_block has a valid value
if contribution_block:
    # Clean up the number by removing spaces/newlines
    contribution_count = contribution_block.replace(" ", "").strip()

    # Print the result
    print(f"Total contributions: {contribution_count}")

    # Save the contribution count to a file
    with open("commits.txt", "w") as file:
        file.write(contribution_count)
else:
    print("No contributions found")

# Close the driver
driver.quit()
