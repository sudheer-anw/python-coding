import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    Fetch the content of the web page.
    
    :param url: The URL of the web page to fetch.
    :return: The HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_blog_posts(html):
    """
    Parse the HTML content and extract blog post information.
    
    :param html: The HTML content of the page.
    :return: A list of blog post titles and links.
    """
    soup = BeautifulSoup(html, 'html.parser')
    posts = []
    
    # Example parsing - adjust selectors based on the actual HTML structure
    for post in soup.find_all('article', class_='post'):
        title_tag = soup.find('h2', class_='post-title')
        link_tag = soup.find('a', class_='read-more')
        
        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            posts.append((title, link))
    
    return posts

def main():
    url = 'https://openweather.co.uk/blog/category/weather'  # Replace with the actual URL you want to scrape
    html = fetch_page(url)
    
    if html:
        posts = parse_blog_posts(html)
        
        if posts:
            print("Blog Posts Found:")
            for title, link in posts:
                print(f"Title: {title}")
                print(f"Link: {link}")
                print()
        else:
            print("No blog posts found.")
    else:
        print("Failed to retrieve the web page.")

if __name__ == "__main__":
    main()


