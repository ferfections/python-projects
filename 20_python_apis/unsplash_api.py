import requests

def fetch_first_photo_url(query):
    url = f"https://unsplash.com/search/photos?query={query}"

    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()['results']
        if results:
            return results[0]['urls']['regular']
        else:
           return None
    return None

def main():
  pass  
    
