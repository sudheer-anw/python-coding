import requests
from bs4 import BeautifulSoup 

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("/home/siddique/Desktop/100 days of my couse/day_45/100 movies to watch.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
