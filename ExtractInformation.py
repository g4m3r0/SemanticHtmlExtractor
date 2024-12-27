import requests
from bs4 import BeautifulSoup

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return ' '.join(soup.stripped_strings)

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

def extract_headings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headings = {}
    for level in range(1, 7):
        headings[f'h{level}'] = [header.get_text(strip=True) for header in soup.find_all(f'h{level}')]
    return headings

def main():
    url = 'https://vsr.informatik.tu-chemnitz.de/about/people/'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        text = extract_text(html_content)
        links = extract_links(html_content)
        headings = extract_headings(html_content)

        print('Text:')
        print(text)
        print('\nLinks:')
        print('\n'.join(links))
        print('\nHeadings:')
        for level, headers in headings.items():
            if headers:
                print(f'{level}:')
                print('\n'.join(headers))
    else:
        print(f'Failed to retrieve the webpage: {response.status_code}')

if __name__ == '__main__':
    main()
