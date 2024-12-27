import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def is_valid_child(child):
    if isinstance(child, Tag):
        return True
    elif isinstance(child, NavigableString):
        return bool(child.strip())
    return False

def process_node(node):
    if node.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']:
        return {
            'type': node.name,
            'content': node.get_text(strip=True),
            'attributes': node.attrs if node.name == 'a' else None,
            'children': [process_node(child) for child in node.children if is_valid_child(child)]
        }
    elif isinstance(node, NavigableString) and node.strip():
        return {
            'type': 'text',
            'content': node.strip()
        }
    else:
        return {
            'type': 'container',
            'children': [process_node(child) for child in node.children if is_valid_child(child)]
        }

def extract_semantic_structure(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body = soup.body if soup.body else soup
    return process_node(body)

def main():
    url = 'https://vsr.informatik.tu-chemnitz.de/about/people/'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        structured_data = extract_semantic_structure(html_content)
        print('Semantic Structure:')
        print(structured_data)
    else:
        print(f'Failed to retrieve the webpage: {response.status_code}')

if __name__ == '__main__':
    main()