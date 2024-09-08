from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="tr", class_="athing")
article_link = []
article_text = []

for tag in articles:
    article = tag.select_one(selector="td span a")
    article_link.append(article.get("href"))
    article_text.append(article.getText())


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

#? My solution
# high_score = 0
# for index, score in enumerate(article_upvotes):
#     if score > high_score:
#         high_score = score
#         high_score_index = index

# print("MOST UPVOTED NEWS")
# print("-----------------")
# print(f"Title: {article_text[high_score_index]}")
# print(f"Link: {article_link[high_score_index]}")
# print(f"Upvotes: {high_score}")

#? Angela solution

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_number)
print(article_text[largest_index])
print(article_link[largest_index])