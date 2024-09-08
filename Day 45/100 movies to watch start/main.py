import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL)
page_text = response.text

soup = BeautifulSoup(page_text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

with open("Day 45/100 movies to watch start/movies.txt", "a", encoding="utf-8") as file:
    for movie in reversed(all_movies):
        movie_name = movie.getText()
        file.write(movie_name + "\n")




