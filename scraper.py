from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the GitHub profile page
driver.get("https://github.com/Jear-Bear")

# Extract the HTML content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the element that contains the "contributions in the last year" information
contributions_text = soup.find('h2', class_='f4 text-normal mb-2').get_text(strip=True)

# Use regex to extract the number of contributions
contributions_number = re.search(r'\d+', contributions_text).group()

# Print the number of contributions
print("Total Contributions in the Last Year:", contributions_number)

# Close the driver
driver.quit()
