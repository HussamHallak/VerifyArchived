import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []
    except Exception as e:
         print(f"An error occurred: {e}")
         return []
    
if __name__ == '__main__':
    url = input("Enter the website URL: ")
    all_links = extract_links(url)
    if all_links:
      for link in all_links:
        print(link)
