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
lines = soup.find_all(string=lambda text: text and "Created" in text)

# Select the first line containing "Created"
if lines:
    # Remove leading/trailing spaces and line breaks
    first_line = lines[0].strip().replace('\n', ' ')
    
    # Print the first line
    print(first_line)

    # Split the line by spaces and extract the second element (the number of commits)
    commit_count = first_line.split()[1]

    # Print the extracted commit count
    print(f"Number of commits: {commit_count}")

    # Save the commit count to commits.txt
    with open("commits.txt", "w") as file:
        file.write(commit_count)
else:
    print("No lines found containing 'Created'.")

# Close the driver
driver.quit()
