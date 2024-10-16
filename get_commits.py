import requests
from bs4 import BeautifulSoup

def fetch_total_commits(username):
    # Construct the GitHub profile URL
    url = f'https://github.com/{username}'

    # Send a GET request to the GitHub profile page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the total commits by navigating to the contributions section
        contributions_section = soup.find('h2', text='Contributions in the last year').find_next('div')

        # Extract the total contributions
        total_commits = contributions_section.find('span', class_='text-bold').get_text(strip=True)

        return total_commits
    else:
        print('Failed to retrieve the page')
        return None

if __name__ == '__main__':
    username = 'Jear-Bear'  # Change this to your GitHub username
    total_commits = fetch_total_commits(username)
    if total_commits:
        print(f'Total Commits: {total_commits}')
