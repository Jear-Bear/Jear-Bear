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

# Find all text lines that contain "contributions"
lines = soup.find_all(string=lambda text: text and "contributions" in text.lower())

# Check if the contributions count line is in the line text
if lines:
    for line in lines:
        line = line.strip().replace('\n', ' ')
        if "contributions" in line.lower():  # Ensure the search is case-insensitive
            print(line)  # Print the line for debugging
            # Use regex to find a four-digit number after "contributions in"
            match = re.search(r'(\d{4})', line)
            if match:
                contributions_count = match.group(1)  # Extract the first match
                print(f"Number of contributions: {contributions_count}")

                # Replace the contributions count in README.md
                with open("README.md", "r") as file:
                    readme_content = file.readlines()

                # Update the line with the new contributions count
                for i, line in enumerate(readme_content):
                    if "Total Commits" in line:
                        readme_content[i] = line.replace("xxx", contributions_count)
                        break

                # Write back the updated README.md
                with open("README.md", "w") as file:
                    file.writelines(readme_content)

                break  # Exit loop after finding the contributions count
else:
    print("No lines found containing 'contributions'.")

# Close the driver
driver.quit()
