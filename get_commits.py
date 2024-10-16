# Import necessary libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to your GitHub contributions page
driver.get("https://github.com/Jear-Bear")

# Give the page some time to load
time.sleep(5)

# Extract the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the total commits count
total_commits = soup.find('h2', class_='f4 text-normal mb-2').get_text(strip=True)

# Write the total commits count to a file
with open("total_commits.txt", "w") as file:
    file.write(total_commits)  # total_commits now holds the correct text

# Close the driver
driver.quit()
