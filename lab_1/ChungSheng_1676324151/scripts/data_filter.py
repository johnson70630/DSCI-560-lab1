import csv
import os
from bs4 import BeautifulSoup

def main():
  raw_data_file = '../data/raw_data/web_data.html'
  market_data_path = '../data/processed_data/market_data.csv'
  news_data_path = '../data/processed_data/news_data.csv'
  with open(raw_data_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
  market_data = []
  banner = soup.find('div', {'class':"MarketsBanner-main"})
  market_cards = banner.find_all('a', {'class':lambda x: x and "MarketCard-wrap" in x})
  print(banner)
  for card in market_cards:
    symbol = card.find('span', {'class':"MarketCard-symbol"}).get_text(strip=True)
    stock_position = card.find('span', {'class':"MarketCard-stockPosition"}).get_text(strip=True)
    change_pct = card.find('span', {'class':"MarketTop-changePct"}).get_text(strip=True)
    market_data.append([symbol, stock_position, change_pct])
  with open(market_data_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['marketCard_symbol', 'marketCard_stockPosition', 'marketCard_changePct'])
    writer.writerows(market_data)
  print(f'Market data has been saved to {market_data_path}')

  news_data = []
  news_items = soup.select('.LatestNews-item')
  for item in news_items:
    timestamp = item.select_one('.LatestNews-timestamp').text.strip()
    title = item.select_one('.LatestNews-headline').text.strip()
    link = item.select_one('.LatestNews-headline')['href'].strip()
    news_data.append([timestamp, title, link])

  with open(news_data_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['LatestNews-timestamp', 'title', 'link'])
    writer.writerows(news_data)
  print(f'Latest news data has been saved to {news_data_path}')

if __name__ == "__main__":
  main()
