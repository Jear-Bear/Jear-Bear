import requests
from bs4 import BeautifulSoup

# URL to your GitHub profile
url = 'https://github.com/Jear-Bear'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the total commits
total_commits = soup.find('span', class_='text-bold color-fg-default').text.strip()

# Write the total commits to commits.md
with open('commits.md', 'w') as file:
    file.write(f'# Total Commits\n\nTotal Commits: {total_commits}\n')
