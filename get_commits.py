import requests

# Hardcoded URL
url = 'https://github.com/Jear-Bear'

# Fetch HTML from the specified URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print(f"Failed to retrieve HTML. Status code: {response.status_code}")
