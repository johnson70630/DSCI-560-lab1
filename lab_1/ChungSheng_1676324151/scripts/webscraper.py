import requests
from bs4 import BeautifulSoup

def main():
  response = requests.get('https://www.cnbc.com/world/?region=world')
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    file_path = '../data/raw_data/web_data.html'
    with open(file_path, 'w', encoding='utf-8') as file:
      file.write(soup.prettify())
    print(f'Data saved to {file_path}')

if __name__ == "__main__":
  main()
