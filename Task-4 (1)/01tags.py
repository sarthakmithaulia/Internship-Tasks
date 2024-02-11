from bs4 import BeautifulSoup

html_snippet = 'https://etherscan.io/accounts/label/take-action'

soup = BeautifulSoup(html_snippet, 'html.parser')


text_content = soup.get_text(strip=True)
print(f'Text: {text_content}')
soup.find_all('a')

link = soup.get('href')
print(f'Link: {link}')


tags = soup.find_all()
print(f'Tags: {tags}')
