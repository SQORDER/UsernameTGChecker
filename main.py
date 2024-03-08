import re
import requests

def check_link(url):
    if not url.startswith('https://t.me'):
        url = f'https://t.me/{url}'
    response = requests.get(url)
    if response.status_code == 200:
        if 'tgme_page_title' in response.text:
            return True
    return False

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9_]{1,32}$', username) is not None

def check_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        links = file.readlines()

    valid_links = []
    for link in links:
        link = link.strip()
        if not check_link(link) and is_valid_username(link):
            valid_links.append(link)

    return valid_links

file_path = 'links.txt'  

valid_links = check_file(file_path)
print(f"Available usernames ({len(valid_links)}):")
for link in valid_links:
    print(f"@{link}")
