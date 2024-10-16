from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the Chrome driver with options
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Initialize the driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# Navigate to your GitHub contributions page
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
