import requests
from bs4 import BeautifulSoup

# Define the GitHub URL for your profile
url = "https://github.com/Jear-Bear"

# Send an HTTP request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the total contributions text
contributions_section = soup.find('div', class_='js-early-contributions')
contributions_text = contributions_section.find('h2', class_='f4 text-normal mb-2').text.strip()

# Extract the number of contributions
total_commits = contributions_text.split()[0]

# Write the total commits to a file
with open('total_commits.txt', 'w') as file:
    file.write(total_commits)

print(f"Total commits: {total_commits}")
