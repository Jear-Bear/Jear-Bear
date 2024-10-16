import requests
from bs4 import BeautifulSoup

# GitHub profile URL
url = "https://github.com/Jear-Bear"

# Send a GET request to fetch the page
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element that contains the contributions count
contributions_text = soup.find('h2', class_='f4 text-normal mb-2').text.strip()

# Extract the number of contributions from the text
total_commits = contributions_text.split(' ')[0]

# Save the total commits to a file
with open("total_commits.txt", "w") as file:
    file.write(total_commits)
