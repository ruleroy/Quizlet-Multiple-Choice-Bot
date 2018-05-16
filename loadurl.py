import urllib
import asyncio

def process_url(url):
    try:
        print(f"\nSearching url: {url}")
        resource = urllib.request.urlopen(url)
        return resource.read().decode(resource.headers.get_content_charset())
    except:
        return ""
