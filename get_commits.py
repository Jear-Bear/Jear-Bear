import requests
from bs4 import BeautifulSoup

# URL to your GitHub profile
url = 'https://github.com/Jear-Bear'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the total commits
total_commits = soup.find('span', class_='text-bold color-fg-default').text.strip()

# Write the total commits to commits.md
with open("total_commits.txt", "w") as f:
    f.write(total_commits)
    print("File written to total_commits.txt")
