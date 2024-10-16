from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re

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

# Find all lines containing "contributions in"
lines = soup.find_all(string=lambda text: text and "contributions in" in text.lower())

# Check if any lines contain the contributions count
if lines:
    # Select the first line found
    first_line = lines[0].strip().replace('\n', ' ')
    print(f"Extracted line: {first_line}")  # Print the line for debugging

    # Use regex to find the contributions count
    match = re.search(r'(\d+)\s+contributions\s+in', first_line)
    if match:
        contributions_count = match.group(1)  # Extract the first match
        print(f"Number of contributions: {contributions_count}")

        # Replace the contributions count in README.md
        with open("README.md", "r") as file:
            readme_content = file.readlines()

        # Update the line with the new contributions count
        for i, line in enumerate(readme_content):
            if "Total Commits" in line:
                # Replace whatever is between the specific markers with the contributions count
                readme_content[i] = re.sub(r'Total_Commits-\d+', f'Total_Commits-{contributions_count}', line)
                break

        # Write back the updated README.md
        with open("README.md", "w") as file:
            file.writelines(readme_content)

else:
    print("No lines found containing contributions count.")

# Close the driver
driver.quit()
