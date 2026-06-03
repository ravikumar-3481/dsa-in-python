import requests as req
from bs4 import BeautifulSoup as bs

def scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = req.get(url, headers=headers)
        if response.status_code == 200:
            soup = bs(response.content, 'html.parser')
            page_title = soup.title.string if soup.title else 'No match found'
            print(f"Title of the page: {page_title}")
            headings = soup.find_all(['h1', 'li', 'a', 'p'])
            print("Headings found on the page:")
            for heading in headings:
                print(heading.get_text(strip=True))
            print("Page content: ")
            print('*' * 40)
            
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

url = "https://www.geeksforgeeks.org/dsa/analysis-of-algorithms/"
scraper(url)

