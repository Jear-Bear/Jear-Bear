from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re  # Import the regex module

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

# Find all text lines that contain "contributions in"
lines = soup.find_all(string=lambda text: text and "contributions in" in text)

# Select the first line containing contributions
if lines:
    first_line = lines[0].strip().replace('\n', ' ')
    
    # Print the first line
    print(first_line)

    # Use regex to find a four-digit number after "contributions in"
    match = re.search(r'(\d{4})', first_line)
    
    if match:
        contributions_count = match.group(1)  # Extract the first match (the four-digit number)
        
        # Print the extracted contributions count
        print(f"Number of contributions: {contributions_count}")

        # Save the contributions count to README.md
        with open("README.md", "r") as file:
            content = file.readlines()
        
        # Update the specific line with the contributions count
        for i in range(len(content)):
            if "![Total Commits](https://img.shields.io/badge/Total_Commits-" in content[i]:
                content[i] = f"![Total Commits](https://img.shields.io/badge/Total_Commits-{contributions_count}-green)\n"
                break
        
        # Write the updated content back to the README.md file
        with open("README.md", "w") as file:
            file.writelines(content)
    else:
        print("No four-digit contributions count found.")
else:
    print("No lines found containing 'contributions in'.")

# Close the driver
driver.quit()
