from bs4 import BeautifulSoup
import lxml

with open("/home/siddique/Desktop/100 days of my couse/day_45/bs4-start/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# all_anchor_tags = soup.find_all(name="a")
# print(all_the_anchortags)
#for tags in all_anchor_tags:
    #print(tags.getText())
    #print(tags.get("a"))

# heading = soup.find(name= "h1",id = "name")
# print(heading)

company_url = soup.select("p a")
print(company_url)



