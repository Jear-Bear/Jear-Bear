import requests

url = 'https://github.com/Jear-Bear'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text

    # Split the HTML content into lines
    lines = html_content.splitlines()

    # Filter lines that contain the word "commit"
    commit_lines = [line for line in lines if 'commit' in line.lower()]

    # Output the filtered lines
    for line in commit_lines:
        print(line)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
