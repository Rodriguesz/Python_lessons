from bs4 import BeautifulSoup

with open("Day 45/website.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
#? returns completed tag
# print(soup.title)

#? returns content
# print(soup.title.string)

#? returns the html code (.prettify() is just a print easier to read)
# print(soup.prettify())

#? returns the first tag specified
# print(soup.p)

#? returns all the specified tag
all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# heading2 = soup.find(name="h3", class_="heading")
# print(heading)
# print(heading2)


#? selects a a-tag inside a p-tag
# company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")