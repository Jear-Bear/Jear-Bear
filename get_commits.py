from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver (e.g., using Chrome WebDriver)
driver = webdriver.Chrome()  # Make sure you have the ChromeDriver installed and in your PATH
url = "https://github.com/Jear-Bear"
driver.get(url)

# Let the page load completely
time.sleep(3)

# Get page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the total contributions text
contributions_section = soup.find('h2', class_='f4 text-normal mb-2')

if contributions_section:
    contributions_text = contributions_section.text.strip()

    # Extract the number of contributions
    total_commits = contributions_text.split()[0]

    # Write the total commits to a file
    with open('total_commits.txt', 'w') as file:
        file.write(total_commits)

    print(f"Total commits: {total_commits}")
else:
    print("Could not find the contributions section.")

# Close the WebDriver session
driver.quit()
